"""A mobile canvas and a single drawer menu. No app bars or bottom navigation."""

from kivy.animation import Animation
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.modalview import ModalView
from kivy.uix.scrollview import ScrollView

from core import VERSION
from ui import Copy, Glyph, Page, Stack, Surface, button, card, horizontal

NAVIGATION = [
    ("main", "Home", "home"), ("dictionary", "Dictionary", "book"),
    ("Article", "Library", "library"), ("video", "Videos", "play"),
    ("start", "Practice", "quiz"), ("settings", "Settings", "settings"),
    ("about_us", "About", "about"),
]


class MenuDrawer(ModalView):
    def __init__(self, shell, **kwargs):
        app = App.get_running_app()
        super().__init__(size_hint=(1, 1), background="", background_color=(0, 0, 0, 0),
                         overlay_color=(0, 0, 0, .30), auto_dismiss=False, **kwargs)
        self.shell = shell
        self.stage = FloatLayout()
        self.panel = Surface(orientation="vertical", radius=0, size_hint=(None, None))
        self.stage.add_widget(self.panel)
        self.add_widget(self.stage)
        self.bind(size=self.fit, pos=self.fit, on_open=self.slide_in)
        self.nav_buttons = {}
        self.render()

    def fit(self, *_):
        self.panel.size = (min(self.width * .90, dp(350)), self.height)
        self.panel.pos = self.pos

    def slide_in(self, *_):
        self.fit()
        if not App.get_running_app().reduced_motion:
            self.panel.x = self.x - self.panel.width
            Animation(x=self.x, duration=.18, t="out_quad").start(self.panel)

    def render(self):
        app = App.get_running_app()
        t = app.tr
        self.panel.clear_widgets()
        scroll = ScrollView(do_scroll_x=False, bar_width=dp(3))
        content = Stack(padding=[dp(20), dp(28), dp(20), dp(28)], spacing=dp(10))
        close = button(t("Close menu"), self.shell.close_menu, "ghost", icon="close")
        content.add_widget(close)
        content.add_widget(Copy(text="Curiocitech", base_size=25, heading=True))
        content.add_widget(Copy(text=t("Your digital companion"), base_size=13, tone="muted"))
        current = {"quiz": "start", "lesson": "Article"}.get(app.manager.current, app.manager.current)
        self.nav_buttons = {}
        for destination, message, icon in NAVIGATION:
            control = button(t(message), lambda dest=destination: app.navigate(dest, section=True),
                             "secondary" if destination == current else "ghost", icon=icon)
            control.active = destination == current
            self.nav_buttons[destination] = control
            content.add_widget(control)
        content.add_widget(Copy(text=t("Language"), base_size=13, tone="muted"))
        content.add_widget(horizontal(
            button("English", lambda: app.set_preference("language", "en"), "primary" if app.language == "en" else "secondary", base_size=13),
            button("Tagalog", lambda: app.set_preference("language", "tl"), "primary" if app.language == "tl" else "secondary", base_size=13)))
        content.add_widget(Copy(text=f"Curiocitech {VERSION}", base_size=11, tone="muted"))
        scroll.add_widget(content)
        self.panel.add_widget(scroll)

    def on_touch_down(self, touch):
        if not self.panel.collide_point(*touch.pos):
            self.shell.close_menu()
            return True
        return super().on_touch_down(touch)


class AppShell(FloatLayout):
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)
        self.manager = manager
        self.manager.size_hint = (None, None)
        self.add_widget(manager)
        self.menu_view = None
        self.menu_button = button(App.get_running_app().tr("Menu"), self.open_menu,
                                  "secondary", icon="menu", size_hint_x=None, width=dp(120))
        self.add_widget(self.menu_button)
        self.bind(size=self.fit, pos=self.fit)
        self.menu_button.bind(height=self.fit)
        App.get_running_app().bind(language=self.update_navigation)
        self.fit()

    @property
    def menu_open(self):
        return self.menu_view is not None

    def fit(self, *_):
        self.manager.size = (min(self.width, dp(560)), self.height)
        self.manager.pos = (self.center_x - self.manager.width / 2, self.y)
        self.menu_button.pos = (self.manager.x + dp(20),
                                self.top - dp(18) - self.menu_button.height)

    def open_menu(self):
        if self.menu_view:
            return
        self.menu_view = MenuDrawer(self)
        self.menu_view.bind(on_dismiss=self._menu_dismissed)
        self.menu_view.open(animation=not App.get_running_app().reduced_motion)

    def close_menu(self):
        if self.menu_view:
            self.menu_view.dismiss(animation=not App.get_running_app().reduced_motion)

    def _menu_dismissed(self, *_):
        self.menu_view = None

    def update_navigation(self, *_):
        self.menu_button.text = App.get_running_app().tr("Menu")
        if self.menu_view:
            self.menu_view.render()


class MainScreen(Page):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.render()

    def render(self):
        app = App.get_running_app()
        t = app.tr
        self.content.clear_widgets()
        brand = BoxLayout(size_hint_y=None, height=dp(64), spacing=dp(16))
        brand.add_widget(Image(source=app.asset("Images/app-icon.png"), size_hint=(None, None),
                               size=(dp(58), dp(58)), fit_mode="contain", pos_hint={"center_y": .5}))
        brand.add_widget(Copy(text="Curiocitech", base_size=25, heading=True, pos_hint={"center_y": .5}))
        self.content.add_widget(brand)
        self.title(t("Your everyday digital guide."), t("Curiocitech helps older adults and curious learners use technology with clear English and Tagalog guidance."))
        panel = card(t("What you can do here"), "")
        for icon, message in [("book", "Understand everyday technology words."),
                              ("library", "Follow simple, step-by-step guides."),
                              ("play", "Watch helpful videos inside the app."),
                              ("quiz", "Practise with questions and explanations.")]:
            row = BoxLayout(size_hint_y=None, spacing=dp(12))
            row.add_widget(Glyph(name=icon, pos_hint={"center_y": .5}))
            description = Copy(text=t(message), base_size=14, tone="muted")
            row.add_widget(description)
            description.bind(height=lambda widget, value, target=row: setattr(target, "height", max(value, dp(32))))
            panel.add_widget(row)
        self.content.add_widget(panel)
        self.content.add_widget(card(t("How to begin"), t("Tap Menu at the upper left and choose a topic. You can change the language and reading size in Settings. Learn at your own pace.")))
        progress = app.store.data["progress"]
        if progress["completed"]:
            self.content.add_widget(Copy(text=t("{count} practice sessions · Best: {best}%", count=progress["completed"], best=progress["best_score"]), base_size=13, tone="muted"))
