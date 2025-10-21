from pynput import keyboard
import threading


class HotkeyActivator:

    """
    Global F9 hotkey that can run in the background.

    """

    def __init__(self, on_start, on_stop=None, key=keyboard.Key.f9, mode="hold"):

        self.on_start = on_start
        self.on_stop = on_stop
        self.key = key
        self.mode = mode

        self._active = False
        self._lock = threading.Lock()
        self.active_event = threading.Event()

        self._listener = keyboard.Listener(
            on_press=self._on_press,
            on_release=self._on_release
        )

        self.listener.daemon = True
        self.listener.start()  # non-blocking; runs in background


    @property
    def active(self):
        with self._lock:
            return self._active


    def _start(self):

        with self._lock:
            if self._active:
                return
            
            self._active = True
            self.active_event.set()

        if self.on_start:
            threading.Thread(target=self.on_start, daemon=True).start()


    def _stop(self):

        with self._lock:
            if not self._active:
                return
            
            self._active = False
            self.active_event.clear()

        if self._on_stop:
            threading.Thread(target=self.on_stop, daemon=True).start()


    def _on_press(self, key):

        if key == self.key:

            if self.mode == "hold":
                self._start()

            elif self.mode == "toggle":
                if self.active:
                    self._stop()
                else:
                    self._start()

    def _on_release(self, key):
        if self.mode == "hold" and key == self.key:
            self._stop()