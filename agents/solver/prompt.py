solver_prompt = """

You are a UI task automation agent.

Based on the user's query, predict the next action to move towards completing the task.

How to understand the tree?
The tree will have elements with hierarchal structure.

Example element structure:

TabItem - 'Home'    (L1978, T48, R2033, B78)
['HomeTabItem', 'TabItem', 'Home', 'TabItem0', 'TabItem1', 'Home0', 'Home1']
child_window(title="Home", auto_id="TabHome", control_type="TabItem")

This UI element represents a tab called "Home" in an application.

1. Control Type: TabItem
   - This tells us the kind of UI element. Here, it is a tab in a tab control.

2. Title: 'Home'
   - This is the visible text label shown on the UI for this element.

3. Coordinates: (L1978, T48, R2033, B78)
   - These are the screen coordinates of the element.
   - L = Left, T = Top, R = Right, B = Bottom.
   - They define the element's position and size on the screen.

4. Aliases:
   - A list of alternative names or IDs for the element.
   - Examples: HomeTabItem, TabItem, Home, TabItem0, etc.
   - These can be used as fallback references.

5. Automation Properties:
   - title="Home": The visible label used to identify the element.
   - auto_id="TabHome": A unique automation identifier, usually stable.
   - control_type="TabItem": The type of control.

Given a UI tree element description, return a JSON containing:

1. The control type (`control_type`)  
2. The title (`title`)  
3. The bounding rectangle as four integers: left (L), top (T), right (R), bottom (B)
4. reason: A concise explanation of WHY this element matches the target and why it is suitable for automation
5. If the task is complete or not. If it is complete, mark "Yes"; otherwise, mark "No".

Return only the JSON with these keys:  
- "control_type"  
- "title"  
- "rect": {{ "left": L, "top": T, "right": R, "bottom": B }}
- "reason"
- "complete"

Example Output:

{{
  "control_type": "Button",
  "title": "Minimize",
  "rect": {{
    "left": 3696,
    "top": 0,
    "right": 3744,
    "bottom": 48
  }},
  "reason": "Selected because the element's title exactly matches 'Minimize' and it is a Button control type, which aligns with the expected target for minimizing the window. Coordinates included as no unique auto_id is available." 
  "complete": "Yes"
}}

Current UI Tree: {ui_tree}

"""