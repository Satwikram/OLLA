import time
import speech_recognition as sr
import threading
import re


# Windows COM init for SAPI
try:
    import pythoncom
    HAVE_PYCOM = True
except Exception:
    HAVE_PYCOM = False

import pyttsx3


class TTS:

    def __init__(self):

        # Function to speak text
        self.engine = pyttsx3.init()
        default_rate = self.engine.getProperty("rate")  # often ~200
        picked = self.set_voice(preferred=("Zira","David"), locale_hint=("EN-US","EN_","EN "))
        self._voice_id = picked.id if picked else self.engine.getProperty("voice")
        self.engine.setProperty("voice", self._voice_id)


        self.engine.setProperty("rate", 150)

        # Threading
        self.lock = threading.RLock()

        # Listening state
        self.listening = False
        self.audio_data = None
        self.listen_thread = None  

        self.pron_map = {
            r"\bOLLA\b": "Oh-lah", 
        }


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

    
    def speak(self, text: str, *, flush: bool = False):

        if not text:
            return
        
        text = self._apply_pronunciations(text)

        with self.lock:
            try:
                if getattr(self, "_voice_id", None):
                    self.engine.setProperty("voice", self._voice_id)

                self.engine.setProperty("rate", getattr(self, "_rate", 150))

                if flush:
                    self.engine.stop()  # only if you really want to interrupt

                self.engine.say(text)
                self.engine.runAndWait()
                
            except Exception as e:
                print("TTS error:", e)
