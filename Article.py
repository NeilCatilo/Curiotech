"""Offline reading lessons; external sites are optional further reading."""

from kivy.app import App
from kivy.metrics import dp

from lessons import GUIDES, get_guide
from ui import AdaptiveGrid, Copy, Page, Stack, button, card


class ArticleScreen(Page):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.category = "All"
        self.render()

    def render(self):
        t = App.get_running_app().tr
        self.content.clear_widgets()
        self.title(t("Read and try it here."), t("Open a guide for steps you can follow. The instructions work offline; links are optional."), "library")
        filters = AdaptiveGrid()
        self.filter_buttons = {}
        for category in ("All", "Internet basics", "App guides", "News & radio"):
            control = button(t(category), lambda value=category: self.set_category(value), "secondary", base_size=13)
            self.filter_buttons[category] = control
            filters.add_widget(control)
        self.content.add_widget(filters)
        self.results = Stack(spacing=dp(14))
        self.content.add_widget(self.results)
        self.set_category(self.category)

    def set_category(self, category):
        app = App.get_running_app()
        t = app.tr
        self.category = category
        self.results.clear_widgets()
        for name, control in self.filter_buttons.items():
            control.kind = "primary" if category == name else "secondary"
        for guide in GUIDES:
            if category != "All" and category != guide["category"]:
                continue
            panel = card(t(guide["title"]), t(guide["summary"]), t(guide["category"]))
            panel.add_widget(button(t("Read guide"), lambda key=guide["id"]: app.open_guide(key), "secondary", icon="book"))
            self.results.add_widget(panel)


class LessonScreen(Page):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.guide_id = None
        self.render()

    def render(self):
        app = App.get_running_app()
        t = app.tr
        self.content.clear_widgets()
        guide = get_guide(self.guide_id)
        if not guide:
            self.title(t("Guide unavailable"), t("Choose a guide from the reading library."))
            return
        self.title(t(guide["title"]), t(guide["intro"]), "library")
        for index, step in enumerate(guide["steps"], 1):
            self.content.add_widget(card(t("Step {number}", number=index), t(step)))
        self.content.add_widget(card(t("Keep in mind"), t(guide["tip"]), icon="check"))
        self.content.add_widget(Copy(text=t("Further reading: {publisher}", publisher=guide["publisher"]), base_size=12, tone="muted"))
        self.content.add_widget(button(t("Learn more"), lambda: app.open_link(guide["url"]), "secondary", icon="chevron"))
        self.content.add_widget(button(t("Back to guides"), app.go_back, "ghost", icon="back"))
