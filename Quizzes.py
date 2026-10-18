"""Bilingual, self-paced practice; changing language preserves answer identity."""

from kivy.app import App

from content import QUESTIONS
from core import QuizSession
from ui import Copy, Page, button, card


class StartQuizScreen(Page):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.render()

    def render(self):
        app = App.get_running_app()
        t = app.tr
        self.content.clear_widgets()
        self.title(t("A little practice."), t("8 questions. No timer."), "quiz")
        self.content.add_widget(card(t("Practice"), t("Choose an answer, read why, then continue when you are ready."), icon="check"))
        active = app.manager.get_screen("quiz").session if app.manager.has_screen("quiz") else None
        self.content.add_widget(button(t("Continue practice" if active and not active.complete else "Start practice"), self.start, icon="play"))
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

    def begin(self):
        self.session = QuizSession(QUESTIONS)
        self.render()

    def on_pre_enter(self, *_):
        if self.session is None:
            self.begin()
        else:
            self.render()

    def render(self):
        app = App.get_running_app()
        t = app.tr
        self.content.clear_widgets()
        self.answer_buttons = []
        self.to_top()
        session = self.session
        if session is None:
            self.title(t("A little practice."), icon="quiz")
            return
        if session.complete:
            self.show_summary()
            return
        question = session.question
        self.content.add_widget(Copy(text=t("Question {number} of {total}", number=session.index + 1, total=len(session.questions)), base_size=12, tone="accent"))
        self.title(t(question["question"]), t("Choose one answer."))
        for index, choice in enumerate(question["choices"]):
            control = button(f"{chr(65 + index)}.  {t(choice)}", lambda idx=index: self.check_answer(idx), "secondary", base_size=15, min_height=58)
            self.answer_buttons.append(control)
            self.content.add_widget(control)
        if session.selected is not None:
            self.show_feedback()

    def check_answer(self, selected_index):
        result = self.session.submit(selected_index)
        if result is None:
            return
        App.get_running_app().play_sound("right" if result else "wrong")
        self.show_feedback()

    def show_feedback(self):
        t = App.get_running_app().tr
        session = self.session
        correct = session.question["answer"]
        for index, control in enumerate(self.answer_buttons):
            control.disabled = True
            if index == correct:
                control.text = t("Correct answer: {answer}", answer=t(session.question["choices"][index]))
                control.kind = "primary"
            elif index == session.selected:
                control.text = t("Your choice: {answer}", answer=t(session.question["choices"][index]))
        self.content.add_widget(card(t("Well done!" if session.selected == correct else "Let's learn from this."), t(session.question["explanation"]), t("Why?"), icon="check"))
        self.content.add_widget(button(t("See results" if session.index == len(session.questions) - 1 else "Next question"), self.next_question, icon="chevron"))

    def next_question(self):
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
        self.title(t("Practice complete"), icon="check")
        self.content.add_widget(card(t("{score} out of {total}", score=session.score, total=len(session.questions)), t("Every question is a chance to learn. Try again whenever you like.")))
        self.content.add_widget(button(t("Try again"), self.begin, icon="quiz"))
        self.content.add_widget(button(t("Return home"), lambda: app.navigate("main", section=True), "secondary", icon="home"))
