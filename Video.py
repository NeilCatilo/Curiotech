"""Localised video catalogue with existing thumbnails."""

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.image import Image
from kivy.utils import platform
from kivy.logger import Logger

from content import VIDEOS
from ui import Copy, Page, button, card


class VideoScreen(Page):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.player = None
        self.render()

    def render(self):
        app = App.get_running_app()
        t = app.tr
        self.content.clear_widgets()
        self.title(t("Watch and learn."), t("Pause, replay, and take your time."), "play")
        self.content.add_widget(Copy(text=t("Videos stream from YouTube inside the Android app. Internet is needed; the publisher controls captions, language, and availability."), base_size=12, tone="muted"))
        for category, title, description, video_id, image in VIDEOS:
            panel = card(t(title), t(description), t(category))
            panel.add_widget(Image(source=app.asset(image), fit_mode="contain", size_hint_y=None, height=dp(138)), index=len(panel.children))
            panel.add_widget(button(t("Watch in app"), lambda code=video_id: self.watch(code), "secondary", icon="play"))
            self.content.add_widget(panel)

    def watch(self, video_id):
        app = App.get_running_app()
        video = next((video for video in VIDEOS if video[3] == video_id), None)
        if video is None:
            raise ValueError("Unknown video")
        if platform != "android":
            app.confirm("Android player preview", "In-app playback is available in the Android build. This computer preview cannot run Android's video player.",
                        "Open on YouTube", lambda: app.open_link("https://www.youtube.com/watch?v=" + video_id))
            return
        try:
            if self.player is None:
                from player import AndroidYouTubePlayer
                self.player = AndroidYouTubePlayer()
            self.player.open(video_id, app.tr(video[1]), app.language, app.dark)
        except Exception:
            Logger.exception("Curiocitech: in-app video player unavailable")
            app.confirm("Video player unavailable", "Please update Android System WebView and try again. You can also use Open on YouTube.",
                        "Open on YouTube", lambda: app.open_link("https://www.youtube.com/watch?v=" + video_id))

    def stop_video(self):
        if self.player:
            self.player.close()

    def on_pre_leave(self, *_):
        self.stop_video()
