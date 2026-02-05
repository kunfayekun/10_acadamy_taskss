# Tooling Strategy — Project Chimera

## Purpose
This document defines the **developer-facing tools** used to build, maintain, and reason about Project Chimera.

These tools are not runtime agent skills.  
They are **MCP (Model Context Protocol) servers** that assist the human developer and IDE-based AI agents.

---

## Selected MCP Servers

### 1. git-mcp
**Purpose:**  
Assist with version control, commit hygiene, diffs, and repository reasoning.

**Capabilities:**
- Read git status
- Review diffs
- Suggest commit messages
- Trace changes to specifications

**Why Needed:**
- Ensures traceability between specs and code
- Prevents undocumented changes

---

### 2. filesystem-mcp
**Purpose:**  
Allow structured reading and editing of project files.

**Capabilities:**
- Read directory trees
- Open and edit files
- Create new files following project conventions

**Why Needed:**
- Enables spec-driven development
- Prevents hallucinated file paths or structures

---

### 3. search-mcp (optional)
**Purpose:**  
Search within the codebase and documentation.

**Capabilities:**
- Keyword and symbol search
- Cross-file reference discovery

**Why Needed:**
- Helps agents understand existing context before changes

---

## Tooling Rules
- MCP tools must be read-first, write-second
- No file modifications without referencing specs
- All tooling actions must preserve traceability
