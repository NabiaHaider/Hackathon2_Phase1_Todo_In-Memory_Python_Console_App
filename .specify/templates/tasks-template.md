# Tasks: [FEATURE NAME]

**Input**: Specification from `specs/[###-feature-name]/spec.md`
**Constitution**: Adheres to `/.specify/memory/constitution.md`

**Methodology**: Tasks are structured for a Test-Driven Development (TDD) approach. For each feature, tests are written first, confirmed to fail, and then the implementation follows.

---

## Task Format

- Tasks are grouped by the files they modify.
- The workflow should follow: `models` -> `service` -> `cli` -> `main`.
- Tests for a module should be completed before the module's implementation.

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for a CLI application.
  The /sp.tasks command MUST replace these with actual, granular tasks
  derived from the feature specification.
  ============================================================================
-->

## 1. Models (`src/todo/models.py` and `tests/test_models.py`)

**Goal**: Define the data structures for the application.

- [ ] **Test**: Write a test in `tests/test_models.py` to verify the `Task` model can be created with a title, description, and default 'incomplete' status.
- [ ] **Implement**: Create the `Task` data class in `src/todo/models.py` to make the test pass.

## 2. Service (`src/todo/service.py` and `tests/test_service.py`)

**Goal**: Implement the core business logic for managing tasks.

### For "Add Task" Feature:
- [ ] **Test**: In `tests/test_service.py`, write a test for the `TodoService` to confirm that calling `add_task` increases the number of tasks and that the new task has the correct details.
- [ ] **Implement**: In `src/todo/service.py`, implement the `__init__` method for `TodoService` to manage an in-memory list of tasks.
- [ ] **Implement**: Implement the `add_task` method to create a new task and add it to the list. Make the test pass.

### For "View Tasks" Feature:
- [ ] **Test**: In `tests/test_service.py`, write a test to confirm `list_tasks` returns the current list of tasks.
- [ ] **Implement**: In `src/todo/service.py`, implement the `list_tasks` method.

### For "Update Task" Feature:
- [ ] **Test**: In `tests/test_service.py`, write a test to check that `update_task` correctly modifies the title and description of a specified task.
- [ ] **Implement**: In `src/todo/service.py`, implement the `update_task` method.

## 3. CLI (`src/todo/cli.py` and `tests/test_cli.py`)

**Goal**: Create the command-line interface for user interaction.

- [ ] **Test**: In `tests/test_cli.py`, write a test that simulates calling the CLI to add a task (e.g., `runner.invoke(app, ["add", "Test Title"])`) and asserts the output is correct. (Using a library like Typer's `CliRunner`).
- [ ] **Implement**: In `src/todo/cli.py`, create the main `app` object (e.g., using Typer or argparse).
- [ ] **Implement**: Implement the `add` command function that calls the `TodoService` to add a task and prints the result to the console.

## 4. Main Entrypoint (`src/todo/main.py`)

**Goal**: Wire everything together so the application can be executed.

- [ ] **Implement**: In `src/todo/main.py`, create the application entrypoint that runs the CLI.

---

## Implementation Strategy

1.  **Define Models**: Start with the data structures (`models.py`) and their tests.
2.  **Build Services**: Implement the business logic (`service.py`) that operates on the models, driven by tests.
3.  **Expose via CLI**: Create the user-facing commands (`cli.py`) that use the services, again, driven by tests.
4.  **Create Entrypoint**: Finally, create the main entrypoint (`main.py`) to make the application runnable.
5.  **Commit frequently** after each task or logical group of tasks is complete.