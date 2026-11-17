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

## MCP runtime requirements

The standard-library-only policy applies to direct `client.py` use. Running `mcp_server.py` requires Python 3.10+ and the official `mcp` SDK (`mcp>=1.0.0,<2`) from `requirements.txt`. Install it into your chosen environment from the repository checkout:

```bash
python -m pip install -r requirements.txt
```

Configure the MCP client with that environment's absolute Python executable path and the absolute path to `mcp_server.py`. The client launches a local STDIO process; a GitHub URL is not a remote MCP endpoint.

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Openclaw Genpark Producer**.
Your primary directive is to execute: OpenClaw GenPark multimodal media task DAG producer with critical path makespan estimation and parallel stage orchestration.
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `{'name': 'plan_multimodal_pipeline', 'description': 'Compile multimodal asset creation jobs into dependency stages.'}`
- Use direct `client.py` execution when the environment requires standard-library-only algorithms; MCP execution also requires the SDK below.

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
- **Core-Client Dependency Policy**: Keep algorithms in `client.py` limited to the Python standard library (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`). This restriction does not apply to the MCP runtime, which uses the official SDK.
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.
