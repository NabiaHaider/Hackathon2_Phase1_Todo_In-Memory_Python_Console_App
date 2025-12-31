# Tasks: Initial Todo CLI Implementation

**Input**: Design documents from `specs/001-initial-cli-setup/`
**Prerequisites**: `plan.md`, `spec.md`

**Methodology**: Tasks are structured for a Test-Driven Development (TDD) approach. For each module, tests are written first, confirmed to fail, and then the implementation follows. All tasks are part of the initial setup user story `[US1]`.

---

## Phase 1: Project & Test Setup
**Goal**: Create the required directory and file structure for the project and tests.

- [x] T001 [P] Create the main source directory: `src/todo/`
- [x] T002 [P] Create the tests directory: `tests/`
- [x] T003 [P] Create empty python files with `__init__.py` in `src/todo/`
- [x] T004 [P] Create empty test files in `tests/`: `test_models.py`, `test_service.py`, `test_cli.py`

---

## Phase 2: Models (`models.py` & `tests/test_models.py`)
**Goal**: Define and validate the `Task` data structure.

- [x] T005 [US1] **Test**: In `tests/test_models.py`, write a test to verify a `Task` can be created with an id, title, description, and correct default `is_completed` status.
- [x] T006 [US1] **Implement**: In `src/todo/models.py`, create the `Task` dataclass to make the test from T005 pass.

---

## Phase 3: Service Layer (`service.py` & `tests/test_service.py`)
**Goal**: Implement and validate the core business logic for managing tasks.

- [x] T007 [US1] **Test**: In `tests/test_service.py`, write a test for `TodoService.add_task()`. It should verify that adding a task increases the task count and the new task's details are correct.
- [x] T008 [US1] **Implement**: In `src/todo/service.py`, create the `TodoService` class with an in-memory list for tasks and an `add_task()` method to make the test from T007 pass.
- [x] T009 [US1] **Test**: In `tests/test_service.py`, write a test for `TodoService.list_tasks()`.
- [x] T010 [US1] **Implement**: In `src/todo/service.py`, implement `list_tasks()` to make the test from T009 pass.
- [x] T011 [US1] **Test**: In `tests/test_service.py`, write a test for `TodoService.update_task()`, including a case for a non-existent ID.
- [x] T012 [US1] **Implement**: In `src/todo/service.py`, implement `update_task()` to make the test from T011 pass.
- [x] T013 [US1] **Test**: In `tests/test_service.py`, write a test for `TodoService.delete_task()`.
- [x] T014 [US1] **Implement**: In `src/todo/service.py`, implement `delete_task()` to make the test from T013 pass.
- [x] T015 [US1] **Test**: In `tests/test_service.py`, write a test for `TodoService.toggle_task_status()`.
- [x] T016 [US1] **Implement**: In `src/todo/service.py`, implement `toggle_task_status()` to make the test from T015 pass.

---

## Phase 4: CLI Layer (`cli.py` & `tests/test_cli.py`)
**Goal**: Implement and validate the user-facing command-line interface. A library like `Typer` or `Click` is recommended, but `argparse` is also acceptable. We will assume `Typer` for testing examples.

- [x] T017 [US1] **Setup**: Add `typer` to the project's dependencies (e.g., in a `requirements.txt` or `pyproject.toml`).
- [x] T018 [US1] **Test**: In `tests/test_cli.py`, write a test for the 'add' command, using a test runner to invoke the command and assert the output.
- [x] T019 [US1] **Implement**: In `src/todo/cli.py`, set up the main `app` object and implement the `add` command function that calls the service. Make test T018 pass.
- [x] T020 [US1] **Test**: In `tests/test_cli.py`, write tests for the `list`, `update`, `delete`, and `toggle` commands.
- [x] T021 [US1] **Implement**: In `src/todo/cli.py`, implement the remaining commands to make the tests from T020 pass.
- [x] T022 [US1] **Implement**: In `src/todo/cli.py`, implement the main menu loop and input validation for user choices.

---

## Phase 5: Main Entrypoint (`main.py`)
**Goal**: Wire everything together to make the application executable.

- [x] T023 [US1] **Implement**: In `src/todo/main.py`, create the application entrypoint that initializes the `TodoService`, injects it into the `cli` layer, and starts the CLI app.

---

## Dependencies & Execution Order

- **Phase 1 (Setup)** must complete first.
- **Phase 2 (Models)** depends on Phase 1.
- **Phase 3 (Service)** depends on Phase 2.
- **Phase 4 (CLI)** depends on Phase 3.
- **Phase 5 (Main)** depends on Phase 4.

This linear, bottom-up dependency chain ensures a stable foundation for each layer.
