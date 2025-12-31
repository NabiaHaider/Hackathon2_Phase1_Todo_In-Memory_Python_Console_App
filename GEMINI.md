# Gemini Development Guidelines

## Purpose
This document outlines the guidelines and principles for the Gemini AI agent when interacting with and contributing to this repository. It ensures consistency, adherence to development methodologies, and clear operational boundaries.

## Rules for Gemini
When working on this repository, Gemini **MUST** adhere to the following rules:

- **Follow `constitution.md` strictly:** All actions and code modifications must align with the project's established constitution.
- **Follow spec-first development:** Every feature, bug fix, or change must originate from a clear, approved specification.
- **Do not write code without an approved spec:** Code implementation is prohibited without a preceding, formally approved specification.
- **Respect folder boundaries:** Maintain the established project structure and organization. Do not introduce new top-level directories or alter the intended purpose of existing ones without explicit instruction.
- **No manual coding by humans:** The repository is managed through AI-driven development. Direct human modification of the codebase should be minimized and, ideally, only for initial setup or critical fixes outside of the AI workflow.

## Gemini's Workflow
Gemini should follow this workflow for development tasks:

- **Read Specs:** Thoroughly understand and parse the provided specifications (`specs/` directory) to grasp the requirements and scope of the task.
- **Generate Plans:** Based on the spec, formulate a detailed technical plan, considering architecture, data models, and implementation steps. This plan should be reviewed and approved.
- **Break Tasks:** Decompose the approved plan into smaller, manageable, and testable sub-tasks.
- **Implement Code:** Write, test, and integrate code strictly according to the detailed tasks and approved plan, ensuring all project conventions are followed.

## Do / Do Not
- **DO:**
    - Always refer to `constitution.md` for project principles.
    - Prioritize reading and understanding specifications.
    - Propose detailed plans before implementation.
    - Create small, testable, and focused changes.
- **DO NOT:**
    - Implement features without an approved spec.
    - Deviate from established folder structures.
    - Write code manually or make assumptions outside the specified context.
    - Skip the planning and task-breaking phases.