import json
import os
import re
from unittest.mock import patch
import pytest
import responses
import secrets
from src.rustmaps import Generator

API_KEY = "FU3ESIWUCNWQLVWBDS3FI1GBQ714V9JJRPY0USW1XAOUULPV"
headers = {"Content-Type": "application/json"}
limits_resp = json.load(open("tests/responses/limits.json"))
maps_resp = json.load(open("tests/responses/maps.json"))
saved_config_resp = json.load(open("tests/responses/saved_config.json"))


class TestGenerator:

    generator_instance = None

    def generate_random_hex(self):
        return secrets.token_hex(16)

    def limits_callback(self, request):
        global limits_resp
        return (200, headers, json.dumps(limits_resp))

    def maps_callback(self, request):
        global maps_resp

        # get map_id
        match = re.search(r"/maps/([a-f0-9]{32})$", request.url)
        if match:
            map_id = match.group(1)
            # You can use the extracted map_id if needed, e.g., to validate or modify maps_resp
            maps_resp["data"]["mapId"] = map_id
        
        # check if it's generating
        generating = TestGenerator.generator_instance.get_generating()
        for map in generating:
            if map.map_id == map_id:
                return (409, headers, json.dumps(maps_resp))
        return (200, headers, json.dumps(maps_resp))

    def saved_config_callback(self, request):
        global limits_resp, saved_config_resp
        limits_resp["data"]["concurrent"]["current"] += 1
        limits_resp["data"]["monthly"]["current"] += 1
        saved_config_resp["data"]["mapId"] = self.generate_random_hex()
        return (201, headers, json.dumps(saved_config_resp))

    @pytest.fixture(scope="class")
    def mock_dirs(self, tmp_path_factory):
        """Create temp directories for testing with class scope"""
        base_temp = tmp_path_factory.mktemp("test_generator")
        cache_dir = base_temp / "cache"
        config_dir = base_temp / "config"
        data_dir = base_temp / "data"
        maps_dir = data_dir / "maps"

        # Create all directories
        for dir_path in [cache_dir, config_dir, data_dir, maps_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)

        return {
            "cache_dir": str(cache_dir),
            "config_dir": str(config_dir),
            "data_dir": str(data_dir),
            "maps_dir": str(maps_dir),
        }

    @pytest.fixture(scope="class", autouse=True)
    def generator(self, mock_dirs):
        """Create a Generator instance with mocked directories"""
        with patch("src.rustmaps.PlatformDirs") as mock_platform_dirs:
            # Configure the mock
            mock_instance = mock_platform_dirs.return_value
            mock_instance.user_cache_dir = mock_dirs["cache_dir"]
            mock_instance.user_config_dir = mock_dirs["config_dir"]
            mock_instance.user_data_dir = mock_dirs["data_dir"]

            # Create generator instance
            generator = Generator()
            TestGenerator.generator_instance = generator  # Save to class-level attribute
            yield generator

    def test_initialization(self, generator, mock_dirs):
        """Test directory initialization"""
        # Basic assertions
        assert generator.config.api_key == ""
        assert generator.maps == list()
        assert generator.target is None
        assert generator.rate_limiter.calls_per_minute == 60
        assert generator.rate_limiter.interval == 1.0
        assert generator.rate_limiter.last_call == 0.0
        # Filesystem assertions
        assert os.path.exists(generator.dirs.user_cache_dir)
        assert os.path.exists(generator.dirs.user_config_dir)
        assert os.path.exists(generator.dirs.user_data_dir)
        assert os.path.exists(generator.maps_dir)
        # Check paths are correct
        assert generator.dirs.user_cache_dir == mock_dirs["cache_dir"]
        assert generator.dirs.user_config_dir == mock_dirs["config_dir"]
        assert generator.dirs.user_data_dir == mock_dirs["data_dir"]
        assert generator.maps_dir == os.path.join(mock_dirs["data_dir"], "maps")

    def test_load_config(self, generator):
        """Test loading configuration"""
        generator.load_config()
        assert os.path.exists(generator.config_path)
        assert generator.config.api_key == ""

    def test_save_config(self, generator):
        """Test saving configuration"""
        generator.config.api_key = API_KEY
        generator.save_config()
        generator.load_config()
        assert generator.config.api_key == API_KEY

    def test_import(self, generator):
        """Test importing maps"""
        generator._import(os.path.abspath("./tests/files/maps.csv"))
        # Check the file was copied
        assert os.path.exists(os.path.join(generator.maps_dir, "maps.sv.csv"))
        # attempting to import the same file twice without force will raise an error
        with pytest.raises(FileExistsError):
            generator._import(os.path.abspath("./tests/files/maps.csv"))

    def test_load(self, generator):
        # we haven't run select yet, so this will raise an error
        with pytest.raises(ValueError):
            generator.load()

    def test_select(self, generator):
        """Test selecting a map"""
        # can end with .csv
        generator.select("maps.csv")
        assert generator.target == os.path.join(generator.maps_dir, "maps.sv.csv")
        # or .sv.csv, both extensions get trimmed
        generator.select("maps.sv.csv")
        assert generator.target == os.path.join(generator.maps_dir, "maps.sv.csv")
        # this is what we'll be expecting to see
        generator.select("maps")
        assert generator.target == os.path.join(generator.maps_dir, "maps.sv.csv")
        # selecting a non-existent map will raise an error
        with pytest.raises(FileNotFoundError):
            generator.select("nonexistent")

    def test_get_generating(self, generator):
        """Test getting the generating status"""
        assert not generator.get_generating()

    def test_get_pending(self, generator):
        """Test getting the pending status"""
        pending = generator.get_pending()
        assert pending
        assert len(pending) == 52

    @responses.activate
    def test_generate(self, generator):
        """Test checking if we can generate a map"""

        global limits_resp, maps_resp, saved_config_resp

        responses.add_callback(
            responses.GET,
            f"{Generator.api_url}/maps/limits",
            callback=self.limits_callback,
        )
        responses.add_callback(
            responses.GET,
            re.compile(rf"{Generator.api_url}/maps/[a-f0-9]{{32}}$"),
            callback=self.maps_callback,
        )
        responses.add_callback(
            responses.POST,
            f"{Generator.api_url}/maps/custom/saved-config",
            callback=self.saved_config_callback,
        )

        generating = generator.get_generating()
        pending = generator.get_pending()
        generating_start = len(generating)
        pending_start = len(pending)
        assert generating_start == 0
        assert pending_start == 52

        for i in range(1, 4):
            assert generator.generate()
            assert limits_resp["data"]["concurrent"]["current"] == min(
                i, limits_resp["data"]["concurrent"]["allowed"]
            )
            assert limits_resp["data"]["monthly"]["current"] == min(
                i, limits_resp["data"]["monthly"]["allowed"]
            )
            generating = generator.get_generating()
            pending = generator.get_pending()
            assert len(generating) == i
            assert len(pending) == pending_start - i
