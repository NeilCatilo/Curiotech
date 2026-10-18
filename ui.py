"""Minimal mobile components with local vector icons and comfortable touch targets."""

from math import cos, pi, sin

from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Line
from kivy.metrics import dp
from kivy.properties import BooleanProperty, ListProperty, NumericProperty, StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.behaviors.focus import FocusBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, TransitionBase
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget


class Copy(Label):
    base_size = NumericProperty(15)
    tone = StringProperty("text")
    heading = BooleanProperty(False)


class GentleTransition(TransitionBase):
    def on_progress(self, progress):
        self.screen_in.pos = self.screen_out.pos = self.manager.pos
        self.screen_in.opacity = progress
        self.screen_out.opacity = 1 - progress

    def on_complete(self):
        self.screen_in.opacity = self.screen_out.opacity = 1
        self.screen_in.pos = self.screen_out.pos = self.manager.pos
        super().on_complete()


class Surface(BoxLayout):
    fill = ListProperty([])
    radius = NumericProperty(16)
    outlined = BooleanProperty(False)


class Stack(BoxLayout):
    pass


class AdaptiveGrid(GridLayout):
    """Two compact filter columns; learning content itself stays in one column."""
    cell_width = NumericProperty(140)


class KeyboardActivation(FocusBehavior):
    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        if keycode[1] in ("enter", "numpadenter", "spacebar") and not self.disabled:
            if not getattr(self, "_key_pressed", False):
                self._key_pressed = True
                self.dispatch("on_press")
            return True
        return super().keyboard_on_key_down(window, keycode, text, modifiers)

    def keyboard_on_key_up(self, window, keycode):
        if keycode[1] in ("enter", "numpadenter", "spacebar") and getattr(self, "_key_pressed", False):
            self._key_pressed = False
            if self.focus and not self.disabled:
                self.dispatch("on_release")
            return True
        return super().keyboard_on_key_up(window, keycode)


class TapFeedback:
    def on_press(self):
        if not App.get_running_app().reduced_motion:
            Animation.cancel_all(self, "opacity")
            Animation(opacity=0.76, duration=0.06).start(self)

    def on_release(self):
        Animation.cancel_all(self, "opacity")
        self.opacity = 1
        App.get_running_app().play_sound("click")


class Action(TapFeedback, KeyboardActivation, ButtonBehavior, Label):
    kind = StringProperty("primary")
    base_size = NumericProperty(15)
    min_height = NumericProperty(52)
    active = BooleanProperty(False)
    fill = ListProperty([])
    text_padding = NumericProperty(28)


class Glyph(Widget):
    """Original line icons, drawn at the device's resolution without an icon font."""
    name = StringProperty("book")
    ink = ListProperty([])

    def __init__(self, **kwargs):
        kwargs.setdefault("size_hint", (None, None))
        kwargs.setdefault("size", (dp(26), dp(26)))
        super().__init__(**kwargs)
        self.bind(pos=self.draw, size=self.draw, name=self.draw, ink=self.draw)
        App.get_running_app().bind(palette=self.draw)
        self.draw()

    def draw(self, *_):
        self.canvas.clear()
        scale = min(self.width, self.height) / 24
        left, bottom = self.center_x - 12 * scale, self.center_y - 12 * scale
        def point(x, y):
            return left + x * scale, bottom + y * scale
        def stroke(*points, close=False):
            Line(points=[value for xy in points for value in point(*xy)], close=close,
                 width=max(dp(1.25), scale * 1.45), joint="round", cap="round")
        def circle(x, y, radius):
            Line(circle=(*point(x, y), radius * scale), width=max(dp(1.25), scale * 1.45))
        def box(x, y, width, height, radius=2):
            Line(rounded_rectangle=(*point(x, y), width * scale, height * scale, radius * scale), width=max(dp(1.25), scale * 1.45))
        with self.canvas:
            Color(*(self.ink or App.get_running_app().palette["accent_ink"]))
            if self.name == "menu":
                for y in (6, 12, 18):
                    stroke((4, y), (20, y))
            elif self.name == "close":
                stroke((6, 6), (18, 18)); stroke((6, 18), (18, 6))
            elif self.name == "home":
                stroke((3, 11), (12, 20), (21, 11)); stroke((6, 12), (6, 4), (18, 4), (18, 12))
                stroke((10, 4), (10, 10), (14, 10), (14, 4))
            elif self.name in ("book", "library"):
                stroke((3, 5), (8, 5), (12, 3), (16, 5), (21, 5), (21, 20), (16, 20), (12, 18), (8, 20), (3, 20), close=True)
                stroke((12, 3), (12, 18))
            elif self.name == "play":
                box(2, 4, 20, 16, 3); stroke((10, 8), (16, 12), (10, 16), close=True)
            elif self.name == "quiz":
                box(5, 2, 15, 19); stroke((9, 15), (11, 13), (16, 17)); stroke((9, 8), (16, 8))
            elif self.name == "check":
                circle(12, 12, 9); stroke((7, 12), (11, 8), (17, 16))
            elif self.name == "settings":
                circle(12, 12, 6); circle(12, 12, 2)
                for index in range(8):
                    angle = index * pi / 4
                    stroke((12 + 8 * cos(angle), 12 + 8 * sin(angle)), (12 + 10 * cos(angle), 12 + 10 * sin(angle)))
            elif self.name == "language":
                circle(12, 12, 9); stroke((3, 12), (21, 12)); stroke((12, 3), (8, 9), (8, 15), (12, 21), (16, 15), (16, 9), close=True)
            elif self.name == "text":
                stroke((3, 5), (9, 20), (15, 5)); stroke((5, 10), (13, 10)); stroke((17, 5), (20, 13), (23, 5))
            elif self.name == "sound":
                stroke((3, 9), (7, 9), (12, 5), (12, 19), (7, 15), (3, 15), close=True)
                stroke((16, 8), (18, 12), (16, 16)); stroke((20, 5), (23, 12), (20, 19))
            elif self.name == "motion":
                stroke((3, 6), (12, 6)); stroke((3, 12), (18, 12)); stroke((3, 18), (22, 18))
            elif self.name == "moon":
                stroke((15, 21), (9, 19), (5, 14), (5, 8), (10, 3), (16, 3), (21, 8), (15, 8), (11, 12), (11, 17), close=True)
            elif self.name == "chevron":
                stroke((9, 6), (15, 12), (9, 18))
            elif self.name == "back":
                stroke((15, 5), (8, 12), (15, 19))
            else:
                circle(12, 12, 9); stroke((12, 6), (12, 12)); circle(12, 17, .5)


