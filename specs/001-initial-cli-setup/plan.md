# Implementation Plan: Todo CLI Application (Phase I)

**Branch**: `001-initial-cli-setup` | **Date**: 2025-12-29 | **Spec**: [spec.md](./spec.md)

## 1. Overview
This document outlines the implementation plan for the "Todo CLI Application", a simple, in-memory, command-line task manager. The primary architectural goal is to establish a clean, modular structure with a strict separation of concerns, which will serve as a foundation for future phases. All code will be AI-generated based on the approved specification, with no manual coding.

## 2. High-Level Architecture
The system will be composed of four core modules within the `src/todo` directory, ensuring a clear separation of responsibilities.

- **`models.py`**: The data layer. It will define the `Task` data structure (id, title, description, is_completed). This module will have no dependencies on other parts of the application.
- **`service.py`**: The business logic layer. It will contain the `TodoService` class, which manages all operations on the in-memory list of tasks (add, update, delete, toggle, list). This module will depend only on `models.py`.
- **`cli.py`**: The presentation layer. It will handle all user interaction, including displaying menus, parsing user input, and formatting output. It will delegate all business operations to the `service` module. It depends on `service.py`.
- **`main.py`**: The application entry point. Its sole responsibility is to initialize the `TodoService` and the `cli`, and start the application loop.

**Data Flow**: User Input -> `cli.py` -> `service.py` -> `models.py`

## 3. Execution Order
Implementation will proceed in a bottom-up fashion to ensure foundational components are built and validated before dependent components are created.

1.  **Models (`models.py`)**: Define the `Task` data class first. This is the core data structure with no dependencies.
2.  **Service (`service.py`)**: Implement the `TodoService` to handle all task manipulations. This allows the core logic to be developed and tested independently of the user interface.
3.  **CLI (`cli.py`)**: Implement the user-facing command-line interface. With the service layer complete, the CLI can focus purely on presentation and input/output.
4.  **Main (`main.py`)**: Create the final entry point to wire all the components together.

This order ensures that at each step, the new component is built upon a stable, tested foundation.

## 4. Feature Mapping
Each functional requirement will be implemented across the `service` and `cli` modules.

| Feature               | Responsible Module(s) | Description                                         |
| --------------------- | --------------------- | --------------------------------------------------- |
| **Add Task**          | `service` + `cli`     | `cli` captures input; `service` creates the task.   |
| **View Tasks**        | `service` + `cli`     | `service` provides tasks; `cli` formats the list.   |
| **Update Task**       | `service` + `cli`     | `cli` gets ID/new data; `service` performs update.  |
| **Delete Task**       | `service` + `cli`     | `cli` gets ID/confirmation; `service` removes task. |
| **Toggle Task Status**| `service` + `cli`     | `cli` gets ID; `service` flips the status.          |

## 5. Risk & Validation Strategy
- **Risk 1: Invalid User Input**: The user may enter non-numeric values for menu choices, provide empty titles, or enter invalid commands.
  - **Validation**: The `cli.py` module will be solely responsible for input validation. It will contain robust checks to handle incorrect input gracefully, displaying clear error messages without crashing, as per the spec.

- **Risk 2: Incorrect Task ID Management**: Users may try to update or delete tasks with IDs that do not exist.
  - **Validation**: The `service.py` module will handle all ID-related logic. Before performing any operation, it will first verify the existence of the given task ID and return an error or specific status if it's not found.

- **Risk 3: State Management**: As an in-memory application, ensuring state is managed correctly for the duration of the session is critical.
  - **Validation**: The `TodoService` will encapsulate the list of tasks. Unit tests for the service layer will rigorously validate state changes for every operation (add, delete, update).

## 6. Definition of Done (Phase I)
This phase will be considered complete when:
- All four modules (`models`, `service`, `cli`, `main`) are implemented.
- All five functional requirements are fully working as per the specification.
- The application can be launched and operated from the command line.
- The code adheres strictly to the defined architecture and quality attributes.
- No manual code has been written in the `src` directory.
