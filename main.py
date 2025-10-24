from llm import MultiAgent
from ui_automation.ui_manager import *
import json
from speech.stt import STT


from utils import *

# --- Global objects ---

obj1 = MultiAgent()
obj2 = UIManager()
obj3 = Utils()

id = obj3.time_id_ms()

config = {"configurable": {"thread_id": id}}
steps = []

def predict_action(query):

    ui_tree = obj2.get_ui_tree()
    print(ui_tree)

    output = obj1.get_solver_response(query, ui_tree, config)
    content = output.content
    print("LLM Response:", content)
    print("---"*40)

    element_data = json.loads(content)

    if element_data["found"] == "Yes":
        simulated = obj2.simulate(element_data)
        steps.append(element_data["title"])

        if simulated == 1:
            if element_data["complete"] == "No":
                predict_action(query)
        else:
            print("The program failed!!")
            return 0
    else:
        print("Did not find any relevant control element")

def on_transcript(transcript: str):

    tts = TTS()
    feedback = f"I heard: {transcript}"
    print(feedback)
    tts.speak(feedback)
    # tts.speak("Thinking......")
    predict_action(transcript)
    print(steps)


def main():

    # query = "Task: Change Margins to Narrow"
    # query = "Task: Change the font size to 10"
    # query = "Task: Add a new comment with text 'Check this section'"
    # query = "Task: Center the alignment for the text"
    # query = "Task: Change the mode to Reviewing"
    # query = "Task: Insert a table with 8 rows and 6 columns"

    # predict_action(query)
    # print(steps)

    stt = STT(on_transcript=on_transcript, model_name="small", device="cpu", compute_type="int8")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        stt.shutdown()

# if __name__ == "__main__":
#     main()

query = "Task: Insert summation symbol"

predict_action(query)
print(steps)