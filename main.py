from llm import MultiAgent
from ui_automation.ui_manager import *

agent = MultiAgent()
uia_manager = UIManager()

command = "Click on Insert"
session_id = "user_123"

ui_tree = uia_manager.get_ui_tree()
print(type(ui_tree))

# Run the agent
result = agent.get_solver_response(ui_tree, command, session_id)

print(result)