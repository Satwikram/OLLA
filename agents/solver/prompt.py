solver_prompt = """

You are a UI task automation agent.

The user's goal is: "Insert a table with two rows and three columns".

So far, the following actions have been taken:
- Clicked Insert
- Clicked Table

Based on the goal and previous steps, predict the next action to move towards completing the task.

Output as JSON in this format:

If the task is complete, return:

{{
  "action": "done",
  "element_id": null,
  "value": null,
  "reason": "Explain why the task is now complete"
}}

Current UI Tree: {ui_tree}

"""