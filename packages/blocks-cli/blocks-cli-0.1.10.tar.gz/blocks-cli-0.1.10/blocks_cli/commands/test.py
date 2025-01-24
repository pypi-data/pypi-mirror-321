import git
import typer
from blocks_cli.api import api_client
from blocks_cli.commands.__base__ import blocks_cli
from blocks_cli.config.config import config
from blocks_cli.console import console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.rule import Rule

from pathlib import Path

from blocks_cli.registration import get_blocks_state_and_module_from_file


def invoke_automation_with_test_event(automation_module, automation):
    trigger_alias = automation.get("trigger_alias")
    function_name = automation.get("function_name")

    automation_name = automation.get("task_kwargs",{}).get("name")

    # get the function from the module
    function = getattr(automation_module, function_name)

    res = api_client.get(f"{config.clients.client_url}/test_events", params={
        "trigger_alias": trigger_alias,
    })
    res.raise_for_status()

    event_response = res.json()
    event_data = event_response.get("event_data")

    console.print(f"\n:rocket: Invoking automation {automation_name} with event {trigger_alias}\n", style="blue")
    console.print(
        Rule("[bold grey]Automation Logs[/bold grey]", characters="=", style="white")
    )

    res = function(event_data)

    console.print(
        Rule("[bold grey]END Automation Logs[/bold grey]", characters="=", style="white")
    )

    console.print(f"\n:white_check_mark: Automation {automation_name} invoked successfully\n", style="green")

       

@blocks_cli.command()
def test(
        file: Path = typer.Argument(..., help="Name of blocks file to test."),
        name: str = typer.Option(None, help="Name of the automation to test."),
    ):
    
    try:
        state, automation_module = get_blocks_state_and_module_from_file(file)
        automations = state.automations

        num_automations = len(automations)

        if num_automations == 1:
            automation = automations[0]

            if name and automation.get("task_kwargs",{}).get("name") != name:
                raise Exception(f"Automation with name {name} not found.")

            invoke_automation_with_test_event(automation_module, automation)

        elif num_automations > 1 and not name:
            raise Exception("Multiple automations found in the file, please specify which one to test.")
        elif num_automations > 1 and name:
            # find in automations
            automation = next((a for a in automations if a.get("task_kwargs",{}).get("name") == name), None)
            if not automation:
                raise Exception(f"Automation with name {name} not found.")
            
            invoke_automation_with_test_event(automation_module, automation)
        else:
            raise Exception("No valid automations file provided.")
        
    except Exception as e:
        console.print(f"\n:cross_mark: [red]Error: {e}[/red]")
        raise typer.Exit(1)
