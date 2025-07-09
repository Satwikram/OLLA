from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

from .agents.solver.prompt import *
import os

class MultiAgent:

    def __init__(self) -> None:

        # MODEL
        self.model = os.environ.get("MODEL")

        self.solver_prompt = solver_prompt
        self.solver_json_schema = None

        #Initiate Solver LLM
        self.solver_llm = ChatOpenAI(model=self.model, temperature=0)
        self.solver_llm.with_structured_output(self.solver_json_schema)

    def get_solver_response(self, ui_tree, command=None):

        
        

