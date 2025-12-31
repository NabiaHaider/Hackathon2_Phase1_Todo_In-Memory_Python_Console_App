# Data Model: Todo Application

This document specifies the data entities for the Todo CLI application, as defined in the feature specification.

## Core Entities

### Task
Represents a single to-do item.

**Attributes**:

| Field          | Type    | Required | Default     | Description                               |
|----------------|---------|----------|-------------|-------------------------------------------|
| `id`           | Integer | Yes      | (Auto-gen)  | Unique identifier for the task at runtime.|
| `title`        | String  | Yes      | N/A         | The main description of the task.         |
| `description`  | String  | No       | `""` (empty)| Additional details about the task.        |
| `is_completed` | Boolean | Yes      | `False`     | The completion status of the task.        |

**Validation Rules**:
- `title` must not be an empty string.
- `id` must be unique within a single application session.

**State Transitions**:
- A `Task` is created with `is_completed` set to `False`.
- The `is_completed` status can be toggled between `True` and `False`.
