from app.agents.base import BaseAgent

class TaskPlannerAgent(BaseAgent):
    def run(self, goal: str):
        return {
            "agent": "1. Task Planner Agent",
            "status": "Completed",
            "sub_traces": [f"Deconstruct objective: {goal}", "Identify core modules", "Define deliverables"]
        }