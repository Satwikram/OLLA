from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

import os

class MultiAgent:

    def __init__(self):

        self.model_name = os.environ.get("MODEL")
        
        self.solver_llm = init_chat_model(self.model_name, model_provider="openai")

        # Define a new state graph
        self.workflow = StateGraph(state_schema=MessagesState)

        # Define the (single) node in the graph
        self.workflow.add_edge(START, "model")
        self.workflow.add_node("model", self.call_model)

        # Add memory
        memory = MemorySaver()
        self.app = self.workflow.compile(checkpointer=memory)

    # Define the function that calls the model
    def call_model(self, state: MessagesState):
        response = self.solver_llm.invoke(state["messages"])
        return {"messages": response}
    
    def get_solver_response(self, query, config):

        input_messages = [HumanMessage(query)]
        output = self.app.invoke({"messages": input_messages}, config)
        
        return output["messages"][-1] # output contains all messages in state


obj = MultiAgent()
config = {"configurable": {"thread_id": "abc123"}}
query = "My name is Satwik"

output = obj.get_solver_response(query, config)
print("LLM Response:", output.content)

query = "Do you know my name?"
output = obj.get_solver_response(query, config)
print("LLM Response:", output.content)

