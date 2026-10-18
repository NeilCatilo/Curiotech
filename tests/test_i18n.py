import json
import tempfile
import unittest
from pathlib import Path
from string import Formatter

from content import ARTICLES, QUESTIONS, TEAM, TERMS, VIDEOS
from core import LocalStore, QuizSession, search_terms
from i18n import TRANSLATIONS, localized_terms, translate


class LanguageTests(unittest.TestCase):
    def test_english_and_tagalog_labels(self):
        self.assertEqual(translate('Dictionary', 'en'), 'Dictionary')
        self.assertEqual(translate('Dictionary', 'tl'), 'Diksiyonaryo')

    def test_all_definitions_are_translated(self):
        for entry in TERMS:
            self.assertIn(entry['meaning'], TRANSLATIONS)
            self.assertNotEqual(translate(entry['meaning'], 'tl'), entry['meaning'])

    def test_every_question_choice_and_explanation_is_translated(self):
        for question in QUESTIONS:
            for text in [question['topic'], question['question'], question['explanation'], *question['choices']]:
                self.assertIn(text, TRANSLATIONS)
                self.assertNotEqual(translate(text, 'tl'), text)

    def test_resource_descriptions_and_roles_are_translated(self):
        for _, title, description, *_ in ARTICLES + VIDEOS:
            self.assertIn(title, TRANSLATIONS)
            self.assertIn(description, TRANSLATIONS)
        for _, role, _ in TEAM:
            self.assertIn(role, TRANSLATIONS)

    def test_format_placeholders_match_in_both_languages(self):
        formatter = Formatter()
        for english, tagalog in TRANSLATIONS.items():
            en = {field for _, field, _, _ in formatter.parse(english) if field}
            tl = {field for _, field, _, _ in formatter.parse(tagalog) if field}
            self.assertEqual(en, tl, english)
        self.assertEqual(translate('Question {number} of {total}', 'tl', number=2, total=8), 'Tanong 2 sa 8')

    def test_search_accepts_either_language(self):
        for language in ('en', 'tl'):
            entries = localized_terms(language)
            self.assertEqual(search_terms(entries, 'pribadong')[0]['term'], 'DM')
            self.assertEqual(search_terms(entries, 'private message')[0]['term'], 'DM')
            self.assertEqual(search_terms(entries, 'pribadong', 'Slang'), [])

    def test_translation_does_not_change_quiz_answer_order(self):
        session = QuizSession(QUESTIONS, seed=7)
        choices = session.question['choices'][:]
        translated = [translate(choice, 'tl') for choice in choices]
        self.assertEqual(len(set(translated)), 4)
        self.assertEqual(session.question['choices'], choices)
        self.assertTrue(session.submit(session.question['answer']))
        self.assertIsNone(session.submit(0))

    def test_language_persistence_and_migration(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'learning.json'
            path.write_text(json.dumps({'settings': {'dark': True}}))
            store = LocalStore(path)
            self.assertEqual(store.data['settings']['language'], 'en')
            self.assertTrue(store.data['settings']['dark'])
            store.data['settings']['language'] = 'tl'
            self.assertTrue(store.save())
            self.assertEqual(LocalStore(path).data['settings']['language'], 'tl')
            for invalid in ('xx', True, 1, None, []):
                path.write_text(json.dumps({'settings': {'language': invalid}}))
                self.assertEqual(LocalStore(path).data['settings']['language'], 'en')


if __name__ == '__main__':
    unittest.main()
