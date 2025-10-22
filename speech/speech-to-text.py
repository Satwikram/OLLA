import numpy as np
import os
import sounddevice as sd
import soundfile as sf
import tempfile
from faster_whisper import WhisperModel  # only needed where you create the model
from pynput import keyboard
from utils import Utils


class STT:
    """
    Start/stop mic capture (no threads), buffer in RAM, transcribe on stop.
    - start(): begin recording
    - stop():  end recording, run Whisper, return text ("" if nothing captured)
    """

    def __init__(self, model, sample_rate: int = 16000):
        self.model = model
        self.sr = sample_rate
        self._buf = []
        self._stream = None

        # start keyboard hook in background
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.daemon = True
        self.listener.start()  # runs in background

        self.speaker = Utils()
        self.speaker.speak("Hi there--this is OLLA. ")

    def _cb(self, indata, _frames, _time, status):
        # 'frames' and 'time' are part of the API; unused here.

        if status:
            return
        if indata.size:
            self._buf.append(indata.copy())

    def start(self):

        if self._stream is not None:
            self.speaker.speak("(already recording)")
            return

        self._buf = []
        self._stream = sd.InputStream(
            samplerate=self.sr,
            channels=1,
            dtype="float32",
            callback=self._cb,
        )
        self._stream.start()

    def stop(self) -> str:
        if self._stream is None:
            return ""

        try:
            self._stream.stop()
            self._stream.close()
        finally:
            self._stream = None

        if not self._buf:  # nothing recorded
            return ""

        audio = np.concatenate(self._buf, axis=0).reshape(-1)

        # --- Windows-safe temp file handling ---
        wav_path = None
        try:
            fd, wav_path = tempfile.mkstemp(suffix=".wav")
            os.close(fd)  # close so soundfile can open it
            sf.write(wav_path, audio, self.sr)
            segs, _ = self.model.transcribe(wav_path, vad_filter=True, beam_size=1)
            text = " ".join(s.text for s in segs).strip()
        finally:
            if wav_path and os.path.exists(wav_path):
                os.unlink(wav_path)

        # free memory for next run
        self._buf = []
        return text
    

    # ---- hotkey activation----
    def on_press(self, key) -> str:

        def is_f9(key):
            return (
                key == keyboard.Key.f9
                or getattr(key, "vk", None) == 120  # F9 virtual key
                or getattr(key, "name", None) == "f9"
            )


        if is_f9(key):
            if self._stream is None:
                try:
                    self.start()

                except Exception as e:
                    print("Could not start recording:", e)
                    self.speaker.speak("Hmmm...something went wrong!")
            else:
                try:
                    text = self.stop()
                    print("Transcript:", repr(text))
                    print("Press F9 to start again.")

                except Exception as e:
                    print("Could not stop/transcribe:", e)


model = WhisperModel("small", device="cpu", compute_type="int8")
stt = STT(model, sample_rate=16000)

# print("Recording… press Enter to stop.")
# stt.start()
# input()  # speak now
# text = stt.stop()
# print("Transcript:", repr(text))



print("Press F9 to start recording, then press Enter to stop.")
# input()  # stop when you’re done speaking
# text = stt.stop()
# print("Transcript:", repr(text))

