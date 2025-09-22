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

engine = pyttsx3.init()
engine.say("Hello, this is an announcement.")
engine.runAndWait()