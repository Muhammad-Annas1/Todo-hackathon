# Data Model: Todo CLI App Enhancement

**Feature**: Todo CLI App Enhancement
**Date**: 2025-01-01
**Branch**: 001-todo-app-enhancement

## Overview

This document defines the data model for the enhanced Todo CLI application, including the updated Task entity and related components.

## Task Entity

The Task entity is enhanced to include priority, tags, and due date fields.

### Fields

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| id | int | Yes | Auto-generated | Unique identifier for the task |
| title | str | Yes | - | Title or brief description of the task |
| description | str | No | "" | Detailed description of the task |
| completed | bool | Yes | False | Whether the task is completed |
| priority | str | Yes | "medium" | Priority level: "high", "medium", or "low" |
| tags | list[str] | No | [] | List of tags associated with the task |
| due_date | str or None | No | None | Due date in YYYY-MM-DD format or None if not set |

### Validation Rules

1. **ID**: Must be a positive integer, auto-incremented from the highest existing ID
2. **Title**: Must not be empty or None
3. **Completed**: Must be a boolean value
4. **Priority**: Must be one of "high", "medium", or "low" (case-insensitive)
5. **Tags**: Must be a list of strings, each tag should be 1-30 characters, alphanumeric with hyphens/underscores
6. **Due Date**: If provided, must be in YYYY-MM-DD format or a valid date string that can be parsed

### Example

```python
task = {
    "id": 1,
    "title": "Implement priority feature",
    "description": "Add priority levels to tasks",
    "completed": False,
    "priority": "high",
    "tags": ["feature", "priority", "enhancement"],
    "due_date": "2025-01-15"
}
```

## Priority Enum

### Values

- "high": Highest priority, represented visually with "!!!" or similar indicator
- "medium": Medium priority, represented visually with "!!" or similar indicator
- "low": Low priority, represented visually with "!" or similar indicator

## Tag Entity

Tags are represented as strings within the Task entity. Each tag should follow these rules:

- Length: 1-30 characters
- Characters: Alphanumeric with hyphens and underscores allowed
- Case: Stored as lowercase for consistency in search/filter operations

## Filter Entity

Represents criteria for filtering tasks.

### Fields

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| status | str or None | No | None | Filter by status: "all", "pending", "completed" |
| priority | str or None | No | None | Filter by priority: "all", "high", "medium", "low" |
| tag | str or None | No | None | Filter by specific tag |

## Sort Entity

Represents criteria for sorting tasks.

### Fields

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| field | str | Yes | "id" | Sort by field: "priority", "due_date", "title", "id" |
| order | str | Yes | "asc" | Sort order: "asc" (ascending) or "desc" (descending) |

## State Transitions

### Task Completion
- `pending` → `completed` when task is marked as done
- `completed` → `pending` when task is marked as incomplete

### Priority Changes
- Priority can be changed from any level to any other level during update operations

## Relationships

- Each Task can have multiple Tags (one-to-many within the same entity)
- Each Task has one Priority (one-to-one)