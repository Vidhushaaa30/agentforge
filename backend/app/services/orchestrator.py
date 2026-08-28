import time
from app.agents.planner import PlannerAgent
from app.agents.workers import ResearcherAgent, WriterAgent
from app.services.history_service import history_service
from app.services.metrics_service import metrics_service
from app.services.summary_service import summary_service
from app.services.task_filter import task_filter_service
from app.core.logger import logger

class Orchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.researcher = ResearcherAgent()
        self.writer = WriterAgent()

    def run_workflow(self, user_prompt: str, max_tasks: int = 5):
        logger.info(f"Starting workflow execution for prompt: '{user_prompt[:30]}...'")
        start_time = time.time()
        
        plan = self.planner.create_plan(user_prompt)
        plan.tasks = task_filter_service.limit_tasks(plan.tasks, max_tasks)
        logger.info(f"Plan generated with {len(plan.tasks)} task(s)")

        results = []
        context = ""

        for task in plan.tasks:
            logger.info(f"Executing task {task.id} with agent '{task.assigned_agent}'")
            if task.assigned_agent == "researcher":
                result = self.researcher.execute(task)
            else:
                result = self.writer.execute(task, context=context)
            
            results.append(result)
            context += f"\n--- Context from Task {task.id} ({task.title}) ---\n{result.output}\n"

        elapsed_time = time.time() - start_time
        dumped_results = [r.model_dump() for r in results]
        
        metrics = metrics_service.calculate_metrics(dumped_results, elapsed_time)
        summary = summary_service.generate_summary(dumped_results)

        log = history_service.save_log(
            prompt=user_prompt, 
            results=dumped_results
        )

        logger.info(f"Workflow completed successfully in {round(elapsed_time, 2)} seconds")

        return {
            "execution_id": log.id,
            "summary": summary,
            "plan": plan,
            "results": results,
            "metrics": metrics
        }