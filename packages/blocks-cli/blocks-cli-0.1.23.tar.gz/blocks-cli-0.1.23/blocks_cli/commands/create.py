import re
import typer
from pathlib import Path

from blocks_cli.console import console
from blocks_cli.commands.__base__ import blocks_cli
from blocks_cli.fs import find_dir
from blocks_cli.package import warn_current_package_version, get_latest_sdk_version

class InvalidAutomationNameError(Exception):
    pass

class NoBlocksDirError(Exception):
    pass

class AutomationAlreadyExistsError(Exception):
    pass

@blocks_cli.command()
def create(
    name: str = typer.Argument(..., help="Name of the automation to create."),
):
    """
    Create a new automation in the .blocks directory.
    The command will fail if .blocks directory doesn't exist.
    """
    try:
        warn_current_package_version()

        # Validate automation name (only allow alphanumeric, dash, and underscore)
        if not name or re.search(r'[^a-zA-Z0-9\_]', name):
            raise InvalidAutomationNameError("Automation name must contain only letters, numbers, and underscores")

        blocks_dir = find_dir(target=".blocks")

        if not blocks_dir:
            raise NoBlocksDirError("No .blocks directory found, have you run `blocks init`?")

        # Create automation directory
        automation_dir = blocks_dir / name
        if automation_dir.exists():
            raise AutomationAlreadyExistsError(f"Automation '{name}' already exists")

        try:
            # Create directory and files
            automation_dir.mkdir(parents=True)
            
            # Create main.py with basic template
            with open(automation_dir / 'main.py', 'w') as f:
                f.write('''from blocks import task, on

@task(name="{name}")
@on("", repos=[])
def {name}(input):
    print(input)
'''.format(name=name))

            sdk_version = get_latest_sdk_version()
            latest_version = sdk_version.get("latest_version")

            with open(automation_dir / 'requirements.txt', 'w') as f:
                f.write('''blocks-sdk>={version}'''.format(version=latest_version))

            console.print(f":white_check_mark: Successfully created automation '{name}' in [green]{automation_dir.absolute()}[/green]")

        except Exception as e:
            # Clean up if something goes wrong after directory creation
            if automation_dir.exists():
                try:
                    import shutil
                    shutil.rmtree(automation_dir)
                except Exception:
                    pass
            raise
        
    except (InvalidAutomationNameError, NoBlocksDirError, AutomationAlreadyExistsError) as e:
        console.print(f"\n:cross_mark: [red]{str(e)}[/red]")
        raise typer.Exit(1)
    except Exception as e:
        console.print(f"\n:cross_mark: [red]Error creating automation: {str(e)}[/red]")
        raise typer.Exit(1)