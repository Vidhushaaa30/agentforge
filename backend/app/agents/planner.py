from app.schemas.planner import Plan, Task

class PlannerAgent:
    def __init__(self):
        pass

    def create_plan(self, prompt: str) -> Plan:
        tasks = [
            Task(
                id=1,
                title="Research",
                description=f"Research key details for: {prompt}",
                assigned_agent="researcher"
            ),
            Task(
                id=2,
                title="Write Report",
                description=f"Write a comprehensive report based on research for: {prompt}",
                assigned_agent="writer"
            )
        ]
        return Plan(user_prompt=prompt, tasks=tasks)