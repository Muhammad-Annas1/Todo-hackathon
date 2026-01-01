# API Contracts: Todo CLI App Enhancement

**Feature**: Todo CLI App Enhancement
**Date**: 2025-01-01
**Branch**: 001-todo-app-enhancement

## Overview

This document defines the contract for the enhanced Todo CLI application commands, including new functionality for priority, tags, due dates, search, filter, and sort.

## Task Entity Schema

```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "integer",
      "description": "Unique identifier for the task",
      "minimum": 1
    },
    "title": {
      "type": "string",
      "description": "Title of the task",
      "minLength": 1
    },
    "description": {
      "type": "string",
      "description": "Detailed description of the task",
      "default": ""
    },
    "completed": {
      "type": "boolean",
      "description": "Whether the task is completed",
      "default": false
    },
    "priority": {
      "type": "string",
      "enum": ["high", "medium", "low"],
      "description": "Priority level of the task",
      "default": "medium"
    },
    "tags": {
      "type": "array",
      "items": {
        "type": "string",
        "pattern": "^[a-zA-Z0-9_-]{1,30}$"
      },
      "description": "List of tags associated with the task",
      "default": []
    },
    "due_date": {
      "type": ["string", "null"],
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$",
      "description": "Due date in YYYY-MM-DD format or null if not set"
    }
  },
  "required": ["id", "title", "completed", "priority"]
}
```

## CLI Commands

### 1. Add Task
- **Command**: `1` or `add`
- **Input**:
  - Title (required)
  - Description (optional)
  - Priority (optional, default: medium)
  - Tags (optional, space/comma separated)
  - Due date (optional, YYYY-MM-DD or natural language)
- **Output**: Success message with task ID
- **Error cases**: Invalid input formats

### 2. View Tasks
- **Command**: `2` or `view`
- **Input**: None
- **Output**: List of all tasks with enhanced information (priority, tags, due date)
- **Error cases**: None

### 3. Update Task
- **Command**: `3` or `update`
- **Input**:
  - Task ID (required)
  - New values for any field (optional, keeps old values if not provided)
- **Output**: Success message
- **Error cases**: Task ID not found

### 4. Delete Task
- **Command**: `4` or `delete`
- **Input**: Task ID
- **Output**: Success message
- **Error cases**: Task ID not found

### 5. Toggle Task Completion
- **Command**: `5` or `toggle`
- **Input**: Task ID
- **Output**: Success message
- **Error cases**: Task ID not found

### 6. Search Tasks
- **Command**: `6` or `search`
- **Input**: Search keyword
- **Output**: List of matching tasks
- **Error cases**: None

### 7. Filter Tasks
- **Command**: `7` or `filter`
- **Input**:
  - Status filter (optional: all, pending, completed)
  - Priority filter (optional: all, high, medium, low)
  - Tag filter (optional: specific tag)
- **Output**: List of filtered tasks
- **Error cases**: Invalid filter values

### 8. Sort Tasks
- **Command**: `8` or `sort`
- **Input**:
  - Sort field (optional: priority, due_date, title, id; default: id)
  - Sort order (optional: asc, desc; default: asc)
- **Output**: List of tasks in sorted order
- **Error cases**: Invalid sort parameters

## Date Input Formats

The system accepts the following date formats:
- Standard: YYYY-MM-DD (e.g., 2025-01-15)
- Natural language:
  - "today"
  - "tomorrow"
  - "yesterday"
  - "next [day of week]" (e.g., "next friday")
  - "in [number] days" (e.g., "in 3 days", "in 1 week")
  - "[number] [day/week/month] [ago/later]" (e.g., "3 days ago", "2 weeks later")

## Validation Rules

### Priority
- Must be one of: "high", "medium", "low"
- Case-insensitive
- Default: "medium"

### Tags
- Each tag must be 1-30 characters
- Only alphanumeric characters, hyphens, and underscores
- Multiple tags separated by spaces or commas
- Converted to lowercase for consistency

### Due Date
- If provided, must be a valid date
- Natural language dates are converted to YYYY-MM-DD format
- Invalid dates result in error message

## Error Responses

All commands return appropriate error messages for invalid inputs:
- "Invalid input: [description of issue]"
- "Task with ID [id] not found"
- "Invalid priority level. Use: high, medium, low"
- "Invalid date format"
- "Invalid filter option"
- "Invalid sort option"