# Implementation Plan: Advanced Todo CLI App with Recurring Tasks and Time-based Reminders

**Branch**: `002-recurring-tasks-reminders` | **Date**: 2026-01-01 | **Spec**: specs/002-recurring-tasks-reminders/spec.md
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan outlines the implementation of recurring tasks and time-based reminders for the existing in-memory Python console todo app. The feature will add due date/time support, recurrence patterns (daily, weekly, monthly, yearly), auto-scheduling of recurring tasks, and visual indicators for overdue and upcoming tasks. The implementation will maintain all existing functionality while adding these advanced features.

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Python 3.13+
**Primary Dependencies**: datetime module, dateutil (for parsing flexible dates), rich (for visual indicators)
**Storage**: In-memory only (list of dictionaries or Task class instances)
**Testing**: Manual testing based on acceptance scenarios
**Target Platform**: Cross-platform console application
**Project Type**: Single project CLI application
**Performance Goals**: Responsive UI with up to 50 tasks, <100ms response time for operations
**Constraints**: <100MB memory usage, no blocking operations, maintain existing functionality
**Scale/Scope**: Single user, console-based, up to 50 tasks

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ✅ Code Quality: Will follow PEP 8, use type hints, and maintain readable code
- ✅ Project Structure: Will use existing src/ directory structure
- ✅ User Experience: Will maintain existing CLI interface with enhanced visual indicators
- ✅ Technical Decisions: Will use Python 3.13+, in-memory storage, and optional rich dependency
- ✅ Development Process: Following Spec-Driven Development with detailed plan first
- ❌ Constraints & Non-Goals: Constitution states "No due dates" and "No search/filter functionality" but this feature explicitly requires due dates - this is a VIOLATION that needs to be addressed in the complexity tracking section

## Project Structure

### Documentation (this feature)

```text
specs/002-recurring-tasks-reminders/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── models/
│   └── task.py          # Task model with due date and recurrence fields
├── services/
│   ├── date_parser.py   # Flexible date/time parsing service
│   ├── recurrence.py    # Recurrence calculation service
│   └── reminder.py      # Reminder/overdue awareness service
├── cli/
│   └── todo_app.py      # Main CLI application with enhanced menu
└── lib/
    └── utils.py         # Utility functions
```

**Structure Decision**: Single project structure selected to maintain consistency with existing codebase and simplicity of deployment.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Constitution constraint "No due dates" | Advanced feature requires due dates for recurring tasks and reminders | Basic todo app doesn't meet user requirements for advanced task management |
| Constitution constraint "No search/filter" | Feature requires filtering for overdue and upcoming tasks | Visual indicators for time-based awareness are essential to the feature |
