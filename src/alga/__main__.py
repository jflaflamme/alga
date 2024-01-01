from typing import Annotated

from rich import print
from typer import Argument, Typer

from alga import (
    __version__,
    cli_app,
    cli_channel,
    cli_input,
    cli_media,
    cli_power,
    cli_sound_output,
    cli_volume,
)
from alga.setup import setup_guide


app = Typer(no_args_is_help=True)
app.add_typer(cli_app.app, name="app")
app.add_typer(cli_channel.app, name="channel")
app.add_typer(cli_input.app, name="input")
app.add_typer(cli_media.app, name="media")
app.add_typer(cli_power.app, name="power")
app.add_typer(cli_sound_output.app, name="sound-output")
app.add_typer(cli_volume.app, name="volume")


@app.command()
def setup(hostname: Annotated[str, Argument()] = "lgwebostv") -> None:
    setup_guide(hostname)


@app.command()
def version() -> None:
    print(f"alga version [bold]{__version__}[/bold]")


if __name__ == "__main__":
    app()
