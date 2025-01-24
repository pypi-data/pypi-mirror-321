# Code Assist MCP Server Implementation Plan

## Project Setup
- [x] Basic file structure
- [x] pyproject.toml with dependencies
- [x] Dockerfile with UV support
- [x] README.md with usage instructions
- [x] LICENSE file (MIT)
- [x] Source package structure
- [x] __main__.py and __init__.py
- [x] Tools module structure

## Core Components Implementation
- [x] XML Parser
  - [x] Add XML schema validation
  - [x] Implement parse/generate methods
  - [x] Add tests

- [x] File Tools
  - [x] create function
  - [x] delete function  
  - [x] modify with search/replace
  - [x] rewrite function
  - [x] diff generation
  - [x] directory tree with gitignore
  - [x] file search
  - [x] file operations tests

- [x] Git Operations
  - [x] Repository tools implementation
  - [x] GitPython integration
  - [x] Status/Diff/Log operations
  - [x] Add/Commit operations
  - [x] Branch operations
  - [x] Tests for git operations

- [ ] Server
  - [ ] OpenRouter integration
  - [ ] Command line interface
  - [ ] XML instruction processing
  - [x] Basic request handlers
  - [x] Error handling
  - [x] Request validation
  - [x] Tests for file operations

## Testing Infrastructure  
- [x] Unit test suite setup
- [x] Integration test cases
- [x] Fixtures and test data
- [x] GitPython test fixtures

## Documentation
- [ ] API documentation
- [ ] Example XML files
- [ ] Configuration examples
- [x] Git operations guide

## System Design Challenges

### Context Length Limitation
Problem: LLMs have limited context length ("memory"). Multiple file changes or complex refactoring can exceed this limit.

Proposed Solutions:
- Make operations idempotent (retryable without side effects)
- Break large changes into atomic, self-contained operations
- Use git commits as checkpoints
- Store intermediate state in temporary files
- Design instruction format to be resumable

## Current Task
Phase 1: Read-only operations
- File read operations complete
- Git read operations complete
- File write operations to be implemented directly

Phase 2:
- OpenRouter integration

Phase 3: Write operations
- For git write operations (add, commit, reset, branch, checkout), Claude provides commands to user by making an API call to openrouter.


## Notes
- XML format for instructions defined and documented
- Using Python 3.12 with UV package manager
- Following MCP server patterns from git implementation
- Local development setup complete with tests
- GitPython used for repository operations