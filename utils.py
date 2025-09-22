import pyttsx3
import time


class Utils:

    def __init__(self):
        # Function to speak text
        self.engine = pyttsx3.init()

    
    def speak(self, text):
        self.engine.stop()
        self.engine.say(text)
        self.engine.runAndWait()

    def base36(self, n: int) -> str:

        ALPHABET = '0123456789abcdefghijklmnopqrstuvwxyz'

        if n == 0: return '0'
        s = []
        while n:
            n, r = divmod(n, 36)
            s.append(ALPHABET[r])

        return ''.join(reversed(s))

    def time_id_ms(self) -> str:
        
        return self.base36(int(time.time() * 1000))

# engine = pyttsx3.init()
# engine.say("Hello, this is an announcement.")
# engine.runAndWait()