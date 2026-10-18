"""The original two-column quiz flow, adapted for the bilingual mobile app."""

from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout

from content import QUESTIONS
from core import QuizSession
from ui import Action, Copy, Page, button, card, horizontal


class QuizAnswer(Action):
    feedback = StringProperty("")


class StartQuizScreen(Page):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.render()

    def render(self):
        app = App.get_running_app()
        t = app.tr
        self.content.clear_widgets()
        self.title(t("QUIZ ME!"), t("8 situational questions. No timer to choose an answer."), "quiz")
        self.content.add_widget(card(t("Test your digital literacy"), t("Answer each situation based on your understanding. Your score appears at the end.")))
        active = app.manager.get_screen("quiz").session if app.manager.has_screen("quiz") else None
        self.content.add_widget(button(t("Continue quiz" if active and not active.complete else "Start Quiz"), self.start, icon="play"))
        self.content.add_widget(card(t("How to play"), t('1. Tap "Start Quiz".\n\n2. Choose an answer. Green means correct; red means incorrect.\n\n3. The next question appears automatically after a short pause. Keep answering until your score appears.')))
        self.content.add_widget(Copy(text=t("An unfinished session stays available while the app is open. Completed scores are saved."), base_size=12, tone="muted"))

    def start(self):
        app = App.get_running_app()
        quiz = app.manager.get_screen("quiz")
        if quiz.session is None or quiz.session.complete:
            quiz.begin()
        app.navigate("quiz")


class QuizScreen(Page):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.session = None
        self.answer_buttons = []
        self._advance_event = None
        self._backgrounded = False

    def begin(self):
        self.pause_feedback()
        self.session = QuizSession(QUESTIONS)
        self.render()

    def on_pre_enter(self, *_):
        if self.session is None:
            self.begin()
        else:
            self.render()
        self.resume_feedback()

    def on_pre_leave(self, *_):
        self.pause_feedback()

    def pause_feedback(self):
        if self._advance_event is not None:
            self._advance_event.cancel()
            self._advance_event = None

    def resume_feedback(self):
        app = App.get_running_app()
        if (self._advance_event is None and self.session is not None
                and not self.session.complete and self.session.selected is not None
                and self.manager and self.manager.current == self.name
                and not self._backgrounded and not app.root.menu_open):
            self._advance_event = Clock.schedule_once(self._auto_advance, 1)

    def _auto_advance(self, _dt):
        self._advance_event = None
        if (self.manager.current == self.name and not self._backgrounded
                and not App.get_running_app().root.menu_open):
            self.next_question()

    def render(self):
        app = App.get_running_app()
        t = app.tr
        self.content.clear_widgets()
        self.answer_buttons = []
        self.to_top()
        session = self.session
        if session is None:
            self.title(t("QUIZ ME!"), icon="quiz")
            return
        if session.complete:
            self.show_summary()
            return
        question = session.question
        self.content.add_widget(Copy(text=t("Question {number} of {total}", number=session.index + 1, total=len(session.questions)), base_size=12, tone="accent"))
        self.content.add_widget(Copy(text=t(question["topic"]), base_size=20, heading=True, halign="center"))
        self.content.add_widget(Copy(text=t(question["question"]), base_size=16, halign="center"))
        self.content.add_widget(Copy(text=t("Choose one answer."), base_size=12, tone="muted", halign="center"))
        self.answer_grid = GridLayout(cols=2, spacing=dp(10), size_hint_y=None)
        self.answer_grid.bind(minimum_height=self.answer_grid.setter("height"))
        for index, choice in enumerate(question["choices"]):
            control = QuizAnswer(text=f"{chr(65 + index)}.  {t(choice)}", kind="secondary",
                                 base_size=14, min_height=84, text_padding=20)
            control.bind(on_release=lambda _button, idx=index: self.check_answer(idx))
            self.answer_buttons.append(control)
            self.answer_grid.add_widget(control)
        self.content.add_widget(self.answer_grid)
        if session.selected is not None:
            self.show_feedback()

    def check_answer(self, selected_index):
        result = self.session.submit(selected_index)
        if result is None:
            return
        App.get_running_app().play_sound("right" if result else "wrong")
        self.show_feedback()
        self.resume_feedback()

    def show_feedback(self):
        t = App.get_running_app().tr
        session = self.session
        correct = session.question["answer"]
        for index, control in enumerate(self.answer_buttons):
            control.disabled = True
            if index == correct:
                control.text = t("Correct answer: {answer}", answer=t(session.question["choices"][index]))
                control.feedback = "correct"
            elif index == session.selected:
                control.text = t("Your choice: {answer}", answer=t(session.question["choices"][index]))
                control.feedback = "incorrect"
        self.content.add_widget(Copy(text=t("Correct!" if session.selected == correct else "Incorrect. The correct answer is shown in green."), base_size=14, halign="center"))

    def next_question(self):
        self.pause_feedback()
        if self.session.advance():
            self.render()

    def show_summary(self):
        app = App.get_running_app()
        t = app.tr
        session = self.session
        if not session.recorded:
            saved = app.store.record_quiz(session.score, len(session.questions))
            session.recorded = True
            if not saved:
                app.notice("Score could not be saved", "Your result is shown here, but the device could not save it. Check available storage.")
        self.title(t("Quiz complete"), icon="check")
        self.content.add_widget(card(t("You answered {score} out of {total} correctly!", score=session.score, total=len(session.questions)), t("Do you want to try again?")))
        self.content.add_widget(horizontal(
            button(t("Yes"), self.begin),
            button(t("No"), lambda: app.navigate("start", section=True), "secondary")))
