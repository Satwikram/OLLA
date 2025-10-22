import os
import tempfile
import threading
import numpy as np
import sounddevice as sd
import soundfile as sf
from pynput import keyboard
from faster_whisper import WhisperModel
from utils import Utils


class STT:
    """
    Start/stop mic capture, buffer in RAM, transcribe on stop.
    - start(): begin recording
    - stop():  end recording, run Whisper, return text ("" if nothing captured)
    """

    def __init__(
            self,
            on_transcript=None, # callable(str) -> None
            model: WhisperModel | None = None,
            model_name: str = "small",
            device: str = "cpu",
            compute_type: str = "int8",
            sample_rate: int = 16000,
            input_device: int | None = None,    # sounddevice input device index
            hotkey: str = "f9",
            verbose: bool = True,
            ):
    
        self.on_transcript = on_transcript or (lambda s: print("Transcript:", repr(s)))
        self.model = model or WhisperModel(model_name, device=device, compute_type=compute_type)
        self.sr = sample_rate
        self.input_device = input_device
        self.hotkey = hotkey.lower()
        self.verbose = verbose


        self._buf: list[np.ndarray] = []

        self._stream = sd.InputStream | None = None

        # Concurrency guards
        self._lock = threading.Lock()       # protects _stream and _buf
        self._transcribing = False          # true while worker is running

        # start keyboard hook in background
        self._listener = keyboard.Listener(on_release=self._on_release)
        self._listener.daemon = True
        self._listener.start()  # runs in background

        if self.verbose:
            print(f"[HotkeySTT] Ready. Release {self.hotkey.upper()} to start/stop.")


        #SST is ready to take inputs
        self.speaker = Utils()
        self.speaker.speak("Hi there--this is OLLA!")

    # Audio
    def _cb(self, indata, _frames, _time, status):
        # 'frames' and 'time' are part of the API; unused here.

        if status:
            return
        
        if indata.size:
            with self._lock:
                self._buf.append(indata.copy())

    def start(self):

        with self._lock:

            if self._stream is not None or self._transcribing:
                if self.verbose:
                    self.speaker.speak("(already recording)")
                    print("[HotkeySTT] Busy (already recording or transcribing).")
                return

            self._buf = []

            try:

                self._stream = sd.InputStream(
                    samplerate=self.sr,
                    channels=1,
                    dtype="int16", # compact; halves RAM vs float32
                    device=self.input_device,
                    callback=self._cb,
                )
                self._stream.start()

            except Exception as e:

                # Fallback to 48k if 16k unsupported
                if self.sr != 48000:
                    if self.verbose:
                        print(f"[HotkeySTT] {e} -- retrying with 48000 Hz.")

                    self.sr = 48000
                    self._stream = sd.InputStream(
                        samplerate=self.sr,
                        channels=1,
                        dtype="int16",
                        device=self.input_device,
                        callback=self._cb,
                    )
                    self._stream.start()
                else:
                    raise

        if self.verbose:
            print(f"[HotkeySTT] Recording… release {self.hotkey.upper()} again to stop.")


    def _stop_and_transcribe_worker(self):
        """Run stop()+transcribe on a worker thread; guarded by _transcribing flag."""

        try:
            text = self.stop()  # stop() calls on_transcript() internally

            if self.verbose and text == "":
                print("[HotkeySTT] (empty transcript)")

        except Exception as e:
            if self.verbose:
                print("[HotkeySTT] Transcription error:", e)

        finally:
            with self._lock:
                self._transcribing = False


    def stop(self) -> str:
        # Take ownership of the stream and close it outside the lock quickly
        with self._lock:
            stream = self._stream
            self._stream = None

        if stream is None:
            return ""

        try:
            stream.stop()
            stream.close()
        finally:
            stream = None

        # Snapshot the buffer safely
        with self._lock:
            if not self._buf:
                self._buf = []
                if self.verbose:
                    print("[HotkeySTT] No audio captured.")
                return ""
            audio = np.concatenate(self._buf, axis=0).reshape(-1)  # int16
            self._buf = []  # free for next run

        # Windows-safe temp handling
        wav_path = None
        try:
            fd, wav_path = tempfile.mkstemp(suffix=".wav")
            os.close(fd)  # allow libsndfile to open by path
            sf.write(wav_path, audio, self.sr)  # PCM16 WAV

            segs, _ = self.model.transcribe(
                wav_path,
                vad_filter=True,
                beam_size=1,
            )
            text = " ".join(s.text for s in segs).strip()
        finally:
            if wav_path and os.path.exists(wav_path):
                os.unlink(wav_path)

        # Fire the callback (exceptions are contained)
        try:
            self.on_transcript(text)
        except Exception as cb_err:
            if self.verbose:
                print("[HotkeySTT] on_transcript() raised:", cb_err)

        return text
    
    def _is_hotkey(self, key) -> bool:
        # Accept Key.fX, name='fx', or Windows VK for F-keys
        if isinstance(key, keyboard.Key) and str(key) == f"Key.{self.hotkey}":
            return True
        if getattr(key, "name", None) == self.hotkey:
            return True
        vk = getattr(key, "vk", None)
        return vk == {"f1": 112, "f2": 113, "f3": 114, "f4": 115, "f5": 116,
                      "f6": 117, "f7": 118, "f8": 119, "f9": 120, "f10": 121,
                      "f11": 122, "f12": 123}.get(self.hotkey, -1)


    def _on_release(self, key):
        if not self._is_hotkey(key):
            return

        # If recording -> spawn worker to stop+transcribe
        with self._lock:
            recording = self._stream is not None
            if recording and self._transcribing:
                # Shouldn't happen; stream can't be open while transcribing
                return
            if not recording and self._transcribing:
                # Busy: ignore this press; user can try again after transcription finishes
                if self.verbose:
                    print("[HotkeySTT] Still transcribing…")
                return

        if recording:
            with self._lock:
                if self._transcribing:
                    return
                self._transcribing = True
            threading.Thread(target=self._stop_and_transcribe_worker, daemon=True).start()
        else:
            self.start()

    # ---------- Utilities ----------
    @property
    def is_recording(self) -> bool:
        with self._lock:
            return self._stream is not None

    def shutdown(self):
        with self._lock:
            stream = self._stream
            self._stream = None
        if stream is not None:
            try:
                stream.stop()
                stream.close()
            except Exception:
                pass
        if self._listener is not None:
            self._listener.stop()


def got_text(transcript: str):
    obj = Utils()
    obj.speak(transcript)

stt = STT(on_transcript=got_text, model_name="small", device="cpu", compute_type="int8")

try:
    import time
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    stt.shutdown()



# print("Recording… press Enter to stop.")
# stt.start()
# input()  # speak now
# text = stt.stop()
# print("Transcript:", repr(text))


# input()  # stop when you’re done speaking
# text = stt.stop()
# print("Transcript:", repr(text))

