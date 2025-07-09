agent = StatefulUIAgent()

# Example UI tree and command
ui_tree = [
    {"id": "switch_notifications", "type": "toggle", "label": "Notifications"},
    {"id": "btn_save", "type": "button", "text": "Save"}
]

command = "Turn on the notifications"
session_id = "user_123"

# Run the agent
result = agent.run_step(ui_tree, command, session_id)

print(result)
