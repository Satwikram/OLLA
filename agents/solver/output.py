output1="""
{{
  "found": "Yes",
  "control_type": "TabItem",
  "title": "Layout",
  "value": null,
  "rect": {{
    "left": 417,
    "top": 72,
    "right": 505,
    "bottom": 117
  }},
  "reason": "I can see the 'Layout' tab item in the provided UI tree, and its title exactly matches 'Layout'; it is a TabItem control, which is necessary for accessing margin settings. By selecting this tab, I can progress towards changing the margin settings. It is present in the tree.",
  "complete": "No"
}}
"""

output2="""
{{
  "found": "Yes",
  "control_type": "MenuItem",
  "title": "Margins",
  "value": null,
  "rect": {{
    "left": 30,
    "top": 123,
    "right": 102,
    "bottom": 237
  }},
  "reason": "I found the 'Margins' menu item in the provided UI tree; this title matches exactly what is needed for changing margin settings. It is a MenuItem control, appropriate for selecting options related to margins. The selection of this item is essential to proceed with changing the margin to narrow. It is present in the tree.",
  "complete": "No"
}}
"""

output3="""
{{
  "found": "Yes",
  "control_type": "ListItem",
  "title": "Narrow Margins",
  "value": null,
  "rect": {{
    "left": 32,
    "top": 353,
    "right": 423,
    "bottom": 467
  }},
  "reason": "The UI tree contains the 'Narrow Margins' list item, which directly corresponds to the user's request to change the margin to narrow. Its title exactly matches the required action and it is a ListItem control, which is suitable for selection options in this context. The element is present in the tree.",
  "complete": "Yes"
}}
"""