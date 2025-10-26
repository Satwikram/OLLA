from llm import MultiAgent
from ui_automation.ui_manager import *
import json
from speech.stt import STT
import time, queue, threading, os, tempfile, logging
from package.tray import start_tray_in_thread

from utils import *
from dotenv import load_dotenv
load_dotenv()

LOG_PATH = os.path.join(tempfile.gettempdir(), "olla.log")
logging.basicConfig(filename=LOG_PATH, level=logging.INFO, format="%(asctime)s %(message)s")

inbox: "queue.Queue[str]" = queue.Queue()
busy_event = threading.Event()

# --- Global objects ---

obj1 = MultiAgent()
obj2 = UIManager()
obj3 = Utils()
speech_model = os.environ.get("SPEECH_MODEL")

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

    query = f"Task: {transcript}"
    # tts.speak("Thinking......")
    inbox.put(query)
    logging.info("Enqueued: %s", query)

    predict_action(query)

    print(steps)

def worker():
    while True:
        q = inbox.get()
        busy_event.set()
        try:
            result = predict_action(q)
            logging.info("Result: %s", result)
        except Exception as e:
            logging.exception("predict_action error: %s", e)
        finally:
            busy_event.clear()
            inbox.task_done()


def main():

    threading.Thread(target=worker, daemon=True).start()

    # query = "Task: Change Margins to Narrow"
    # query = "Task: Change the font size to 10"
    # query = "Task: Add a new comment with text 'Check this section'"
    # query = "Task: Center the alignment for the text"
    # query = "Task: Change the mode to Reviewing"
    # query = "Task: Insert a table with 8 rows and 6 columns"

    # predict_action(query)
    # print(steps)

    stt = STT(on_transcript=on_transcript, model_name=speech_model, device="cpu", compute_type="int8")

    start_tray_in_thread(stt, busy_event=busy_event, log_path=LOG_PATH, title="OLLA")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        stt.shutdown()

if __name__ == "__main__":
    main()

# query = "Task: Insert summation symbol"

# predict_action(query)
# print(steps)