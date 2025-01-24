import csv
import json
import logging
import os
from typing import List
from platformdirs import PlatformDirs
from pydantic import BaseModel, Field
import requests
import sys
import time


class Config(BaseModel):
    api_key: str = Field(default="")


class Map(BaseModel):
    seed: str
    size: int
    saved_config: str
    staging: bool = Field(default=False)
    map_id: str = Field(default=None)
    status: str = Field(default="pending")


class RateLimiter(object):

    def __init__(self, calls_per_minute: int = 60):
        self.calls_per_minute = calls_per_minute
        self.interval = 60.0 / calls_per_minute  # time between calls in seconds
        self.last_call = 0.0

    def wait(self):
        """Wait until enough time has passed since the last call"""
        now = time.time()
        time_passed = now - self.last_call
        if time_passed < self.interval:
            time.sleep(self.interval - time_passed)
        self.last_call = time.time()


class Generator(object):

    api_url = "https://api.rustmaps.com/v4"
    backoff_time = 30

    def __init__(self):
        self.config: Config = Config()
        self.maps: List[Map] = list()
        self.target: str = None
        self.rate_limiter = RateLimiter(calls_per_minute=60)
        self.dirs: PlatformDirs = None
        self.config_path: str = None
        self.maps_dir: str = None
        self.cache_dir: str = None
        self.log_path: str = None
        self.init_dirs()
        self.setup_logging()

    def init_dirs(self):
        self.dirs = PlatformDirs("rustmaps-generator", "mainloot")
        os.makedirs(self.dirs.user_cache_dir, exist_ok=True)
        os.makedirs(self.dirs.user_config_dir, exist_ok=True)
        os.makedirs(self.dirs.user_data_dir, exist_ok=True)
        os.makedirs(self.dirs.user_log_dir, exist_ok=True)
        self.config_path = os.path.join(self.dirs.user_config_dir, "config.json")
        self.maps_dir = os.path.join(self.dirs.user_data_dir, "maps")
        self.cache_dir = self.dirs.user_cache_dir
        self.log_path = os.path.join(self.dirs.user_log_dir, "generator.log")
        os.makedirs(self.maps_dir, exist_ok=True)

    def setup_logging(self):
        logging.basicConfig(
            filename=self.log_path,
            level=logging.INFO,
            format="%(asctime)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        # Create a stream handler for stdout
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)  # Set the logging level for stdout
        console_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s - %(message)s",  # Same format as file logging
                datefmt="%Y-%m-%d %H:%M:%S",
            )
        )

        # Add the console handler to the root logger
        logging.getLogger().addHandler(console_handler)

    def load_config(self):
        if not os.path.isfile(self.config_path):
            with open(self.config_path, "w") as config_file:
                # dump the default value for Config
                json.dump(Config().model_dump(), config_file, indent=4)

        with open(self.config_path) as config_file:
            self.config = Config.model_validate(json.load(config_file))

    def save_config(self):
        with open(self.config_path, "w") as config_file:
            json.dump(self.config.model_dump(), config_file, indent=4)

    def get_maps_file_name(self, maps_path: str):
        maps_name = os.path.basename(maps_path)
        if maps_name.endswith(".sv.csv"):
            maps_name = maps_name.replace(".sv.csv", "")
        if maps_name.endswith(".csv"):
            maps_name = maps_name.replace(".csv", "")
        return maps_name

    def _import(self, maps_path: str, force=False):
        maps_name = self.get_maps_file_name(maps_path)
        imported_path = os.path.join(self.maps_dir, f"{maps_name}.sv.csv")

        if not force and os.path.isfile(imported_path):
            logging.error(
                f"Map {maps_name} already exists in {self.maps_dir}. Use force=True to overwrite."
            )
            raise FileExistsError(
                f"Map {maps_name} already exists in {self.maps_dir}. Use force=True to overwrite."
            )

        with open(maps_path, "r") as map_file:
            with open(imported_path, "w") as dest_file:
                dest_file.write(map_file.read())

        logging.info(f"Imported map from {maps_path} to {imported_path}")

    def select(self, maps_name: str):

        maps_name = self.get_maps_file_name(maps_name)
        target = os.path.join(self.maps_dir, f"{maps_name}.sv.csv")

        if not os.path.isfile(target):
            logging.error(f"Map {maps_name} not found.")
            raise FileNotFoundError(f"Map {maps_name} not found.")

        self.maps = list()
        self.target = target
        self.load()

    def destroy(self, maps_name: str):

        maps_name = self.get_maps_file_name(maps_name)
        target = os.path.join(self.maps_dir, f"{maps_name}.sv.csv")

        if not os.path.isfile(target):
            logging.error(f"Map {maps_name} not found.")
            raise FileNotFoundError(f"Map {maps_name} not found.")

        os.remove(target)
        logging.info(f"Map {maps_name} removed.")

    def list_imported(self):
        return [
            f.replace(".sv.csv", "")
            for f in os.listdir(self.maps_dir)
            if f.endswith(".sv.csv")
        ]

    def load(self):

        if not self.target:
            raise ValueError("No map file selected.")

        with open(self.target) as map_file:
            maps = csv.DictReader(map_file)
            for map in maps:
                self.maps.append(Map.model_validate(map))

    def save(self):
        with open(self.target, "w") as maps_file:
            writer = csv.DictWriter(
                maps_file,
                fieldnames=[
                    "seed",
                    "size",
                    "saved_config",
                    "staging",
                    "map_id",
                    "status",
                ],
            )
            writer.writeheader()
            for map in self.maps:
                writer.writerow(map.model_dump())

    def download_map(self, map: Map, version: str = "latest"):

        if not self.target:
            logging.error("No map file selected.")
            raise ValueError("No map file selected.")

        maps_name = self.get_maps_file_name(self.target)
        download_dir = os.path.join(self.cache_dir, maps_name, version, map.seed)

        os.makedirs(download_dir, exist_ok=True)
        status = self.sync_status(map)

        if "data" in status and "canDownload" not in status.get("data", {}):
            logging.error(f"Map {map.seed} failed to obtain download information.")
            return

        if not status["data"]["canDownload"]:
            logging.error(f"Map {map.seed} is not ready for download.")
            return
        
        downloads = [
            {
                "name": "map",
                "url": status["data"]["downloadUrl"],
                "extension": "map",
            },
            {
                "name": "image",
                "url": status["data"]["imageUrl"],
                "extension": "png",
            },
            {
                "name": "image_with_icons",
                "url": status["data"]["imageIconUrl"],
                "extension": "png",
            },
            {
                "name": "thumbnail",
                "url": status["data"]["thumbnailUrl"],
                "extension": "png",
            }
        ]

        logging.info(f"Downloading map {map.seed} to {download_dir}")

        prefix = f"{map.seed}_{map.size}_{map.saved_config}_{version}"
        for download in downloads:
            download_path = os.path.join(download_dir, f"{prefix}_{download['name']}.{download['extension']}")
            logging.info(f"Downloading {download['name']} to {download_path}")
            response = requests.get(download["url"])
            with open(download_path, "wb") as file:
                file.write(response.content)
        
        logging.info(f"Map {map.seed} downloaded successfully")


    def generate_map(self, map: Map):
        """Generate a map using the Rustmaps API."""

        self.rate_limiter.wait()

        body = {
            "mapParameters": {
                "size": map.size,
                "seed": map.seed,
                "staging": map.staging,
            },
            "configName": map.saved_config,
        }

        logging.debug(
            f"POST /maps/custom/saved-config - Generating map with seed {map.seed}"
        )
        response = requests.post(
            f"{Generator.api_url}/maps/custom/saved-config",
            headers={
                "X-API-Key": self.config.api_key,
                "Content-Type": "application/json",
            },
            json=body,
        )
        logging.debug(f"Response: {response.status_code}")

        if map_id := response.json().get("data", {}).get("mapId"):
            map.map_id = map_id

        if response.status_code == 200:
            logging.info(f"Map {map.seed} has already generated successfully")
            map.status = "complete"
        elif response.status_code == 201:
            logging.info(f"Map {map.seed} has begun generating")
            map.status = "generating"
        elif response.status_code == 401:
            logging.error(f"Unauthorized Map {map.seed}. Check your API key.")
            map.status = "unauthorized"
        elif response.status_code == 403:
            logging.error(f"Forbidden Map {map.seed}. Check your API key.")
            map.status = "forbidden"
        elif response.status_code == 409:
            logging.info(f"Map {map.seed} is still generating")
            map.status = "generating"
        self.save()

    def sync_status(self, map: Map):
        """Fetch the map status from the Rustmaps API."""
        self.rate_limiter.wait()

        logging.debug(f"GET /maps/{map.map_id} - Checking status")
        response = requests.get(
            f"{Generator.api_url}/maps/{map.map_id}",
            headers={"X-API-Key": self.config.api_key},
        )
        logging.debug(f"Response: {response.status_code}")

        if response.status_code == 200:
            logging.info(f"Map {map.seed} has completed generation")
            map.status = "complete"
        elif response.status_code == 401:
            logging.error(f"Unauthorized Map {map.seed}. Check your API key.")
            map.status = "unauthorized"
        elif response.status_code == 403:
            logging.error(f"Forbidden Map {map.seed}. Check your API key.")
            map.status = "forbidden"
        elif response.status_code == 404:
            logging.error(f"Map {map.seed} not found")
            map.status = "not found"
        elif response.status_code == 409:
            logging.info(f"Map {map.seed} is still generating")
            map.status = "generating"
        self.save()
        try:
            return response.json()
        except:
            return {}

    def get_limits(self):
        """Fetch the map size limits from the Rustmaps API."""
        self.rate_limiter.wait()

        logging.debug("GET /maps/limits - Checking API limits")
        response = requests.get(
            f"{Generator.api_url}/maps/limits",
            headers={"X-API-Key": self.config.api_key},
        )
        logging.debug(f"Response: {response.status_code}")

        if response.status_code == 200:
            return response.json()

    def can_generate(self):
        """Wait until the concurrent map generation limit is no longer reached."""
        limits = self.get_limits()
        concurrent_limits = limits.get("data", {}).get("concurrent", {})
        current = concurrent_limits.get("current", 0)
        allowed = concurrent_limits.get("allowed", 0)
        return current < allowed

    def get_generating(self):
        """Get the maps that are currently generating."""
        return [m for m in self.maps if m.status == "generating"]

    def get_pending(self):
        """Get the maps that are pending generation."""
        return [m for m in self.maps if m.status == "pending"]

    def generate(self):
        """Generate maps using the Rustmaps API."""

        if not self.config.api_key:
            logging.error(
                "API key not set. Use `rustmaps-generator login` to set your API key."
            )
            raise ValueError(
                "API key not set. Use `rustmaps-generator login` to set your API key."
            )

        if not self.maps:
            if not self.target:
                logging.info(
                    "No maps loaded. Use `rustmaps-generator select` to load a map file."
                )
            else:
                logging.info("Empty map file. Nothing to generate.")
            return False

        generating = self.get_generating()
        pending = self.get_pending()

        for map in generating:
            self.sync_status(map)

        if not (pending or generating):
            # if there's nothing to process, we're done
            return False
        elif not (pending and self.can_generate()):
            # either nothing's pending or we've hit a generation limit
            time.sleep(Generator.backoff_time)
            return True

        map = pending[0]
        self.generate_map(map)
        time.sleep(2)
        return True

    def download(self, version: str = "latest"):
        """Download a generated map using the Rustmaps API."""

        if not self.target:
            logging.error("No map file selected.")
            raise ValueError("No map file selected.")

        if not self.maps:
            logging.error(
                "No maps loaded. Use `rustmaps-generator select` to load a map file."
            )
            raise ValueError(
                "No maps loaded. Use `rustmaps-generator select` to load a map file."
            )

        maps_name = self.get_maps_file_name(self.target)
        for map in self.maps:
            if map.status == "complete":
                self.download_map(map, version)
            else:
                logging.error(f"Map {map.seed} is not complete. Skipping download.")
                continue
