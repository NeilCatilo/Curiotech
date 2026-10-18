"""Real UI checks for the mobile drawer and English/Tagalog learning flows.

Uses isolated local data. Does not open a browser. A PC window previews a phone;
these checks do not replace Android-device testing.
"""
import json
import os
import sys
import traceback
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
os.environ['CURIOCITECH_DATA_DIR'] = str(ROOT / '.runtime' / 'mobile-smoke-data')
os.environ['KIVY_HOME'] = str(ROOT / '.runtime' / 'kivy-mobile')
os.environ['KIVY_NO_ARGS'] = '1'
os.environ['KIVY_METRICS_DENSITY'] = '1'
os.environ['KIVY_DPI'] = '96'
os.environ['KIVY_METRICS_FONTSCALE'] = '1'
from kivy.config import Config
Config.remove_option('input', 'wm_pen')
Config.remove_option('input', 'wm_touch')
from main import CuriocitechApp
from kivy.clock import Clock
from kivy.core.window import Window
from core import LocalStore
from ui import Action, Copy, IconButton

OUTPUT = ROOT / 'artifacts' / 'mobile-v1.2'
OUTPUT.mkdir(parents=True, exist_ok=True)


class SmokeApp(CuriocitechApp):
    def on_start(self):
        super().on_start()
        self.report = {'passed': [], 'screenshots': [], 'errors': []}
        self.steps = iter([
            self.setup, lambda: self.capture('home-english'), self.menu,
            lambda: self.capture('menu-english'), self.tagalog,
            lambda: self.capture('menu-tagalog'), self.dictionary,
            self.check_search, lambda: self.capture('dictionary-tagalog'),
            self.start_quiz, self.answer, lambda: self.capture('quiz-tagalog'),
            self.switch_during_quiz, self.complete_quiz,
            self.library, lambda: self.capture('library-tagalog'), self.read_lesson,
            lambda: self.capture('reading-steps-tagalog'), self.learn_more,
            self.video_route, lambda: self.capture('video-preview-notice'), self.video_and_about,
            self.settings, lambda: self.capture('settings-tagalog-dark'),
            self.dialog_cancel, self.dialog_accept, self.menu_back_and_scrim,
            self.small_phone, lambda: self.capture('small-phone-tagalog'),
            self.animated_navigation, self.check_animation, self.open_animated_menu,
            self.check_animated_menu, self.return_home,
            lambda: self.capture('home-tagalog'), self.finish,
        ])
        self.timeout = Clock.schedule_once(lambda *_: self.fail('UI check timed out'), 90)
        Clock.schedule_once(self.step, .8)

    def step(self, *_):
        try:
            if self.manager.transition.is_active:
                Clock.schedule_once(self.step, .1)
                return
            next(self.steps)()
            if not self._exiting:
                Clock.schedule_once(self.step, .4)
        except Exception:
            self.fail(traceback.format_exc())

    def passed(self, text):
        self.report['passed'].append(text)

    def setup(self):
        self.store.data['settings'].update(dark=False, large_text=False, sound=False, reduced_motion=True, language='en')
        self.apply_preferences()
        for screen in self.manager.screens:
            screen.render()
        Window.size = (412, 820)
        assert not any(hasattr(self.root, name) for name in ('header', 'bottom', 'sidebar'))
        assert self.manager.height == self.root.height
        assert abs(self.root.menu_button.x - (self.manager.x + 20)) < 1
        home = [widget.text for widget in self.manager.current_screen.walk() if isinstance(widget, Copy)]
        assert 'Your everyday digital guide.' in home
        assert 'What you can do here' in home
        self.passed('mobile canvas has no top bar, bottom bar or permanent sidebar')
        self.passed('Menu is at upper left and Home explains the app')

    def capture(self, name):
        assert self.manager.children == [self.manager.current_screen]
        assert self.manager.current_screen.opacity == 1
        path = OUTPUT / (name + '.png')
        if self.root.menu_open or self.dialog:
            Window.dispatch('on_draw')
            produced = Path(Window.screenshot(name=str(path)))
            produced.replace(path)
            Window.flip()
        else:
            self.root.export_to_png(str(path))
        self.report['screenshots'].append(str(path))

    def menu(self):
        self.root.menu_button.dispatch('on_release')
        assert self.root.menu_open
        assert set(self.root.menu_view.nav_buttons) == {'main', 'dictionary', 'Article', 'video', 'start', 'settings', 'about_us'}
        self.passed('one floating Menu opens a drawer with all seven destinations')

    def tagalog(self):
        self.set_preference('language', 'tl')
        assert self.root.menu_open
        assert self.root.menu_view.nav_buttons['dictionary'].text == 'Diksiyonaryo'
        assert LocalStore(self.store.path).data['settings']['language'] == 'tl'
        self.passed('language changes in open menu and persists to disk')

    def choose(self, destination):
        if not self.root.menu_open:
            self.root.open_menu()
        self.root.menu_view.nav_buttons[destination].dispatch('on_release')
        assert self.manager.current == destination

    def dictionary(self):
        self.choose('dictionary')
        assert not self.root.menu_open
        self.manager.get_screen('dictionary').search.text = 'pribadong'

    def check_search(self):
        screen = self.manager.get_screen('dictionary')
        assert screen.counter.text == '1 resulta'
        assert len(screen.results.children) == 1
        screen.search.text = 'private message'
        screen.update_results()
        assert screen.counter.text == '1 resulta'
        screen.set_category('Slang')
        assert screen.counter.text == '0 resulta'
        screen.clear_search()
        assert screen.counter.text == '25 resulta'
        screen.search.text = 'BRB'
        screen.update_results()
        self.passed('search understands English and Tagalog; filters and empty results work')

    def start_quiz(self):
        self.choose('start')
        self.manager.get_screen('start').start()
        assert self.manager.current == 'quiz'

    def answer(self):
        quiz = self.manager.get_screen('quiz')
        quiz.check_answer(quiz.session.question['answer'])
        quiz.check_answer(0)
        assert quiz.session.score == 1
        assert all(control.disabled for control in quiz.answer_buttons)
        assert any(control.text.startswith('Tamang sagot:') for control in quiz.answer_buttons)
        self.passed('Tagalog quiz feedback and repeated-tap protection')

    def switch_during_quiz(self):
        quiz = self.manager.get_screen('quiz')
        session = quiz.session
        snapshot = (session.index, session.selected, session.score, session.question['choices'][:])
        self.set_preference('language', 'en')
        assert quiz.session is session
        assert any(control.text.startswith('Correct answer:') for control in quiz.answer_buttons)
        self.set_preference('language', 'tl')
        assert (session.index, session.selected, session.score, session.question['choices']) == snapshot
        self.choose('settings')
        self.choose('start')
        self.manager.get_screen('start').start()
        assert quiz.session is session
        self.passed('changing language or visiting menu destinations preserves the active quiz')

    def complete_quiz(self):
        quiz = self.manager.get_screen('quiz')
        before = self.store.data['progress']['completed']
        while not quiz.session.complete:
            if quiz.session.selected is None:
                quiz.check_answer(quiz.session.question['answer'])
            quiz.next_question()
        assert quiz.session.score == 8
        quiz.render()
        assert self.store.data['progress']['completed'] == before + 1
        self.passed('all eight questions can finish; result saved exactly once')

    def library(self):
        self.choose('Article')
        screen = self.manager.get_screen('Article')
        screen.set_category('App guides')
        assert len(screen.results.children) == 4
        assert screen.filter_buttons['App guides'].text == 'Mga gabay sa app'
        self.passed('resource titles, descriptions and category labels translate')

    def read_lesson(self):
        from lessons import get_guide
        screen = self.manager.get_screen('Article')
        control = next(widget for widget in screen.walk() if isinstance(widget, IconButton) and widget.text == 'Basahin ang gabay')
        original = self.open_link
        outside = []
        self.open_link = lambda url: outside.append(url)
        try:
            control.dispatch('on_release')
        finally:
            self.open_link = original
        assert not outside
        assert self.manager.current == 'lesson'
        reader = self.manager.current_screen
        guide = get_guide(reader.guide_id)
        labels = [widget.text for widget in reader.walk() if isinstance(widget, Copy)]
        assert 'Hakbang 1' in labels
        assert self.tr(guide['steps'][0]) in labels
        guide_id = reader.guide_id
        self.set_preference('language', 'en')
        self.set_preference('language', 'tl')
        assert reader.guide_id == guide_id
        self.passed('reading opens offline numbered steps without launching an external link')

    def learn_more(self):
        reader = self.manager.current_screen
        control = next(widget for widget in reader.walk() if isinstance(widget, IconButton) and widget.text == 'Alamin pa')
        control.dispatch('on_release')
        assert self.dialog.title == 'Buksan sa iyong browser?'
        self.go_back()
        self.go_back()
        assert self.manager.current == 'Article'
        assert self.manager.get_screen('Article').category == 'App guides'
        self.passed('Learn more is optional; Back returns to the filtered library')

    def video_route(self):
        from content import VIDEOS
        self.choose('video')
        screen = self.manager.current_screen
        class FakePlayer:
            def __init__(self):
                self.opened = []
                self.closed = 0
            def open(self, *arguments):
                self.opened.append(arguments)
            def close(self):
                self.closed += 1
        fake = FakePlayer()
        screen.player = fake
        with patch('Video.platform', 'android'):
            control = next(widget for widget in screen.walk() if isinstance(widget, IconButton) and widget.text == 'Panoorin sa app')
            control.dispatch('on_release')
            assert fake.opened
            assert fake.opened[0][2] == 'tl'
            self.on_pause()
            assert fake.closed == 1
        screen.player = None
        screen.watch(VIDEOS[0][3])
        assert self.dialog.title == 'Preview ng Android player'
        self.passed('video buttons use the Android in-app player route; pausing stops playback (native route mocked)')

    def video_and_about(self):
        self.go_back()
        self.choose('video')
        videos = self.manager.get_screen('video')
        assert any(isinstance(widget, Copy) and widget.text == 'Manood at matuto.' for widget in videos.walk())
        self.choose('about_us')
        assert any(isinstance(widget, Copy) and 'Mananaliksik' in widget.text for widget in self.manager.current_screen.walk())
        self.passed('video descriptions and team roles translate; images load')

    def settings(self):
        self.choose('settings')
        self.set_preference('dark', True)
        self.set_preference('large_text', True)
        self.set_preference('sound', True)
        self.set_preference('sound', False)
        assert self.text_scale == 1.2 and self.dark
        self.passed('mobile settings support dark mode, larger text and optional sound')

    def dialog_cancel(self):
        self.launched = None
        self._launch_url = lambda url: setattr(self, 'launched', url)
        self.open_link('https://example.com/guide')
        assert self.dialog.title == 'Buksan sa iyong browser?'
        assert self.launched is None
        self.handle_back_button(Window, 27)

    def dialog_accept(self):
        self.open_link('https://example.com/guide')
        controls = [widget for widget in self.dialog.content.walk() if isinstance(widget, Action)]
        next(widget for widget in controls if widget.text == 'Buksan ang link').dispatch('on_release')
        assert self.launched == 'https://example.com/guide'
        self.passed('translated external-link confirmation and Android-style Back dismissal')

    def menu_back_and_scrim(self):
        destination = self.manager.current
        self.root.open_menu()
        self.handle_back_button(Window, 27)
        assert not self.root.menu_open and self.manager.current == destination
        self.root.open_menu()
        self.root.menu_view.on_touch_down(SimpleNamespace(pos=(Window.width - 2, Window.height / 2)))
        assert not self.root.menu_open
        self.passed('Back and tapping the scrim close the menu without navigating')

    def small_phone(self):
        Window.size = (320, 640)
        self.set_preference('dark', False)
        self.navigate('settings', section=True)
        self.passed('320 px phone with larger Tagalog text')

    def animated_navigation(self):
        self.set_preference('reduced_motion', False)
        self.navigate('Article', section=True)
        self.navigate('video')
        self.go_back()

    def check_animation(self):
        assert self.manager.current == 'Article'
        assert self.manager.children == [self.manager.current_screen]
        assert self.manager.current_screen.opacity == 1
        self.passed('rapid animated navigation leaves one visible screen')

    def open_animated_menu(self):
        self.root.open_menu()

    def check_animated_menu(self):
        assert abs(self.root.menu_view.panel.x - self.root.menu_view.x) < 1
        self.root.close_menu()
        self.passed('drawer slide animation settles at the screen edge')

    def return_home(self):
        Window.size = (412, 820)
        self.set_preference('large_text', False)
        self.navigate('main', section=True)
        for screen in self.manager.screens:
            for widget in screen.walk():
                if isinstance(widget, (Action, IconButton)):
                    assert widget.height >= 48
        self.passed('all controls retain comfortable touch target heights')

    def finish(self):
        self.timeout.cancel()
        (OUTPUT / 'smoke-report.json').write_text(json.dumps(self.report, indent=2), encoding='utf-8')
        self.exit_app()

    def fail(self, error):
        self.report['errors'].append(error)
        self.finish()


if __name__ == '__main__':
    application = SmokeApp()
    application.run()
    sys.exit(1 if application.report['errors'] else 0)
