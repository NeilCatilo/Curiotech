import json
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path

from content import ARTICLES, QUESTIONS, TERMS, VIDEOS
from core import DEFAULT_STATE, LocalStore, NavigationHistory, QuizSession, search_terms


class QuizTests(unittest.TestCase):
    def test_repeated_taps_cannot_score_twice(self):
        quiz = QuizSession(QUESTIONS, seed=1)
        self.assertTrue(quiz.submit(quiz.question['answer']))
        for _ in range(20):
            self.assertIsNone(quiz.submit(0))
        self.assertEqual((quiz.score, quiz.index), (1, 0))

    def test_requires_answer_before_advance(self):
        quiz = QuizSession(QUESTIONS)
        self.assertFalse(quiz.advance())
        self.assertEqual(quiz.index, 0)

    def test_full_perfect_quiz_and_finished_guard(self):
        quiz = QuizSession(QUESTIONS, seed=4)
        for _ in QUESTIONS:
            self.assertTrue(quiz.submit(quiz.question['answer']))
            self.assertTrue(quiz.advance())
        self.assertTrue(quiz.complete)
        self.assertIsNone(quiz.question)
        self.assertIsNone(quiz.submit(0))
        self.assertFalse(quiz.advance())
        self.assertEqual(quiz.score, len(QUESTIONS))

    def test_wrong_answer_scores_zero(self):
        quiz = QuizSession(QUESTIONS)
        self.assertFalse(quiz.submit((quiz.question['answer'] + 1) % 4))
        self.assertEqual(quiz.score, 0)

    def test_shuffle_preserves_answer_identity_and_source(self):
        original = deepcopy(QUESTIONS)
        expected = {q['topic']: q['choices'][q['answer']] for q in QUESTIONS}
        for seed in range(20):
            for q in QuizSession(QUESTIONS, seed).questions:
                self.assertEqual(q['choices'][q['answer']], expected[q['topic']])
        self.assertEqual(QUESTIONS, original)

    def test_invalid_choice_is_rejected(self):
        quiz = QuizSession(QUESTIONS)
        for value in (-1, 4, '0', True):
            with self.assertRaises(ValueError):
                quiz.submit(value)

    def test_empty_quiz_is_rejected(self):
        with self.assertRaises(ValueError):
            QuizSession([])


class NavigationTests(unittest.TestCase):
    def test_home_does_not_reopen_previous_screen(self):
        nav = NavigationHistory()
        nav.go('dictionary')
        nav.go('main')
        self.assertEqual(nav.back(), 'main')

    def test_back_returns_to_parent(self):
        nav = NavigationHistory()
        nav.go('start', section=True)
        nav.go('quiz')
        self.assertEqual(nav.back(), 'start')
        self.assertEqual(nav.back(), 'main')

    def test_section_navigation_clears_old_history(self):
        nav = NavigationHistory()
        nav.go('Article')
        nav.go('video')
        nav.go('dictionary', section=True)
        self.assertEqual(nav.back(), 'main')

    def test_revisits_are_kept_in_order(self):
        nav = NavigationHistory()
        for destination in ['Article', 'video', 'Article', 'video']:
            nav.go(destination)
        self.assertEqual([nav.back(), nav.back(), nav.back()], ['Article', 'video', 'Article'])


class PersistenceTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.path = Path(self.folder.name) / 'learning.json'
        self.addCleanup(self.folder.cleanup)

    def test_defaults_and_round_trip(self):
        store = LocalStore(self.path)
        self.assertEqual(store.data, DEFAULT_STATE)
        store.data['settings']['dark'] = True
        self.assertTrue(store.save())
        self.assertTrue(LocalStore(self.path).data['settings']['dark'])
        self.assertFalse(self.path.with_suffix('.tmp').exists())

    def test_corrupt_json_recovers(self):
        self.path.write_text('{broken', encoding='utf-8')
        store = LocalStore(self.path)
        self.assertEqual(store.data, DEFAULT_STATE)
        self.assertIsNotNone(store.last_error)
        self.assertTrue(store.save())

    def test_invalid_preference_types_are_ignored(self):
        self.path.write_text(json.dumps({'settings': {'dark': 'yes', 'sound': True}, 'progress': {'completed': -3, 'best_score': 900}}))
        store = LocalStore(self.path)
        self.assertFalse(store.data['settings']['dark'])
        self.assertTrue(store.data['settings']['sound'])
        self.assertEqual(store.data['progress']['completed'], 0)
        self.assertEqual(store.data['progress']['best_score'], 100)

    def test_unexpected_shapes_recover(self):
        for raw in ([], None, {'settings': None}, {'progress': []}):
            self.path.write_text(json.dumps(raw))
            self.assertEqual(LocalStore(self.path).data, DEFAULT_STATE)

    def test_score_tracking_and_validation(self):
        store = LocalStore(self.path)
        self.assertTrue(store.record_quiz(6, 8))
        self.assertTrue(store.record_quiz(3, 8))
        progress = LocalStore(self.path).data['progress']
        self.assertEqual(progress['completed'], 2)
        self.assertEqual(progress['best_score'], 75)
        self.assertEqual(progress['last_score'], 3)
        for score, total in ((1, 0), (-1, 8), (9, 8)):
            with self.assertRaises(ValueError):
                store.record_quiz(score, total)

    def test_write_failure_is_reported(self):
        parent_file = Path(self.folder.name) / 'not_a_folder'
        parent_file.write_text('test')
        store = LocalStore(parent_file / 'state.json')
        self.assertFalse(store.save())
        self.assertIsNotNone(store.last_error)


class ContentTests(unittest.TestCase):
    def test_casefold_whitespace_meaning_and_filters(self):
        self.assertEqual(search_terms(TERMS, '  brB  ')[0]['term'], 'BRB')
        self.assertIn('Phishing', [e['term'] for e in search_terms(TERMS, 'steal')])
        self.assertEqual(search_terms(TERMS, 'BRB', 'Slang'), [])
        self.assertEqual(search_terms(TERMS, 'notaword'), [])

    def test_no_duplicate_terms(self):
        words = [entry['term'].casefold() for entry in TERMS]
        self.assertEqual(len(words), len(set(words)))

    def test_questions_are_unambiguous_in_structure(self):
        for question in QUESTIONS:
            self.assertEqual(len(question['choices']), 4)
            self.assertEqual(len(set(question['choices'])), 4)
            self.assertTrue(0 <= question['answer'] < 4)
            self.assertTrue(question['explanation'])

    def test_external_resources_use_https(self):
        for article in ARTICLES:
            self.assertTrue(article[-1].startswith('https://'))
        for video in VIDEOS:
            self.assertEqual(len(video[3]), 11)


if __name__ == '__main__':
    unittest.main()
