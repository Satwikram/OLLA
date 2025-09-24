from ui_automation.ui_manager import *


obj = UIManager()

element = {
    
    "title": "12",
    "control_type": "Edit",
    "value": 14.5,
}

# print(obj.get_ui_tree())

# property = obj.get_control_properties(element)
# print(property)

obj.simulate(element)