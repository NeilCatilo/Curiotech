import configparser
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

from content import ARTICLES, VIDEOS
from core import VERSION
from i18n import TRANSLATIONS, translate
from lessons import GUIDES, get_guide
from player import AndroidYouTubePlayer, app_origin, build_player_html, validate_video_id


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.tags = []
        self.feed(text)

    def handle_starttag(self, tag, attributes):
        self.tags.append((tag, dict(attributes)))


class ReadingTests(unittest.TestCase):
    def test_every_catalogue_entry_has_a_local_guide(self):
        self.assertEqual({guide['title'] for guide in GUIDES}, {article[1] for article in ARTICLES})
        self.assertEqual(len({guide['id'] for guide in GUIDES}), len(GUIDES))

    def test_guides_have_real_bilingual_steps(self):
        for guide in GUIDES:
            self.assertGreaterEqual(len(guide['steps']), 3)
            for text in [guide['intro'], guide['tip'], *guide['steps']]:
                self.assertTrue(text.strip())
                self.assertIn(text, TRANSLATIONS)
                self.assertNotEqual(translate(text, 'tl'), text)

    def test_lookup_and_optional_https_sources(self):
        self.assertIsNone(get_guide('unknown'))
        for guide in GUIDES:
            self.assertIs(get_guide(guide['id']), guide)
            self.assertEqual(urlsplit(guide['url']).scheme, 'https')
            self.assertTrue(guide['publisher'])


class EmbedTests(unittest.TestCase):
    def document(self, **kwargs):
        return build_player_html(VIDEOS[0][3], 'org.example.MyApp', 'A useful video', **kwargs)

    def test_real_app_identity_and_interactive_playback(self):
        document = Document(self.document())
        iframe = next(attributes for tag, attributes in document.tags if tag == 'iframe')
        address = urlsplit(iframe['src'])
        self.assertEqual(address.hostname, 'www.youtube-nocookie.com')
        parameters = parse_qs(address.query)
        self.assertEqual(parameters['origin'], ['https://org.example.myapp'])
        self.assertEqual(parameters['autoplay'], ['0'])
        self.assertEqual(parameters['controls'], ['1'])
        self.assertEqual(parameters['enablejsapi'], ['1'])
        self.assertEqual(iframe['referrerpolicy'], 'strict-origin-when-cross-origin')
        self.assertIn('allowfullscreen', iframe)

    def test_invalid_ids_and_origins_are_rejected(self):
        for invalid in ('bad', '../abcdefgh', 'abcdefghij<', None, 123):
            with self.assertRaises(ValueError):
                validate_video_id(invalid)
        for invalid in ('https://example.com', 'app', 'org.example/evil', 'org.example"', None):
            with self.assertRaises(ValueError):
                app_origin(invalid)

    def test_existing_video_ids_are_valid(self):
        for video in VIDEOS:
            self.assertEqual(validate_video_id(video[3]), video[3])

    def test_title_is_escaped_and_scripts_have_a_nonce(self):
        text = build_player_html(VIDEOS[0][3], 'org.example.app', '<script>alert("x")</script>')
        self.assertNotIn('<script>alert', text)
        self.assertIn('&lt;script&gt;', text)
        document = Document(text)
        inline = [attributes for tag, attributes in document.tags if tag == 'script']
        self.assertTrue(inline[0]['nonce'])
        self.assertIn("script-src 'nonce-", text)

    def test_tagalog_status_and_errors_are_present(self):
        text = self.document(language='tl', dark=True)
        self.assertIn('lang="tl"', text)
        self.assertIn('Nilo-load ang video', text)
        self.assertIn('hl=tl', text)
        self.assertIn('101,150', text)
        self.assertIn('event.data===153', text)
        self.assertIn('min-height:200px', text)
        self.assertIn('setTimeout', text)

    def test_bridge_uses_runtime_package_and_localised_controls(self):
        calls = []
        class Native:
            @staticmethod
            def show(*arguments):
                calls.append(arguments)
            @staticmethod
            def close():
                calls.append('closed')
        activity = SimpleNamespace(getPackageName=lambda: 'ph.example.RealApplication')
        def autoclass(name):
            if name == 'org.kivy.android.PythonActivity':
                return SimpleNamespace(mActivity=activity)
            self.assertEqual(name, 'org.curiocitech.player.VideoPlayer')
            return Native
        with patch.dict(sys.modules, {'jnius': SimpleNamespace(autoclass=autoclass)}):
            bridge = AndroidYouTubePlayer()
            bridge.open(VIDEOS[0][3], 'Kaligtasan', 'tl', True)
            arguments = calls[0]
            self.assertIs(arguments[0], activity)
            self.assertIn('ph.example.realapplication', arguments[1])
            self.assertEqual(arguments[2], VIDEOS[0][3])
            self.assertEqual(arguments[4], 'Isara ang video')
            self.assertEqual(arguments[5], 'Buksan sa YouTube')
            self.assertTrue(arguments[-1])
            bridge.close()
            self.assertEqual(calls[-1], 'closed')

    def test_android_configuration_includes_native_source_and_network_permission(self):
        root = Path(__file__).resolve().parents[1]
        config = configparser.ConfigParser()
        config.read(root / 'buildozer.spec')
        self.assertIn('INTERNET', config['app']['android.permissions'])
        self.assertIn('android_src', config['app']['android.add_src'])
        self.assertTrue((root / 'android_src/org/curiocitech/player/VideoPlayer.java').is_file())
        self.assertEqual(config['app']['version'], VERSION)


if __name__ == '__main__':
    unittest.main()
