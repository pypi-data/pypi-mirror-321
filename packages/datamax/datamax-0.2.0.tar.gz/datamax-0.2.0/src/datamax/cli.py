import click
import pathlib
from datamax.console import tty
from datamax.publish import Publisher
import os

@click.group(name="datamax")
def main():
    tty.log("Welcome to Datamax CLI")

@main.command()
@click.argument("directory")
def publish(directory: str):
    api_host = os.getenv("SUBSTRATE_API_HOST")
    if not api_host:
        tty.log("SUBSTRATE_API_HOST is not set")
        return
    path = pathlib.Path(directory).absolute()
    tty.log(f"Publishing from {path}...")
    publisher = Publisher("substrate", path, api_host)
    publisher.publish()

if __name__ == "__main__":
    main()
