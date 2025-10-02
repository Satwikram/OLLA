from ui_automation.ui_manager import *


# obj = UIManager()

element = {
    
    "title": "12",
    "control_type": "Edit",
    "value": 14.5,
}


# print(obj.get_ui_tree())

# property = obj.get_control_properties(element)
# print(property)

# obj.simulate(element)


import pygetwindow as gw
from pywinauto.application import Application
from io import StringIO
from contextlib import redirect_stdout
import pyttsx3
from utils import *
from pywinauto.uia_defines import IUIA  
from pywinauto.controls.uiawrapper import UIAWrapper


class UIManager:

    def __init__(self):

        self.util = Utils()

        self.active_window = gw.getActiveWindow()
        self.app = Application(backend="uia").connect(title=self.active_window.title, visible_only=False)
        self.window = self.app.window(title=self.active_window.title)

    def get_ui_tree(self):
        """
        Retrieves the UI tree of the currently active window.
        """
        dialog = self.app.top_window()  
        dialog.set_focus()
        print(dir(dialog))

        output = StringIO()

        with redirect_stdout(output):
            dialog.print_control_identifiers()

        ui_tree = output.getvalue()

        return ui_tree
    
obj = UIManager()
obj.get_ui_tree()