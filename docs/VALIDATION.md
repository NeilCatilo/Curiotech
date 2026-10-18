# Mobile validation — 18 October 2026

Current scope: minimalist Android app, version 1.2.0, English/Tagalog, one drawer
menu for all sections. Prior version-1.0 Windows build reports and ZIPs do not
describe the current mobile design.

All 39 automated tests passed. They cover scoring, shuffled answer identity, repeated
submissions, navigation, persistence and failed writes, bilingual search,
translation coverage, matching format placeholders, language migration, ten local
guides, video-ID/origin validation, embed configuration and escaping, the mocked
PyJNIus bridge, and Android source/permission integration.

All 20 Kivy UI checks passed. `tools/smoke_ui.py` uses isolated preferences and
reports to `artifacts/mobile-v1.2/smoke-report.json`. It checks the single menu,
all destinations, scrim/Back dismissal, language persistence, search in both
languages, language changes during a quiz, completion recorded once, resource
labels, settings, link confirmation, small screens, animations, and touch targets.
Additional checks confirm the upper-left menu, Home's app introduction, offline
numbered lessons, optional Learn more, and the native video route using a mock.
Previews in that folder show the current mobile design, visually inspected at
412 × 820 and 320 × 640, including Tagalog, larger text, and dark mode.

The native `VideoPlayer.java` component compiled successfully with javac 23.0.2
against Google's Android API 36 reference JAR, targeting Java 8 bytecode. Expected
compatibility/deprecation notes were emitted, with no compile errors. The generated
player JavaScript passed `node --check`. A standalone reference JAR was downloaded
for compilation; it is excluded from the app and is not a full Android toolchain.

Environment: Windows 11 x64, Python 3.13.3, Kivy 2.3.1 in the project virtual
environment. Phone dimensions are simulated on a desktop display. There is no
installed Linux/WSL distribution, complete Android SDK/NDK, connected Android
device, or Android emulator here. No APK/AAB was built or tested. The actual
YouTube stream, Android WebView playback, fullscreen and lifecycle behaviour
have not been verified on a device; the PC notice explicitly explains this.

Before public release, complete the physical-device, accessibility, translation,
asset-rights, signing, and store checks in [DEPLOYMENT.md](DEPLOYMENT.md).
