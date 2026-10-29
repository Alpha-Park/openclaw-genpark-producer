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

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            res = run_tool(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"jsonrpc": "2.0", "id": req.get("id"), "result": res}))
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}}))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
