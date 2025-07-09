from .llm import MultiAgent
from ui_automation.ui_manager import *

agent = MultiAgent()
uia_manager = UIManager()

command = "Turn on the notifications"
session_id = "user_123"

ui_tree = uia_manager.get_ui_tree()

# Run the agent
result = agent.run_step(ui_tree, command, session_id)

print(result)