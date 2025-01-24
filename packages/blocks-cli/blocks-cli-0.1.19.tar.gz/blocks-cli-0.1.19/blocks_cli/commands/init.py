import git
import typer
from blocks_cli.api import api_client
from blocks_cli.commands.__base__ import blocks_cli
from blocks_cli.config.config import config
from blocks_cli.console import console
from rich.progress import Progress, SpinnerColumn, TextColumn

from pathlib import Path

@blocks_cli.command()
def init(apikey: str = typer.Option(None, "--key", help="API key for authentication")):
    """Initialize blocks in the current directory."""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=False,
    ) as progress:

        working_dir = Path.cwd()
        try:
            repo = git.Repo(search_parent_directories=True)
            working_dir = repo.working_dir
        except Exception as e:
            pass

        working_dir = Path(working_dir)

        # Create .blocks directory if it doesn't exist
        blocks_dir = working_dir / ".blocks"

        if not blocks_dir.exists():
            blocks_dir.mkdir()
            folder_task = progress.add_task(description="Creating .blocks folder...", total=None)
            progress.update(folder_task, description=":white_check_mark: Created .blocks folder")

        progress.refresh()

        # Verify and save API key if provided
        if apikey:
            api_task = progress.add_task(description="Verifying API key...", total=None)

            try:
                response = api_client.get(f"{config.clients.client_url}/apikeys/{apikey}", headers={
                    "Authorization": f"ApiKey {apikey}"
                })
                if response.status_code > 299:
                    raise Exception("API Key is invalid. Please check your API key at [link=https://app.blocksorg.com]https://app.blocksorg.com[/link]")

                config.auth.save_api_key(apikey)
                progress.update(api_task, description=":white_check_mark: API key verified and saved successfully")
                progress.refresh()

            except Exception as e:
                message = str(e)
                progress.update(api_task, description=f":cross_mark: {message}")
                progress.refresh()
                raise typer.Exit(code=1)
    console.print(":white_check_mark: Blocks has been successfully initialized.")
