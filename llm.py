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
