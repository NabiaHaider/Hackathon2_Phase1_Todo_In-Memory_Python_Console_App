import typer
from typing import Optional
from typing_extensions import Annotated
from src.todo.service import TodoService
from src.todo.models import Task

# Annotated is needed for newer Typer argument syntax
# from typing_extensions import Annotated

app = typer.Typer(name="todo")
_service: Optional[TodoService] = None # Global service instance, to be set by main.py

def set_service(svc: TodoService):
    global _service
    _service = svc

@app.command()
def add(
    title: str = typer.Argument(..., help="Title of the task."),
    description: Optional[str] = typer.Option(None, "--description", "-d", help="Optional description for the task.")
):
    """
    Adds a new task to the todo list.
    """
    if _service is None:
        typer.echo("Error: Service not initialized.", err=True)
        raise typer.Exit(code=1)
    if not title: # Typer's Argument(...) should handle this, but keeping for explicit check
        typer.echo("Error: Title cannot be empty.", err=True)
        raise typer.Exit(code=1)
    
    task = _service.add_task(title=title, description=description if description is not None else "")
    typer.echo(f"Task '{task.title}' added with ID {task.id}.")
    if task.description:
        typer.echo(f"Description: {task.description}")

@app.command(name="list") # Added name to avoid conflict with python's list
def list_tasks_cmd(): # Renamed to avoid conflict with python's list
    """
    Lists all tasks.
    """
    if _service is None:
        typer.echo("Error: Service not initialized.", err=True)
        raise typer.Exit(code=1)
    tasks = _service.list_tasks()
    if not tasks:
        typer.echo("No tasks found.")
        return

    for task in tasks:
        status = "[x]" if task.is_completed else "[ ]"
        desc = f" ({task.description})" if task.description else ""
        typer.echo(f"{status} {task.id}: {task.title}{desc}")

@app.command()
def update(
    task_id: Annotated[int, typer.Argument(help="ID of the task to update.")],
    title: Annotated[Optional[str], typer.Option("--title", "-t", help="New title for the task.")] = None,
    description: Annotated[Optional[str], typer.Option("--description", "-d", help="New description for the task.")] = None
):
    """
    Updates an existing task by its ID.
    """
    if _service is None:
        typer.echo("Error: Service not initialized.", err=True)
        raise typer.Exit(code=1)
    if title is None and description is None:
        typer.echo("Error: Provide at least a new title or description to update.", err=True)
        raise typer.Exit(code=1)

    updated_task = _service.update_task(task_id, title, description)
    if updated_task:
        typer.echo(f"Task {task_id} updated.")
    else:
        typer.echo(f"Error: Task with ID {task_id} not found.", err=True)
        raise typer.Exit(code=1)

@app.command()
def delete(
    task_id: Annotated[int, typer.Argument(help="ID of the task to delete.")]
):
    """
    Deletes a task by its ID.
    """
    if _service is None:
        typer.echo("Error: Service not initialized.", err=True)
        raise typer.Exit(code=1)
    if _service.delete_task(task_id):
        typer.echo(f"Task {task_id} deleted.")
    else:
        typer.echo(f"Error: Task with ID {task_id} not found.", err=True)
        raise typer.Exit(code=1)

@app.command()
def toggle(
    task_id: Annotated[int, typer.Argument(help="ID of the task to toggle status.")]
):
    """
    Toggles the completion status of a task by its ID.
    """
    if _service is None:
        typer.echo("Error: Service not initialized.", err=True)
        raise typer.Exit(code=1)
    if _service.toggle_task_status(task_id):
        typer.echo(f"Task {task_id} status toggled.")
    else:
        typer.echo(f"Error: Task with ID {task_id} not found.", err=True)
        raise typer.Exit(code=1)

# Functions for the interactive menu (as per clarified T022)
def display_main_menu():
    typer.echo("\n--- Todo CLI Menu ---")
    typer.echo("1. Add Task")
    typer.echo("2. View Tasks")
    typer.echo("3. Update Task")
    typer.echo("4. Delete Task")
    typer.echo("5. Toggle Task Status")
    typer.echo("6. Exit")
    typer.echo("---------------------")

def get_menu_choice() -> int:
    while True:
        try:
            choice = typer.prompt("Enter your choice (1-6)")
            int_choice = int(choice)
            if 1 <= int_choice <= 6:
                return int_choice
            else:
                typer.echo("Invalid choice. Please enter a number between 1 and 6.", err=True)
        except ValueError:
            typer.echo("Invalid input. Please enter a number.", err=True)

# The `app()` call is moved to main.py
# if __name__ == "__main__":
#     app()
