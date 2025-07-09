from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser


from .agents.solver.prompt import *
import os

class UIAction(BaseModel):
    action: str = Field(description="Action to perform, e.g., click, type, select")
    element_id: str = Field(description="The id of the element in the UI tree")

class MultiAgent:

    def __init__(self) -> None:

        # MODEL
        self.model = os.environ.get("MODEL")

        # Create JSON output parser for UIAction
        self.solver_json_parser = JsonOutputParser(pydantic_object=UIAction)

        #Initiate Solver LLM
        self.solver_llm = ChatOpenAI(model=self.model, temperature=0)

        # Create a prompt template
        self.solver_prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant that maps user commands to UI actions."),
            MessagesPlaceholder(variable_name="history"),
            ("user", "{ui_tree}\n\nQuestion: {command}\n\nRespond in JSON format:"),
            ("user", self.solver_json_parser.get_format_instructions())
        ])

        #Create a store to hold chat histories
        self.store = {}

    def get_session_history(self, session_id: str):
        if session_id not in self.store:
            self.store[session_id] = InMemoryChatMessageHistory()
        return self.store[session_id]


    def get_solver_response(self, ui_tree, command: str, session_id: str):
        
        chain = self.solver_prompt | self.solver_llm | self.solver_json_parser

        chat_chain = RunnableWithMessageHistory(
            chain,
            self.get_session_history,
            input_messages_key=["command", "ui_tree"],
            history_messages_key="history"
        )

        response = chat_chain.invoke(
            {"ui_tree": ui_tree, "command": command},
            config={"configurable": {"session_id": session_id}}
        )

        return response