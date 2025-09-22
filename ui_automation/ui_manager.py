import pygetwindow as gw
from pywinauto.application import Application
from io import StringIO
from contextlib import redirect_stdout
import pyttsx3
from utils import *

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

        output = StringIO()

        with redirect_stdout(output):
            dialog.print_control_identifiers()

        ui_tree = output.getvalue()

        return ui_tree
    
    def simulate(self, element_data):

        """
        Simulates a click on the element specified in element_data.
        """
        try:
            element = self.window.child_window(
                control_type=element_data["control_type"],
                title=element_data["title"]
            )

            element.wait('exists', timeout=5)

            self.util.speak(f"Prediction -- {element_data['title']} -- {element_data['reason']}")
            self.util.speak(f"Verified -- the {element_data['title']} element is present, clicking on it now.")

            element.click_input()
            print(f"Clicked on element using control_type='{element_data['control_type']}' and title='{element_data['title']}'.")

            return 1

        except Exception as e:
            print("Error:", e)
            return 0

# obj = UIManager()
# element_data = {

#     "title": "Review",
#     "control_type": "Button",
# }
# obj.simulate(element_data)