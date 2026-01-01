# Todo (In-Memory Python Console Todo App) Constitution

## Core Principles

### Code Quality
Strictly follow PEP 8 style guide; Use meaningful, self-documenting variable/function names; Keep functions short and focused (single responsibility); Use type hints wherever possible (Python 3.13+); Minimal comments — code should be readable by itself; Proper error handling with clear user messages

### Project Structure
Use UV for project & virtual environment management; Standard layout with .specify/, src/, pyproject.toml, and README.md; All source code in src/ directory

### User Experience Requirements
Menu-driven CLI interface (loop until user quits); Clear numbered options (1: Add, 2: View, 3: Update, 4: Delete, 5: Toggle Complete, 0: Quit); Show tasks in clean table-like format with status indicators; Handle all invalid inputs gracefully; Auto-generate incremental unique IDs for tasks

### Technical Decisions
Python 3.13+; In-memory storage only: list of dictionaries or simple Task class; No external dependencies (except possibly rich for better formatting — optional); No persistence (data resets on every program restart — intentional for Phase I)

### Development Process (Spec-Driven Development)
Use Spec-Kit Plus with Qwen model for code generation; Generate detailed specs first → plans → tasks → implementation; Preserve full specification history; Human review of every AI-generated code block mandatory; Aim for clean, production-ready quality even for hackathon MVP

### Success Criteria
All 5 core features must work perfectly; Application runs without crashes; Clean console output (readable even on small terminals); GitHub repository must contain: Constitution file, Specs history folder, /src folder with working code, Detailed README with setup & usage instructions

## Constraints & Non-Goals (Phase I)
No due dates, priorities, categories, tags; No search/filter functionality; No user accounts; No file save/load; No tests required (but structure should allow easy addition later)

## Feature Requirements
Build a minimal, clean, command-line todo list application that stores tasks only in memory (no file/database persistence); 1. Add new task (with title and description); 2. View all tasks (with ID, title, description, and completion status); 3. Update existing task details (title or description); 4. Delete task by ID; 5. Mark task as complete / incomplete (toggle status)

## Governance
Constitution supersedes all other practices; Amendments require documentation and approval; All development must verify compliance with these principles; Use Spec-Kit Plus for development guidance

**Version**: 1.0.0 | **Ratified**: 2025-01-01 | **Last Amended**: 2025-01-01