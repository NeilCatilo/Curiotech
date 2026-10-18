"""Curiocitech mobile app. Running on a PC opens a portrait development preview."""

import os
import sys
from pathlib import Path

# Configure before importing Window; assets never depend on the launch directory.
os.environ.setdefault("KIVY_NO_ARGS", "1")
from kivy.config import Config
from kivy.utils import platform

Config.set("input", "mouse", "mouse,multitouch_on_demand")
if platform not in ("android", "ios"):
    Config.set("graphics", "width", "412")
    Config.set("graphics", "height", "820")
    Config.set("graphics", "minimum_width", "320")
    Config.set("graphics", "minimum_height", "540")

from kivy.app import App
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.properties import BooleanProperty, DictProperty, NumericProperty, StringProperty
from kivy.metrics import dp, sp
from kivy.resources import resource_add_path
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager

from core import LocalStore, NavigationHistory
from i18n import LANGUAGES, translate

BASE_DIR = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
LIGHT = {
    "background": [0.965, 0.973, 0.961, 1], "surface": [1, 1, 1, 1],
    "text": [0.10, 0.18, 0.22, 1], "muted": [0.34, 0.40, 0.43, 1],
    "accent": [0.10, 0.39, 0.38, 1], "accent_ink": [0.10, 0.39, 0.38, 1], "soft": [0.89, 0.93, 0.90, 1],
    "border": [0.85, 0.88, 0.85, 1], "orange": [0.58, 0.29, 0.10, 1], "brand": [0.97, 0.65, 0.38, 1],
    "success": [0.10, 0.38, 0.26, 1], "error": [0.64, 0.18, 0.17, 1],
    "nav": [0.08, 0.18, 0.23, 1], "nav_text": [0.94, 0.96, 0.94, 1],
    "nav_selected": [0.16, 0.31, 0.34, 1], "selection": [0.28, 0.60, 0.52, 0.3],
}
DARK = {
    "background": [0.065, 0.10, 0.12, 1], "surface": [0.10, 0.16, 0.18, 1],
    "text": [0.94, 0.96, 0.94, 1], "muted": [0.69, 0.77, 0.77, 1],
    "accent": [0.16, 0.47, 0.43, 1], "accent_ink": [0.62, 0.85, 0.74, 1], "soft": [0.14, 0.24, 0.25, 1],
    "border": [0.23, 0.32, 0.33, 1], "orange": [0.98, 0.72, 0.46, 1], "brand": [0.97, 0.65, 0.38, 1],
    "success": [0.51, 0.86, 0.65, 1], "error": [1, 0.65, 0.61, 1],
    "nav": [0.07, 0.13, 0.16, 1], "nav_text": [0.94, 0.96, 0.94, 1],
    "nav_selected": [0.15, 0.31, 0.32, 1], "selection": [0.28, 0.60, 0.52, 0.4],
}


