from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, BaseMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from typing import Sequence
from langgraph.graph.message import add_messages
from typing_extensions import Annotated, TypedDict

import os
from agents.solver.prompt import *
from ui_automation.ui_manager import *

import json

class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    ui_tree: str

class MultiAgent:

    def __init__(self):

        self.model_name = os.environ.get("MODEL")
        
        self.solver_llm = init_chat_model(self.model_name, model_provider="openai")

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
                solver_prompt,
            ),
            MessagesPlaceholder(variable_name="messages"),
        ])


    # Define the function that calls the model
    def call_model(self, state: State):
        prompt = self.prompt_template.invoke(state)
        response = self.solver_llm.invoke(prompt)
        return {"messages": [response]}
    
    def get_solver_response(self, query, ui_tree, config):

        input_messages = [HumanMessage(query)]
        output = self.app.invoke({"messages": input_messages, "ui_tree": ui_tree}, config)

        return output["messages"][-1] # output contains all messages in state


obj1 = MultiAgent()
obj2 = UIManager()


ui_tree = obj2.get_ui_tree()

config = {"configurable": {"thread_id": "abc123"}}
query = "Task: Change Margins to Narrow"

output = obj1.get_solver_response(query, ui_tree, config)
print("LLM Response:", output.content, type(output.content))
print("---"*40)

element_data = json.loads(output.content)

obj2.simulate(element_data)
title = element_data["title"]
print(f"Clicked: {title}") 
print("---"*40)

while element_data["complete"] == "Yes":

    output = obj1.get_solver_response(query, ui_tree, config)
    print("LLM Response:", output.content, type(output.content))
    print("---"*40)

    obj2.simulate(element_data)
    title = element_data["title"]
    print(f"Clicked: {title}")
    print("---"*40)