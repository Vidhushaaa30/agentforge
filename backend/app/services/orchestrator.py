from app.agents.planner import PlannerAgent
from app.agents.workers import ResearcherAgent, WriterAgent

class Orchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.researcher = ResearcherAgent()
        self.writer = WriterAgent()

    def run_workflow(self, user_prompt: str):
        plan = self.planner.create_plan(user_prompt)
        results = []
        context = ""

        for task in plan.tasks:
            if task.assigned_agent == "researcher":
                result = self.researcher.execute(task)
            else:
                result = self.writer.execute(task, context=context)
            
            results.append(result)
            context += f"\n--- Context from Task {task.id} ({task.title}) ---\n{result.output}\n"

        return {"plan": plan, "results": results}