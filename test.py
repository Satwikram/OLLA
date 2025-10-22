# from ui_automation.ui_manager import UIManager

# obj = UIManager()
# # element_data = {

# #     "title": "Aptos (Body)",
# #     "control_type": "Edit",
# # }
# # obj.simulate(element_data)

# obj.get_screenshot()

# tree = obj.get_ui_tree()

# with open("ui_tree.txt", "w+", encoding="utf-8") as f:
#     f.write(tree)

from pynput import keyboard

def on_press(key):
    print("press:", key, "vk:", getattr(key, "vk", None), "name:", getattr(key, "name", None))

def on_release(key):
    print("release:", key, "vk:", getattr(key, "vk", None))
    if key == keyboard.Key.esc:
        return False

print("Press F9 (or Fn+F9 on some laptops). Press ESC to quit.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