class IconButton(TapFeedback, KeyboardActivation, ButtonBehavior, Surface):
    text = StringProperty("")
    icon_name = StringProperty("menu")
    kind = StringProperty("ghost")
    active = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(orientation="horizontal", padding=[dp(16), dp(12)], spacing=dp(12), size_hint_y=None, **kwargs)
        self.glyph = Glyph(name=self.icon_name, pos_hint={"center_y": .5})
        self.caption = Copy(text=self.text, base_size=15, pos_hint={"center_y": .5})
        self.add_widget(self.glyph)
        self.add_widget(self.caption)
        self.bind(text=lambda *_: setattr(self.caption, "text", self.text),
                  icon_name=lambda *_: setattr(self.glyph, "name", self.icon_name), kind=self.repaint)
        self.caption.bind(height=lambda *_: setattr(self, "height", max(dp(52), self.caption.height + dp(24))))
        App.get_running_app().bind(palette=self.repaint)
        self.repaint()

    def repaint(self, *_):
        app = App.get_running_app()
        self.caption.tone = "nav_text" if self.kind == "primary" else "text"
        self.glyph.ink = app.palette["nav_text"] if self.kind == "primary" else app.palette["accent_ink"]


class Page(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.scroll = ScrollView(do_scroll_x=False, bar_width=dp(3))
        self.content = Stack(padding=[dp(24), dp(94), dp(24), dp(32)], spacing=dp(20))
        self.scroll.add_widget(self.content)
        self.add_widget(self.scroll)

    def title(self, title, description=None, icon=None):
        if icon:
            self.content.add_widget(Glyph(name=icon, size=(dp(32), dp(32))))
        self.content.add_widget(Copy(text=title, base_size=26, heading=True))
        if description:
            self.content.add_widget(Copy(text=description, tone="muted"))

    def to_top(self):
        self.scroll.scroll_y = 1

    def on_pre_enter(self, *_):
        self.render()


def card(title, text, eyebrow=None, icon=None):
    panel = Surface(orientation="vertical", padding=dp(18), spacing=dp(12), size_hint_y=None)
    panel.bind(minimum_height=panel.setter("height"))
    if eyebrow:
        panel.add_widget(Copy(text=eyebrow, base_size=11, tone="accent", heading=True))
    if icon:
        row = BoxLayout(size_hint_y=None, spacing=dp(12))
        glyph = Glyph(name=icon, pos_hint={"center_y": .5})
        label = Copy(text=title, base_size=19, heading=True)
        row.add_widget(glyph); row.add_widget(label)
        label.bind(height=lambda *_: setattr(row, "height", max(label.height, dp(30))))
        panel.add_widget(row)
    else:
        panel.add_widget(Copy(text=title, base_size=19, heading=True))
    if text:
        panel.add_widget(Copy(text=text, tone="muted"))
    return panel


def button(text, callback, kind="primary", icon=None, **kwargs):
    if icon:
        control = IconButton(text=text, icon_name=icon, kind=kind, **kwargs)
    else:
        control = Action(text=text, kind=kind, **kwargs)
    control.bind(on_release=lambda *_: callback())
    return control


def horizontal(*widgets):
    row = BoxLayout(spacing=dp(8), size_hint_y=None)
    def resize(*_):
        row.height = max(child.height for child in row.children)
    for widget in widgets:
        row.add_widget(widget)
        widget.bind(height=resize)
    Clock.schedule_once(resize, 0)
    return row
