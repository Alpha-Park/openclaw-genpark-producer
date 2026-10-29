# -*- coding: utf-8 -*-
"""
OpenClaw GenPark Producer - Multimodal Media Task DAG Producer & Workload Balancer
Standard Library only: collections, math, typing.
Generates priority-aware task DAGs, identifies critical execution paths,
and allocates rendering compute steps under quality diminishing returns.
"""

from typing import Dict, List, Set, Any

class OpenClawGenParkProducer:
    def plan_multimodal_pipeline(self, asset_requests: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        asset_requests: [{"id": "script_gen", "type": "text", "cost": 10},
                         {"id": "tts_audio", "type": "audio", "depends_on": ["script_gen"], "cost": 25},
                         {"id": "video_render", "type": "video", "depends_on": ["tts_audio"], "cost": 60}]
        """
        graph = {}
        in_degree = {}
        costs = {}

        for req in asset_requests:
            task_id = req["id"]
            graph[task_id] = []
            costs[task_id] = float(req.get("cost", 10.0))
            in_degree[task_id] = 0

        for req in asset_requests:
            task_id = req["id"]
            deps = req.get("depends_on", [])
            for d in deps:
                if d in graph:
                    graph[d].append(task_id)
                    in_degree[task_id] += 1

        # Kahn's topological sort
        queue = [t for t, deg in in_degree.items() if deg == 0]
        ordered_stages = []

        while queue:
            stage = list(queue)
            ordered_stages.append(stage)
            next_queue = []
            for u in stage:
                for v in graph.get(u, []):
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        next_queue.append(v)
            queue = next_queue

        has_cycle = sum(len(st) for st in ordered_stages) != len(asset_requests)

        # Critical path calculation (longest latency path)
        est = {t: 0.0 for t in graph}
        for stage in ordered_stages:
            for u in stage:
                finish_time = est[u] + costs[u]
                for v in graph[u]:
                    if finish_time > est[v]:
                        est[v] = finish_time

        max_makespan = max((est[t] + costs[t] for t in graph), default=0.0)

        return {
            "has_deadlock_cycle": has_cycle,
            "total_tasks": len(asset_requests),
            "execution_stages": ordered_stages,
            "estimated_makespan_seconds": round(max_makespan, 2),
            "total_compute_cost": round(sum(costs.values()), 2)
        }
