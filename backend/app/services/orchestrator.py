from app.agents.planner import PlannerAgent
from app.agents.workers import ResearcherAgent, WriterAgent
from app.schemas.planner import Plan, TaskResult

class Orchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.researcher = ResearcherAgent()
        self.writer = WriterAgent()

    def run_workflow(self, user_prompt: str):
        # 1. Generate the plan
        plan = self.planner.create_plan(user_prompt)
        results = []
        context = ""

        # 2. Execute tasks sequentially
        for task in plan.tasks:
            if task.assigned_agent == "researcher":
                result = self.researcher.execute(task)
            else:
                result = self.writer.execute(task, context=context)
            
            results.append(result)
            # Update context for the next agent
            context += f"\n{result.output}"

        return {"plan": plan, "results": results}