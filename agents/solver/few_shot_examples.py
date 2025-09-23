from .ui_tree import *
from .output import *


examples = f"""

Task 1: Change the margin to narrow.

Turn 1:
{{{{

current view: {ui_tree1}

Thought: The user has mentioned that the task is to change the margin to narrow. By analyzing the UI tree, I need to find an element that allows changing the margin settings. There is no direct element for changing margins, but I can see a TabItem named 'Layout', which likely contains margin settings. Selecting this should help me progress toward the goal.

Output: {output1} 
}}}}
---------------------------------------------------------------------------------------
Turn 2:
{{{{

current view: {ui_tree2}

Thought: By referencing the chat history in the thread, I can see that the intended task user had given is to change the margin to narrow. In the previous step, I selected the TabItem named 'Layout'. This means, the task is not yet complete. The UI tree of the current window has changed. Now, I need to find a setting from the updated UI tree that lets me change the margins to narrow. In the UI tree, I can see a MenuItem named 'Margins,' which might contain the margin settings. I will select this control element since I think this would be the right control element to proceed towards completion of the task.

Output: {output2}
}}}}
---------------------------------------------------------------------------------------
Turn 3:
{{{{

current view: {ui_tree3}

Thought: By referencing the chat history in the thread, I can see that the intended task user had given is to change the margin to narrow. In the previous step, I selected the MenuItem named 'Margins'. The UI tree of the current window has changed. Now, I need to find the specific option to change the margin to narrow. I can see a ListItem named 'Narrow Margins,' which closely aligns with the task. I think this is the right element to complete the task given by the user.

Output: {output3}
}}}}
"""