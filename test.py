from ui_automation.ui_manager import UIManager

obj = UIManager()
# element_data = {

#     "title": "Aptos (Body)",
#     "control_type": "Edit",
# }
# obj.simulate(element_data)

obj.get_screenshot()

tree = obj.get_ui_tree()

with open("ui_tree.txt", "w+", encoding="utf-8") as f:
    f.write(tree)