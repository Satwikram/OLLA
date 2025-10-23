# from ui_automation.ui_manager import UIManager
from utils import Utils
from speech.stt import *
from speech.tts import *

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

def test():
    while True:
        a = 10
        b = 20
        print(a + b)
        time.sleep(5)

def got_text(transcript: str):
    obj = TTS()
    print(transcript)
    obj.speak(transcript)
    test()

stt = STT(on_transcript=got_text, model_name="small", device="cpu", compute_type="int8")

try:
    import time
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    stt.shutdown()

# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty("voices")
# for i, v in enumerate(voices):
#     print(i, "| id:", v.id, "| name:", v.name)
