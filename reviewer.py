from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, BaseMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from typing import Sequence
from langgraph.graph.message import add_messages
from typing_extensions import Annotated, TypedDict

import os
from agents.reviewer.prompt import *
from ui_automation.ui_manager import *

from dotenv import load_dotenv
load_dotenv()


class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    ui_tree: str
    solver_response: str

class ReviewAgent:

    def __init__(self):

        self.model_name = os.environ.get("MODEL")
        
        self.reviewer_llm = init_chat_model(self.model_name, model_provider="openai")

        # Define a new state graph
        self.workflow = StateGraph(state_schema=State)

        # Define the (single) node in the graph
        self.workflow.add_edge(START, "model")
        self.workflow.add_node("model", self.call_model)

        # Add memory
        memory = MemorySaver()
        self.app = self.workflow.compile(checkpointer=memory)

        self.prompt_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                reviewer_prompt,
            ),
            MessagesPlaceholder(variable_name="messages"),
        ])


    # Define the function that calls the model
    def call_model(self, state: State):
        prompt = self.prompt_template.invoke(state)
        response = self.reviewer_llm.invoke(prompt)
        return {"messages": [response]}
    
    def get_reviewer_response(self, solver_response, ui_tree, config):

        input_messages = [HumanMessage(solver_response)]
        output = self.app.invoke({"messages": input_messages, "ui_tree": ui_tree}, config)

        return output["messages"][-1] # output contains all messages in state