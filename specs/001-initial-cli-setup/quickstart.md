# Quickstart: Todo CLI Application

This guide explains how to set up and run the Todo CLI application.

## Prerequisites
- Python 3.13+
- `uv` (for environment management, as specified in the constitution)

## Setup
1.  **Create a virtual environment**:
    ```sh
    uv venv
    ```

2.  **Activate the virtual environment**:
    ```sh
    # Windows
    .venv\Scripts\activate

    # macOS/Linux
    source .venv/bin/activate
    ```

## Running the Application
Once the environment is set up and activated, you can run the application from the root of the project directory:

```sh
python -m src.todo.main
uv run python -m todo.main
```

The application will start, and you will see a menu of options to manage your tasks.
