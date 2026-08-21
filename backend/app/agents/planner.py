from app.core.config import get_llm
from app.schemas.planner import Plan
from langchain_core.prompts import ChatPromptTemplate

class PlannerAgent:
    def __init__(self):
        self.llm = get_llm()

    def create_plan(self, prompt: str) -> Plan:
        structured_llm = self.llm.with_structured_output(Plan)
        
        system_prompt = (
            "You are an expert project planner. Break down the user's request into "
            "sequential tasks. Assign tasks to either 'researcher' or 'writer'."
        )
        
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{user_prompt}")
        ])
        
        chain = prompt_template | structured_llm
        return chain.invoke({"user_prompt": prompt})