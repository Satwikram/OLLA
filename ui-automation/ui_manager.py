import pygetwindow as gw
from pywinauto.application import Application
from io import StringIO
from contextlib import redirect_stdout

class UIManager:

    def __init__(self):

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