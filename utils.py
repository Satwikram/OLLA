import pyttsx3
# class Utils:

#     def __init__(self):
#         # Function to speak text
#         self.engine = pyttsx3.init()

    
#     def speak(self, text):
#         self.engine.say(text)
#         self.engine.runAndWait()

# obj = Utils()

# obj.speak("Hi, How are you? Satwik !")
# print("Done")

# engine = pyttsx3.init()
# engine.say("Hello, this is an announcement.")
# engine.runAndWait()

from gtts import gTTS
from playsound import playsound
import os
import winsound

def google_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    filename = "temp_announcement.mp3"
    tts.save(filename)
    playsound(filename, winsound.SND_FILENAME)
    os.remove(filename)

# Example usage
google_speech("Hello, this is an announcement from Google Text to Speech!")


