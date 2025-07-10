from llm import MultiAgent
from ui_automation.ui_manager import *
import json

obj1 = MultiAgent()
obj2 = UIManager()

config = {"configurable": {"thread_id": "abc123"}}
steps = []

def predict_action(query):

    ui_tree = obj2.get_ui_tree()

    output = obj1.get_solver_response(query, ui_tree, config)
    content = output.content
    print("LLM Response:", content)
    print("---"*40)

    element_data = json.loads(content)

    obj2.simulate(element_data)
    steps.append(element_data["title"])

    if element_data["complete"] == "No":
        predict_action(query)

# query = "Task: Change Margins to Narrow"
query = "Task: Add a new comment"

# predicted_action = predict_action(query, ui_tree)

predict_action(query)
print(steps)
