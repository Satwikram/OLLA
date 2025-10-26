# package/tray.py
import os
import sys
import threading
from pathlib import Path

import pystray
from pystray import MenuItem as Item, Menu
from PIL import Image, ImageDraw

try:
    import pythoncom  # optional; helps on some Windows setups
except Exception:
    pythoncom = None


def _assets_dir() -> Path:
    """Return the assets folder both in dev and in a PyInstaller onefile build."""
    if hasattr(sys, "_MEIPASS"):
        # we copy assets to sys._MEIPASS/assets via --add-data "assets;assets"
        return Path(sys._MEIPASS) / "assets"
    # running from source; assets sits at project root
    # package/tray.py  -> parents[1] is project root
    return Path(__file__).resolve().parents[1] / "assets"


def _load_icon() -> Image.Image:
    assets = _assets_dir()
    for name in ("olla_tray.ico", "olla_tray.png"):
        p = assets / name
        if p.exists():
            return Image.open(p)
    # Fallback: simple blue dot with “O”
    im = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse((8, 8, 56, 56), fill=(0, 120, 215, 255))
    d.text((24, 18), "O", fill="white")
    return im


class TrayApp:
    """
    System tray controller.
    Menu:
      • Status (Busy/Idle)
      • Start/Stop Listening (calls stt.start/stop)
      • Mute/Unmute TTS (optional)
      • Open Logs (optional)
      • Exit
    """

    def __init__(self, stt, *, tts=None, busy_event=None, log_path: str | None = None, title: str = "OLLA"):
        self.stt = stt
        self.tts = tts
        self.busy_event = busy_event
        self.log_path = log_path
        self.title = title
        self.muted = False
        self.icon: pystray.Icon | None = None

    # ---- menu actions ----
    def _toggle_listen(self, icon, item):
        if self.stt.is_recording:
            self.stt.stop()
        else:
            self.stt.start()

    def _toggle_mute(self, icon, item):
        self.muted = not self.muted
        if self.tts and hasattr(self.tts, "muted"):
            self.tts.muted = self.muted

    def _open_logs(self, icon, item):
        if self.log_path and os.path.exists(self.log_path):
            os.startfile(self.log_path)

    def _quit(self, icon, item):
        try:
            if self.stt:
                self.stt.shutdown()
        finally:
            icon.stop()

    # ---- dynamic labels ----
    def _status_label(self, _item):
        return "Status: Busy" if (self.busy_event and self.busy_event.is_set()) else "Status: Idle"

    def _listen_label(self, _item):
        return "Stop Listening" if self.stt.is_recording else "Start Listening"

    def _mute_label(self, _item):
        return "Unmute TTS" if self.muted else "Mute TTS"

    def _menu(self):
        return Menu(
            Item(self._status_label, enabled=False),
            Item(self._listen_label, self._toggle_listen),
            Item(self._mute_label, self._toggle_mute),
            Item("Open Logs", self._open_logs, enabled=bool(self.log_path)),
            Item("Exit", self._quit),
        )

    def run(self):
        if pythoncom:
            try:
                pythoncom.CoInitialize()
            except Exception:
                pass
        self.icon = pystray.Icon(self.title, _load_icon(), self.title, self._menu())
        self.icon.run()


def start_tray_in_thread(stt, *, tts=None, busy_event=None, log_path: str | None = None, title="OLLA"):
    app = TrayApp(stt, tts=tts, busy_event=busy_event, log_path=log_path, title=title)
    t = threading.Thread(target=app.run, daemon=True)
    t.start()
    return app