# from ui_automation.ui_manager import UIManager
from utils import Utils
from speech.speech_to_text import *

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

def got_text(transcript: str):
    obj = Utils()
    print(transcript)
    obj.speak(transcript)

stt = STT(on_transcript=got_text, model_name="small", device="cpu", compute_type="int8")

try:
    import time
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    stt.shutdown()