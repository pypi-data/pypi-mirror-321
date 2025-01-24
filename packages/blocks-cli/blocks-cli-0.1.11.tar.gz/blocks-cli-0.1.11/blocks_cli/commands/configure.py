from blocks_cli.config.config import config
from blocks_cli.console import console
from blocks_cli.commands.__base__ import blocks_cli
import typer

@blocks_cli.command()
def configure(apikey: str = typer.Option(None, "--key", help="Blocks API key")):
    """Configure the blocks CLI."""

    existing_api_key = config.auth.api_key
    lastDigits = existing_api_key[-8:] if existing_api_key else ""

    new_api_key = None
    if not apikey:
        console.print("\nEnter Blocks API Key below", style="bold", end=" ")

        if lastDigits:
            console.print(
                "[dim]leave empty if you want to keep existing API key: [/dim]",
                style="italic",
                end=" ",
            )
            console.print(f"[dim]...{lastDigits}[/dim]", style="italic")
        else:
            print()

        new_api_key = typer.prompt("API Key", existing_api_key, show_default=False)

    else:
        new_api_key = apikey


    if not new_api_key:
        console.print("\n:cross_mark: No API key has has been previously saved, please retry with a valid API key.\n")
        raise typer.Exit(code=1)

    try:
        config.auth.save_api_key(new_api_key)
    except Exception as e:
        console.print(f"\n:cross_mark: {e}\n")
        raise typer.Exit(code=1)
    
    last_digits = new_api_key[-8:]

    console.print(f"\n:white_check_mark: API key saved successfully [italic][dim]...{last_digits}[/dim][/italic]\n")