import typer
from src.todo.service import TodoService
import src.todo.cli as cli
from typer.testing import CliRunner # For programmatic invocation of CLI commands

def main():
    service = TodoService()
    cli.set_service(service) # Inject the service into the cli module

    runner = CliRunner() # Initialize CliRunner for programmatic command invocation

    typer.echo("Starting Todo CLI Application.")
    while True:
        cli.display_main_menu()
        choice = cli.get_menu_choice()

        if choice == 1:
            # Add Task
            title = typer.prompt("Enter task title")
            description = typer.prompt("Enter task description (optional)", default="")
            # Use runner to invoke the add command
            if description:
                result = runner.invoke(cli.app, ["add", title, "--description", description])
            else:
                result = runner.invoke(cli.app, ["add", title])
            typer.echo(result.stdout, nl=False) # nl=False to prevent extra newline

        elif choice == 2:
            # View Tasks
            result = runner.invoke(cli.app, ["list"])
            typer.echo(result.stdout, nl=False)

        elif choice == 3:
            # Update Task
            try:
                task_id = int(typer.prompt("Enter task ID to update"))
            except ValueError:
                typer.echo("Invalid ID. Please enter a number.", err=True)
                continue
            title = typer.prompt("Enter new title (leave empty to keep current)", default="")
            description = typer.prompt("Enter new description (leave empty to keep current)", default="")
            
            args = ["update", str(task_id)]
            if title:
                args.extend(["--title", title])
            if description:
                args.extend(["--description", description])
            
            if len(args) == 2: # Only 'update' and 'task_id' provided, no actual update parameters
                typer.echo("No update parameters provided.", err=True)
                continue

            result = runner.invoke(cli.app, args)
            typer.echo(result.stdout, nl=False)
            if result.exit_code != 0:
                typer.echo(result.stderr, nl=False, err=True)

        elif choice == 4:
            # Delete Task
            try:
                task_id = int(typer.prompt("Enter task ID to delete"))
            except ValueError:
                typer.echo("Invalid ID. Please enter a number.", err=True)
                continue
            result = runner.invoke(cli.app, ["delete", str(task_id)])
            typer.echo(result.stdout, nl=False)
            if result.exit_code != 0:
                typer.echo(result.stderr, nl=False, err=True)

        elif choice == 5:
            # Toggle Task Status
            try:
                task_id = int(typer.prompt("Enter task ID to toggle status"))
            except ValueError:
                typer.echo("Invalid ID. Please enter a number.", err=True)
                continue
            result = runner.invoke(cli.app, ["toggle", str(task_id)])
            typer.echo(result.stdout, nl=False)
            if result.exit_code != 0:
                typer.echo(result.stderr, nl=False, err=True)

        elif choice == 6:
            typer.echo("Exiting Todo CLI Application. Goodbye!")
            break

if __name__ == "__main__":
    main()
