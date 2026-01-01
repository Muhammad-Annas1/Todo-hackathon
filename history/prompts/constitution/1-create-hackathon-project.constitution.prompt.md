---
id: 1
title: Create Hackathon Project
stage: constitution
date: 2025-01-01
surface: agent
model: Qwen
feature: todo
branch: main
user: user
command: /sp.constitution
labels: [constitution, hackathon, todo-app]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```
Create a constitution for Phase I of a hackathon project: a simple in-memory Python console todo application.

Project Name: Todo (In-Memory Python Console Todo App)
Phase: I - Basic Level (Core Essentials)
Objective: Build a minimal, clean, command-line todo list application that stores tasks only in memory (no file/database persistence) and demonstrates the following 5 essential features:
1. Add new task (with title and description)
2. View all tasks (with ID, title, description, and completion status)
3. Update existing task details (title or description)
4. Delete task by ID
5. Mark task as complete / incomplete (toggle status)

Core Principles & Guidelines:

1. Code Quality
- Strictly follow PEP 8 style guide
- Use meaningful, self-documenting variable/function names
- Keep functions short and focused (single responsibility)
- Use type hints wherever possible (Python 3.13+)
- Minimal comments — code should be readable by itself
- Proper error handling with clear user messages

2. Project Structure
- Use UV for project & virtual environment management
- Standard layout:
  ├── .specify/                # Spec-Kit Plus artifacts
  │   ├── memory/
  │   │   └── constitution.md
  │   └── history/
  ├── src/                     # All source code here
  │   └── todo.py             # Main application file (or split if needed)
  ├── pyproject.toml
  └── README.md

3. User Experience Requirements
- Menu-driven CLI interface (loop until user quits)
- Clear numbered options (1: Add, 2: View, 3: Update, 4: Delete, 5: Toggle Complete, 0: Quit)
- Show tasks in clean table-like format with status indicators:
  [ ] → incomplete
  [X] → complete
- Handle all invalid inputs gracefully (wrong ID, empty title, etc.)
- Auto-generate incremental unique IDs for tasks

4. Technical Decisions
- Python 3.13+
- In-memory storage only: list of dictionaries or simple Task class
- No external dependencies (except possibly rich for better formatting — optional)
- No persistence (data resets on every program restart — intentional for Phase I)

5. Development Process (Spec-Driven Development)
- Use Spec-Kit Plus with Qwen model for code generation
- Generate detailed specs first → plans → tasks → implementation
- Preserve full specification history
- Human review of every AI-generated code block mandatory
- Aim for clean, production-ready quality even for hackathon MVP

6. Success Criteria
- All 5 core features must work perfectly
- Application runs without crashes
- Clean console output (readable even on small terminals)
- GitHub repository must contain:
  - Constitution file
  - Specs history folder
  - /src folder with working code
  - Detailed README with setup & usage instructions

7. Constraints & Non-Goals (Phase I)
- No due dates, priorities, categories, tags
- No search/filter functionality
- No user accounts
- No file save/load
- No tests required (but structure should allow easy addition later)
```

## Response snapshot

The constitution for the Todo (In-Memory Python Console Todo App) has been successfully created and saved to `.specify/memory/constitution.md`. The constitution establishes 6 core principles covering code quality, project structure, user experience requirements, technical decisions, development process, and success criteria. It also defines constraints and non-goals for Phase I, feature requirements, and governance procedures.

## Outcome

- ✅ Impact: Created initial constitution document for hackathon project
- 🧪 Tests: none
- 📁 Files: Updated .specify/memory/constitution.md with complete constitution
- 🔁 Next prompts: Build specification based on updated constitution
- 🧠 Reflection: Constitution successfully created with all required principles and guidelines

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A