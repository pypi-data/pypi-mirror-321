import os
from rustmaps import Generator
import click


@click.group()
def app():
    """Initialize the generator and store it in the context"""
    ctx = click.get_current_context()
    ctx.ensure_object(dict)
    ctx.obj["generator"] = Generator()
    ctx.obj["generator"].load_config()


@app.command()
@click.option("--api-key", prompt="Enter your API key", help="Your RustMaps API key")
@click.pass_context
def login(ctx, api_key):
    g = ctx.obj["generator"]
    g.config.api_key = api_key
    g.save_config()


@app.command("list")
@click.pass_context
def _list(ctx):
    g = ctx.obj["generator"]
    imported = g.list_imported()
    print(f"Imported maps: ({len(imported)})")
    for map in imported:
        print(f"  - {map}")


@app.command("import")
@click.option(
    "--maps-path",
    prompt="Enter the path to the maps file",
    help="Path to the maps file",
)
@click.option(
    "--force",
    is_flag=True,
    help="Force import (caution: overwrites existing imported map file with same name)",
)
@click.pass_context
def _import(ctx, maps_path: str, force: bool):
    g = ctx.obj["generator"]
    maps_path = os.path.abspath(maps_path)
    if not os.path.isfile(maps_path):
        raise FileNotFoundError(f"File not found: {maps_path}")
    try:
        g._import(maps_path, force)
    except FileExistsError:
        pass


@app.command()
@click.option(
    "--maps-name",
    prompt="Enter the map name",
    help="Name of the map to destroy (find this using `rustmaps list`)",
)
@click.pass_context
def destroy(ctx, maps_name: str):
    g = ctx.obj["generator"]
    g.destroy(maps_name)


@app.command()
@click.option(
    "--maps-name",
    prompt="Enter the map name",
    help="Name of the map to generate (find this using `rustmaps list`)",
)
@click.option("--once", is_flag=True, help="Generate only once")
@click.pass_context
def generate(ctx, maps_name: str, once: bool):
    g = ctx.obj["generator"]
    g.select(maps_name)
    while g.generate():
        if once:
            break

@app.command()
@click.option(
    "--maps-name",
    prompt="Enter the map name",
    help="Name of the map to download (find this using `rustmaps list`)",
)
@click.option("--version", prompt="Enter the version", default="latest", help="Version suffix that will be applied to your map")
@click.pass_context
def download(ctx, maps_name: str, version: str):
    g = ctx.obj["generator"]
    g.select(maps_name)
    g.download(version)

if __name__ == "__main__":
    app(obj={})
