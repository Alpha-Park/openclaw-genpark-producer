---
name: openclaw-genpark-producer
description: OpenClaw GenPark multimodal media task DAG producer with critical path makespan estimation and parallel stage orchestration.
category: Service
version: 1.0.0
license: MIT
tools:
  - {'name': 'plan_multimodal_pipeline', 'description': 'Compile multimodal asset creation jobs into dependency stages.'}
---

# Openclaw Genpark Producer

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Openclaw Genpark Producer**.
Your primary directive is to execute: OpenClaw GenPark multimodal media task DAG producer with critical path makespan estimation and parallel stage orchestration.
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `{'name': 'plan_multimodal_pipeline', 'description': 'Compile multimodal asset creation jobs into dependency stages.'}`
- Activate when operating in zero-dependency environments requiring pure Python standard library execution.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import *

# Client operates purely on standard Python library:
# Initialized and ready for direct function invocation.
```

### Option 2: FastMCP Tool Calling
Tools registered in `mcp_server.py`:
- `{'name': 'plan_multimodal_pipeline', 'description': 'Compile multimodal asset creation jobs into dependency stages.'}`

## Core Mathematical & Algorithmic Guardrails
- **Zero-Dependency Policy**: 100% Python standard library only (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`).
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.
