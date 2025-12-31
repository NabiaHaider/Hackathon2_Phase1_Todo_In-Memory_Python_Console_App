# The Evolution of Todo – Phase I

## Project Overview
This project presents a simple Command-Line Interface (CLI) Todo application, developed using a spec-driven AI development approach. It serves as a foundational example of how AI can assist in generating and managing project specifications, plans, and code.

## Features
- **Add Task:** Create new todo items with a title and an optional description.
- **View Tasks:** Display all tasks with clear status indicators (e.g., pending, completed).
- **Update Task:** Modify the title or description of an existing task.
- **Delete Task:** Remove a task from the list.
- **Toggle Completion:** Mark tasks as complete or incomplete.

## Project Structure
D:\Hackathon2\Phase1\
├───.gitignore
├───GEMINI.md
├───pyproject.toml
├───uv.lock
├───.gemini\
│   └───commands\
│       ├───sp.adr.toml
│       ├───sp.analyze.toml
│       ├───sp.checklist.toml
│       ├───sp.clarify.toml
│       ├───sp.constitution.toml
│       ├───sp.git.commit_pr.toml
│       ├───sp.implement.toml
│       ├───sp.phr.toml
│       ├───sp.plan.toml
│       ├───sp.reverse-engineer.toml
│       ├───sp.specify.toml
│       ├───sp.tasks.toml
│       └───sp.taskstoissues.toml
├───.git\...
├───.specify\
│   ├───memory\
│   │   └───constitution.md
│   ├───scripts\
│   │   └───powershell\
│   │       ├───check-prerequisites.ps1
│   │       ├───common.ps1
│   │       ├───create-new-feature.ps1
│   │       ├───setup-plan.ps1
│   │       └───update-agent-context.ps1
│   └───templates\
│       ├───adr-template.md
│       ├───agent-file-template.md
│       ├───checklist-template.md
│       ├───phr-template.prompt.md
│       ├───plan-template.md
│       ├───spec-template.md
│       └───tasks-template.md
├───.venv...\
├───history\
│   └───prompts\
│       ├───001-initial-cli-setup\
│       │   ├───001-create-initial-specification-for-todo-cli.spec.prompt.md
│       │   ├───002-create-implementation-plan-for-todo-cli.plan.prompt.md
│       │   ├───003-generate-tasks-for-todo-cli.tasks.prompt.md
│       │   └───004-implement-todo-cli-application-core.implement.prompt.md
│       └───constitution\
│           └───001-establish-initial-project-constitution-and-align-templates.constitution.prompt.md
├───specs\
│   └───001-initial-cli-setup\
│       ├───data-model.md
│       ├───plan.md
│       ├───quickstart.md
│       ├───research.md
│       ├───spec.md
│       ├───tasks.md
│       └───checklists\
│           └───requirements.md
├───src\
│   ├───__init__.py
│   ├───__pycache__\
│   ├───.venv...\
│   └───todo\
│       ├───__init__.py
│       ├───cli.py
│       ├───main.py
│       ├───models.py
│       ├───service.py
│       └───__pycache__\
├───tests\
│   ├───__init__.py
│   ├───test_cli.py
│   ├───test_models.py
│   ├───test_service.py
│   └───__pycache__\
└───todo_cli.egg-info\

## Requirements
- Python 3.13+
- uv (package installer and resolver)

## Setup Instructions (Windows)
1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Phase1 # or whatever your project directory is named
    ```
3.  **Navigate to the `src` directory:**
    ```bash
    cd src
    ```
4.  **Create a virtual environment using `uv`:**
    ```bash
    uv venv
    ```
5.  **Activate the virtual environment:**
    ```bash
    .venv\Scripts\activate
    ```
6.  **Run the Todo CLI application:**
    ```bash
    python -m todo.main
    ```

## Usage Instructions
The application provides a menu-driven command-line interface. Once started, follow the on-screen prompts to interact with your todo list.

## Notes
- **In-memory only:** All tasks are stored in memory and are not persisted.
- **Data resets on exit:** Your todo list will be cleared every time the application is closed.
