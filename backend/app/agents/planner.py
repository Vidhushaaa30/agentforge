from app.schemas.planner import Plan, Task

class PlannerAgent:
    def create_plan(self, prompt: str) -> Plan:
        # Mocking task breakdown for now (we'll wire up LLM calls later)
        tasks = [
            Task(
                id=1,
                title="Research Topic",
                description=f"Gather core context and insights for: {prompt}",
                assigned_agent="researcher"
            ),
            Task(
                id=2,
                title="Draft Content",
                description=f"Create a initial draft based on research for: {prompt}",
                assigned_agent="writer"
            )
        ]
        
        return Plan(user_prompt=prompt, tasks=tasks)