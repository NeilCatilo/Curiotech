"""Bilingual dictionary search with stable category IDs."""

from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.textinput import TextInput

from core import search_terms
from i18n import localized_terms
from ui import AdaptiveGrid, Copy, Page, Stack, button, card


class DictionaryScreen(Page):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.category = "All"
        self.search = None
        self._search_event = Clock.create_trigger(self.update_results, .12)
        self.render()

    def render(self):
        app = App.get_running_app()
        t = app.tr
        query = self.search.text if self.search else ""
        if self.search:
            self.search.focus = False
        self.content.clear_widgets()
        self.title(t("Words made simple."), t("Find a word or browse a category."), "book")
        self.search = TextInput(text=query, multiline=False, hint_text=t("Search words or meanings"),
                                size_hint_y=None, height=dp(64), write_tab=False)
        self.search.bind(text=lambda *_: self._search_event(), on_text_validate=lambda *_: self.update_results())
        self.content.add_widget(self.search)
        self.filters = AdaptiveGrid()
        self.filter_buttons = {}
        for category in ("All", "Technology", "Abbreviations", "Slang"):
            control = button(t(category), lambda value=category: self.set_category(value), "secondary", base_size=13)
            self.filter_buttons[category] = control
            self.filters.add_widget(control)
        self.content.add_widget(self.filters)
        self.counter = Copy(base_size=12, tone="muted")
        self.content.add_widget(self.counter)
        self.results = Stack(spacing=dp(12))
        self.content.add_widget(self.results)
        self.update_results()

    def set_category(self, category):
        self.category = category
        self.update_results()

    def update_results(self, *_):
        app = App.get_running_app()
        t = app.tr
        entries = search_terms(localized_terms(app.language), self.search.text, self.category)
        self.results.clear_widgets()
        for category, control in self.filter_buttons.items():
            control.active = category == self.category
            control.kind = "primary" if control.active else "secondary"
        self.counter.text = t("{count} results", count=len(entries))
        for entry in entries:
            self.results.add_widget(card(entry["term"], entry["meaning"], t(entry["category"])))
        if not entries:
            self.results.add_widget(card(t("No matching words"), t("Try another word or choose All.")))
            self.results.add_widget(button(t("Clear search"), self.clear_search, "secondary"))

    def clear_search(self):
        self.search.text = ""
        self.category = "All"
        self.update_results()

    def on_leave(self, *_):
        self.search.focus = False
        self._search_event.cancel()
