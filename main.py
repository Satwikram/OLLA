from llm import MultiAgent
from ui_automation.ui_manager import *
import json

from utils import *

obj1 = MultiAgent()
obj2 = UIManager()
obj3 = Utils()

id = obj3.time_id_ms()

config = {"configurable": {"thread_id": id}}
steps = []

def predict_action(query):

    ui_tree = obj2.get_ui_tree()

    output = obj1.get_solver_response(query, ui_tree, config)
    content = output.content
    print("LLM Response:", content)
    print("---"*40)

    element_data = json.loads(content)

    if element_data["found"] == "Yes":
        simulated = obj2.simulate(element_data)
        steps.append(element_data["title"])

        if simulated == 1:
            if element_data["complete"] == "No":
                predict_action(query)
        else:
            print("The program failed!!")
            return 0
    else:
        print("Did not find any relevant control element")

# query = "Task: Change Margins to Narrow"
query = "Task: Change the font size to 14.5"
# query = "Task: Add a new comment with text 'Check this section'"
# query = "Task: Center the alignment for the text"
# query = "Task: Change the mode to Reviewing"

predict_action(query)
print(steps)