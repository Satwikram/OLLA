from ui_automation.ui_manager import *


obj = UIManager()

element = {
    
    "title": "Aptos (Body)",
    "control_type": "Edit",
}

property = obj.get_control_properties(element)
print(property)