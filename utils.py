import pyttsx3
import time
import speech_recognition as sr
import threading
import keyboard
import re


class Utils:

    def __init__(self):

        # Function to speak text
        self.engine = pyttsx3.init()
        default_rate = self.engine.getProperty("rate")  # often ~200
        self.set_voice()
        self.engine.setProperty("rate", 50)

        # Threading
        self.lock = threading.RLock()

        # Speech recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        # Listening state
        self.listening = False
        self.audio_data = None
        self.listen_thread = None  

        self.pron_map = {
            r"\bOLLA\b": "Oh-lah", 
        }

        # keyboard.add_hotkey("ctrl+shift+Z", self._shortcut_action)
        # self.speak("Hi, I am OLLA! Press Ctrl+Shift+Z to start listening.")
    
    def set_voice(self, preferred=("Zira", "David"), locale_hint=("EN-US","EN_","EN ")):

        voices = self.engine.getProperty("voices")

        for want in preferred:
            for v in voices:
                name = (v.name or "").lower()
                vid  = (v.id or "").lower()
                if want.lower() in name or want.lower() in vid:
                    self.engine.setProperty("voice", v.id)
                    return v
                
        # Try locale hint (any English voice)
        for v in voices:
            meta = f"{v.id} {v.name}".upper()
            if any(h in meta for h in locale_hint):
                self.engine.setProperty("voice", v.id)
                return v
            
        # Fallback: first available
        if voices:
            self.engine.setProperty("voice", voices[0].id)
            return voices[0]
        return None


    def _apply_pronunciations(self, text: str) -> str:

        if not text:
            return text
        
        out = text

        for pattern, replacement in self.pron_map.items():
            out = re.sub(pattern, replacement, out, flags=re.IGNORECASE)

        return out

    
    def speak(self, text: str, *, flush=True):

        if not text:
            return
        
        text = self._apply_pronunciations(text)

        with self.lock:
            try:
                if flush:
                    self.engine.stop()
                self.engine.say(text)
                self.engine.runAndWait()  
            except Exception as e:
                print("TTS error:", e)


    # def _listen_background(self):
    #     """Internal method: records audio until stopped."""
    #     with self.microphone as source:
    #         self.recognizer.adjust_for_ambient_noise(source)
    #         print("Listening... Press shortcut again to stop.")
    #         self.audio_data = self.recognizer.listen(source, timeout=None, phrase_time_limit=None)

    # def toggle_listen(self):

    #     if not self.listening:
    #         # Start listening
    #         self.listening = True
    #         self.listen_thread = threading.Thread(target=self._listen_background)
    #         self.listen_thread.start()
    #         return None
    #     else:
    #         # Stop and process audio
    #         self.listening = False
    #         if self.listen_thread and self.listen_thread.is_alive():
    #             self.listen_thread.join()

    #         if self.audio_data:
    #             try:
    #                 text = self.recognizer.recognize_google(self.audio_data)
    #                 print(f"Recognized: {text}")
    #                 return text
    #             except sr.UnknownValueError:
    #                 return "Sorry, I couldn't understand."
    #             except sr.RequestError as e:
    #                 return f"API error: {e}"
    #         else:
    #             return "No audio captured."
            
    # def _shortcut_action(self):

    #     result = self.toggle_listen()
    #     if result:
    #         print("Final result:", result)


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