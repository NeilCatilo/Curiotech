"""Mobile comfort settings and team credits in English and Tagalog."""

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

from content import TEAM
from core import DEFAULT_STATE, VERSION
from ui import Copy, Page, button, card, horizontal


class SettingsScreen(Page):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.render()

    def render(self):
        app = App.get_running_app()
        t = app.tr
        settings = app.store.data["settings"]
        self.content.clear_widgets()
        self.title(t("Make it yours."), t("Your choices are saved on this device."), "settings")
        language = card(t("Language"), t("Choose the language for the app and learning content."), icon="language")
        language.add_widget(horizontal(
            button("English", lambda: app.set_preference("language", "en"), "primary" if app.language == "en" else "secondary"),
            button("Tagalog", lambda: app.set_preference("language", "tl"), "primary" if app.language == "tl" else "secondary")))
        self.content.add_widget(language)
        choices = [
            ("Appearance", "Light or dark, whichever feels comfortable.", "dark", "Light", "Dark", "moon"),
            ("Text size", "Make words easier to read.", "large_text", "Standard", "Larger", "text"),
            ("Sounds", "Soft button and answer sounds. Off by default.", "sound", "Off", "On", "sound"),
            ("Reduced motion", "Use fewer animations.", "reduced_motion", "Off", "On", "motion"),
        ]
        for title, description, key, off, on, icon in choices:
            panel = card(t(title), t(description), icon=icon)
            panel.add_widget(horizontal(
                button(t(off), lambda name=key: app.set_preference(name, False), "secondary" if settings[key] else "primary", base_size=14),
                button(t(on), lambda name=key: app.set_preference(name, True), "primary" if settings[key] else "secondary", base_size=14)))
            self.content.add_widget(panel)
        progress = app.store.data["progress"]
        panel = card(t("Your progress"), t("{count} completed sessions\nPersonal best: {best}%", count=progress["completed"], best=progress["best_score"]), icon="check")
        panel.add_widget(button(t("Clear scores"), self.confirm_reset, "secondary"))
        self.content.add_widget(panel)
        self.content.add_widget(card(t("Privacy"), t("Words, reading guides, and practice work offline. Scores and settings are saved locally; device backups may apply. Streaming video connects to YouTube, which has its own privacy policy."), icon="about"))
        self.content.add_widget(Copy(text=f"Curiocitech {VERSION}", base_size=11, tone="muted"))

    def confirm_reset(self):
        app = App.get_running_app()
        def reset():
            app.store.data["progress"] = dict(DEFAULT_STATE["progress"])
            if not app.store.save():
                app.notice("Could not clear scores", "Check available storage, then try again.")
            self.render()
        app.confirm("Clear saved scores?", "Your session count and best score will be removed. Language and other preferences will stay the same.", "Clear scores", reset)


class AboutUsScreen(Page):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.render()

    def render(self):
        app = App.get_running_app()
        t = app.tr
        self.content.clear_widgets()
        self.title(t("Everyone belongs."), t("Curiocitech helps older adults and curious learners feel at home in the digital world."), "about")
        self.content.add_widget(card(t("Our mission"), t("Connecting generations with a simple touch.")))
        self.content.add_widget(Copy(text=t("Our team"), base_size=21, heading=True))
        for name, role, photo in TEAM:
            row = BoxLayout(size_hint_y=None, spacing=dp(14))
            row.add_widget(Image(source=app.asset(photo), fit_mode="contain", size_hint_x=None, width=dp(66)))
            details = card(name, t(role))
            row.add_widget(details)
            details.bind(height=lambda widget, height, target=row: setattr(target, "height", max(height, dp(90))))
            self.content.add_widget(row)
        self.content.add_widget(card(t("Contact"), "acarannessa@gmail.com"))