class CuriocitechApp(App):
    title = "Curiocitech"
    palette = DictProperty(LIGHT)
    text_scale = NumericProperty(1)
    reduced_motion = BooleanProperty(False)
    sound_enabled = BooleanProperty(False)
    dark = BooleanProperty(False)
    language = StringProperty("en")

    def tr(self, message, **values):
        return translate(message, self.language, **values)

    def asset(self, name):
        return str(BASE_DIR / name)

    def build(self):
        resource_add_path(str(BASE_DIR))
        LabelBase.register("Body", fn_regular=self.asset("FONTS/Lexend-Regular.ttf"))
        LabelBase.register("Display", fn_regular=self.asset("FONTS/LufgaBold.ttf"))
        Builder.load_file(self.asset("ui.kv"))
        self.icon = self.asset("Images/app-icon.png")
        state_dir = Path(os.environ.get("CURIOCITECH_DATA_DIR", self.user_data_dir))
        self.store = LocalStore(state_dir / "learning.json")
        self.apply_preferences()
        self.history = NavigationHistory()
        self.sounds = {}
        self.dialog = None
        self._exiting = False
        from ui import GentleTransition
        self.manager = ScreenManager(transition=GentleTransition(duration=0.16))

        from Manager import AppShell, MainScreen
        from Dictionary import DictionaryScreen
        from Article import ArticleScreen, LessonScreen
        from Video import VideoScreen
        from Quizzes import StartQuizScreen, QuizScreen
        from About import AboutUsScreen, SettingsScreen

        for screen in [MainScreen(name="main"), DictionaryScreen(name="dictionary"),
                       ArticleScreen(name="Article"), VideoScreen(name="video"),
                       StartQuizScreen(name="start"), QuizScreen(name="quiz"),
                       SettingsScreen(name="settings"), AboutUsScreen(name="about_us"), LessonScreen(name="lesson")]:
            self.manager.add_widget(screen)
        root = AppShell(self.manager)
        self.manager.bind(current=lambda *_: root.update_navigation())
        Window.bind(on_keyboard=self.handle_back_button, on_request_close=self.request_close)
        return root

    def open_guide(self, guide_id):
        from lessons import get_guide
        if get_guide(guide_id) is None:
            raise ValueError("Unknown reading guide")
        lesson = self.manager.get_screen("lesson")
        lesson.guide_id = guide_id
        lesson.to_top()
        if self.manager.current == "lesson":
            lesson.render()
        self.navigate("lesson")

    def on_start(self):
        self._audio_event = Clock.schedule_once(self.load_sounds, 0.3)
        if self.store.last_error:
            Clock.schedule_once(lambda *_: self.notice("Local preferences", "Your previous settings could not be read. Default settings are available."), 0.5)

    def load_sounds(self, *_):
        for key, filename in {"click": "click.mp3", "right": "rightanswer-95219.mp3", "wrong": "wronganswer-37702.mp3"}.items():
            try:
                sound = SoundLoader.load(self.asset("Sounds/" + filename))
                if sound:
                    sound.volume = 0.25
                    self.sounds[key] = sound
            except Exception:
                Logger.warning("Curiocitech: optional audio unavailable")

    def play_sound(self, key):
        if self.sound_enabled and key in self.sounds:
            self.sounds[key].stop()
            self.sounds[key].play()

    def apply_preferences(self):
        settings = self.store.data["settings"]
        self.dark = settings["dark"]
        self.palette = dict(DARK if self.dark else LIGHT)
        self.text_scale = 1.2 if settings["large_text"] else 1
        self.reduced_motion = settings["reduced_motion"]
        self.sound_enabled = settings["sound"]
        self.language = settings["language"]
        Window.clearcolor = self.palette["background"]

    def set_preference(self, name, value):
        if name == "language":
            if value not in LANGUAGES:
                raise ValueError("Unsupported language")
        elif name not in ("dark", "large_text", "sound", "reduced_motion") or type(value) is not bool:
            raise ValueError("Invalid preference")
        previous_language = self.language
        self.store.data["settings"][name] = value
        self.apply_preferences()
        if not self.store.save():
            self.notice("Settings could not be saved", "You can keep using the app. Your changes may not be remembered after closing it.")
        if self.language != previous_language:
            for screen in self.manager.screens:
                screen.render()
        else:
            self.manager.get_screen("settings").render()

    def navigate(self, destination, section=False):
        if not self.manager.has_screen(destination):
            raise ValueError(f"Unknown screen: {destination}")
        self.history.go(destination, section=section)
        if self.root:
            self.root.close_menu()
        self._set_screen(destination)

    def _set_screen(self, destination):
        # Finish the previous transition before replacing it. Rapid taps can
        # otherwise leave an orphaned animation that removes the current canvas.
        self.manager.transition.stop()
        if destination != self.manager.current:
            self.manager.transition.duration = 0 if self.reduced_motion else 0.16
            self.manager.current = destination

    def go_back(self):
        if self.dialog:
            self.dialog.dismiss()
        elif self.root and self.root.menu_open:
            self.root.close_menu()
        elif self.manager.current != "main":
            self._set_screen(self.history.back())
        else:
            self.request_close()

    def handle_back_button(self, window, key, *_):
        if key == 27:
            self.go_back()
            return True
        return False

    def request_close(self, *_):
        if self._exiting:
            return False
        if not self.dialog:
            self.confirm("Take a break?", "Your saved settings and completed quiz scores will be here when you return.", "Close app", self.exit_app)
        return True

    def exit_app(self):
        self._exiting = True
        self.stop()

    def _popup(self, title, text, actions):
        from ui import Copy, horizontal
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.scrollview import ScrollView
        if self.dialog:
            self.dialog.dismiss()
        body = BoxLayout(orientation="vertical", padding=dp(20), spacing=dp(16))
        scroll = ScrollView(do_scroll_x=False, bar_width=dp(3))
        scroll.add_widget(Copy(text=self.tr(text)))
        body.add_widget(scroll)
        body.add_widget(horizontal(*actions))
        popup = Popup(title=self.tr(title), title_font="Display", title_size=sp(18 * self.text_scale),
                      content=body, size_hint=(None, None), width=min(Window.width - dp(32), dp(420)),
                      background="", background_color=self.palette["surface"],
                      separator_color=self.palette["accent"], title_color=self.palette["text"], auto_dismiss=True)
        popup.height = min(Window.height - dp(48), dp(390 * self.text_scale))
        popup.bind(on_dismiss=lambda *_: self._dismissed(popup))
        self.dialog = popup
        popup.open(animation=not self.reduced_motion)
        return popup

    def _dismissed(self, popup):
        if self.dialog is popup:
            self.dialog = None

    def notice(self, title, text):
        from ui import button
        return self._popup(title, text, [button(self.tr("Got it"), lambda: self.dialog.dismiss())])

    def confirm(self, title, text, action, callback):
        from ui import button
        def accept():
            self.dialog.dismiss()
            callback()
        return self._popup(title, text, [button(self.tr("Cancel"), lambda: self.dialog.dismiss(), "secondary"), button(self.tr(action), accept)])

    def open_link(self, url):
        from urllib.parse import urlsplit
        parsed = urlsplit(url)
        if parsed.scheme != "https" or not parsed.hostname:
            self.notice("Link unavailable", "This resource does not have a valid secure web address.")
            return
        self.confirm("Open in your browser?", self.tr("You are visiting {host}.\n\nInternet access is needed. This service has its own language, privacy policy, and possible charges.", host=parsed.hostname), "Open link", lambda: self._launch_url(url))

    def _launch_url(self, url):
        try:
            if platform == "android":
                from importlib import import_module
                autoclass = import_module("jnius").autoclass
                activity = autoclass("org.kivy.android.PythonActivity").mActivity
                intent = autoclass("android.content.Intent")
                uri = autoclass("android.net.Uri")
                activity.startActivity(intent(intent.ACTION_VIEW, uri.parse(url)))
            else:
                import webbrowser
                if not webbrowser.open(url):
                    raise RuntimeError("No browser available")
        except Exception:
            Logger.exception("Curiocitech: browser launch failed")
            self.notice("Could not open your browser", "Check that a browser is installed and that your device is connected to the internet, then try again.")

    def on_pause(self):
        self.manager.get_screen("video").stop_video()
        quiz = self.manager.get_screen("quiz")
        quiz._backgrounded = True
        quiz.pause_feedback()
        self.store.save()
        return True

    def on_resume(self):
        quiz = self.manager.get_screen("quiz")
        quiz._backgrounded = False
        quiz.resume_feedback()

    def on_stop(self):
        self.manager.get_screen("video").stop_video()
        self.manager.get_screen("quiz").pause_feedback()
        self.store.save()
        if hasattr(self, "_audio_event"):
            self._audio_event.cancel()
        for sound in self.sounds.values():
            sound.stop()
        Window.unbind(on_keyboard=self.handle_back_button, on_request_close=self.request_close)


FinalApp = CuriocitechApp

if __name__ == "__main__":
    CuriocitechApp().run()
