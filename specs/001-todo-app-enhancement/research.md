# Research: Todo CLI App Enhancement

**Feature**: Todo CLI App Enhancement
**Date**: 2025-01-01
**Branch**: 001-todo-app-enhancement

## Overview

This research document outlines the key decisions and technical considerations for enhancing the Todo CLI app with priority levels, tags, due dates, search, filter, and sort functionality.

## Decision: Data Model Enhancement
**Rationale**: The existing Task model needs to be extended to support new features. Based on the feature requirements, we need to add priority, tags, and due date fields to the Task entity.

**Alternatives considered**:
1. Separate entities for each new feature - rejected as it would overcomplicate the data model
2. Store all new data as a single metadata field - rejected as it would make filtering and sorting difficult
3. Extend the existing Task entity with new fields - chosen as it maintains simplicity while enabling required functionality

## Decision: Date Parsing Library
**Rationale**: For flexible date input (natural language like "tomorrow", "next friday"), we need a library that can parse these formats. The `dateutil.parser` library is a good choice, but for more natural language parsing, we might consider `parsedatetime` or implement a custom solution.

**Alternatives considered**:
1. Use `dateutil.parser` - good for standard formats but limited for natural language
2. Use `parsedatetime` - better for natural language but adds a dependency
3. Implement custom parsing for common phrases - maintains minimal dependencies
4. Use `moment.js` equivalent in Python - no direct equivalent available

**Chosen approach**: Implement custom parsing for common phrases like "tomorrow", "next friday", "in 3 days" using Python's `datetime` module, with fallback to standard date parsing for YYYY-MM-DD format.

## Decision: Storage Implementation
**Rationale**: The constitution specifies in-memory storage only, so we'll extend the existing in-memory implementation rather than introducing a database.

**Alternatives considered**:
1. Keep existing list of dictionaries approach - simple but less structured
2. Use dataclasses for better structure and type hints - chosen for better maintainability
3. Use Pydantic models - would add dependencies, not needed for this phase

## Decision: UI Enhancement
**Rationale**: The existing UI needs to display additional information (priority, tags, due dates) in a readable format.

**Alternatives considered**:
1. Extend the existing table format with additional columns - chosen as it maintains consistency
2. Use the `rich` library for enhanced formatting - considered but optional per constitution
3. Create a completely new UI format - rejected as it would break user familiarity

## Decision: Search Implementation
**Rationale**: Need to implement search functionality across title, description, and tags fields.

**Alternatives considered**:
1. Simple substring matching - simple but less flexible
2. Regular expressions - more powerful but potentially slower
3. Case-insensitive search with word boundaries - chosen for good balance of functionality and performance

## Decision: Filter and Sort Implementation
**Rationale**: Need to implement filtering and sorting capabilities based on multiple criteria.

**Alternatives considered**:
1. Separate functions for each filter/sort type - clear but creates many functions
2. Single function with parameters for different behaviors - more flexible and maintainable
3. Use Python's built-in `filter()` and `sorted()` functions with custom key functions - chosen for leveraging Python's built-in capabilities

## Technology Stack
- Python 3.13+ (as per constitution)
- Standard library only (to maintain minimal dependencies as per constitution)
- Optional: `rich` library for enhanced formatting (as per constitution)