import time
from app.agents.planner import PlannerAgent
from app.agents.workers import ResearcherAgent, WriterAgent
from app.services.history_service import history_service
from app.services.metrics_service import metrics_service

class Orchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.researcher = ResearcherAgent()
        self.writer = WriterAgent()

    def run_workflow(self, user_prompt: str):
        start_time = time.time()
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

        elapsed_time = time.time() - start_time
        dumped_results = [r.model_dump() for r in results]
        metrics = metrics_service.calculate_metrics(dumped_results, elapsed_time)

        log = history_service.save_log(
            prompt=user_prompt, 
            results=dumped_results
        )

        return {
            "execution_id": log.id,
            "plan": plan,
            "results": results,
            "metrics": metrics
        }