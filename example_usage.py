# -*- coding: utf-8 -*-
from client import OpenClawGenParkProducer

def main():
    producer = OpenClawGenParkProducer()
    print("=== OpenClaw GenPark Multimodal Pipeline Producer ===")

    # Define multimodal ad production workflow
    workflow = [
        {"id": "copywriting", "cost": 8.0},
        {"id": "voiceover_synthesis", "depends_on": ["copywriting"], "cost": 12.0},
        {"id": "product_3d_render", "depends_on": ["copywriting"], "cost": 45.0},
        {"id": "video_composer", "depends_on": ["voiceover_synthesis", "product_3d_render"], "cost": 20.0}
    ]

    plan = producer.plan_multimodal_pipeline(workflow)
    print(f"Total Tasks: {plan['total_tasks']}, Stages: {len(plan['execution_stages'])}")
    print(f"Estimated Critical Path Makespan: {plan['estimated_makespan_seconds']}s")
    for idx, stage in enumerate(plan["execution_stages"], 1):
        print(f"  Stage {idx}: {stage}")

if __name__ == "__main__":
    main()
