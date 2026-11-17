# -*- coding: utf-8 -*-
import sys, json
from client import OpenClawGenParkProducer

producer = OpenClawGenParkProducer()

def run_tool(name, args):
    if name == "plan_multimodal_pipeline":
        reqs = args.get("asset_requests", [])
        return producer.plan_multimodal_pipeline(reqs)
    else:
        raise ValueError(f"Unknown tool: {name}")

from typing import Any, Dict, List, Optional

try:
    from mcp.server.fastmcp import FastMCP
except ImportError as exc:
    raise SystemExit("MCP requires the mcp package. Run: python -m pip install -r requirements.txt") from exc

mcp = FastMCP('openclaw-genpark-producer')

@mcp.tool()
def plan_multimodal_pipeline(asset_requests: Optional[List[Dict[str, Any]]] = None) -> str:
    """Plan dependencies for supplied media asset requests."""
    return json.dumps(run_tool('plan_multimodal_pipeline', {'asset_requests': asset_requests if asset_requests is not None else []}))

def main():
    if "--test" in sys.argv:
        print("[TEST] Running OpenClaw Producer Self-Test...")
        pipeline = [
            {"id": "text_draft", "cost": 5},
            {"id": "voice_gen", "depends_on": ["text_draft"], "cost": 15},
            {"id": "b_roll_gen", "depends_on": ["text_draft"], "cost": 30},
            {"id": "composite", "depends_on": ["voice_gen", "b_roll_gen"], "cost": 20}
        ]
        res = producer.plan_multimodal_pipeline(pipeline)
        assert res["has_deadlock_cycle"] is False
        assert len(res["execution_stages"]) == 3
        print("[TEST] All tests passed successfully!")
        return

    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
