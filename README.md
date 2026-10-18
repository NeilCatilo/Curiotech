# Curiocitech mobile

A minimalist Android learning app in **English and Tagalog**. One upper-left Menu
button opens every section: Home, Dictionary, Library, Videos, Quiz, Settings,
and About. There are no app bars, bottom navigation, or desktop sidebar.

## Preview while developing

```powershell
.\.venv\Scripts\python.exe main.py
```

On a computer this opens a portrait phone preview; the product targets mobile.
The project virtual environment is already prepared. On another machine, install
Python 3.12 or 3.13, create a virtual environment, and install `requirements.txt`.
Kivy 2.3.1 is the runtime dependency.

## Language and content

Choose **English** or **Tagalog** in the menu or Settings. The choice is saved
and updates the interface, definitions, resource descriptions, questions, choices,
and explanations immediately. Switching languages keeps an unfinished quiz's
order, selected answer, and score. Search accepts English and Tagalog meanings.
Technology names, abbreviations, publisher names, and people's names stay intact.

The reading library includes ten original offline guides with numbered steps,
practical reminders, and optional **Learn more** links. The app's own guides are
available in both languages. External further-reading pages, video audio, and
captions remain in their publishers' languages.

## In-app online video

On Android, **Watch in app** opens YouTube's embedded player inside a native
WebView in the app. No video is downloaded or extracted. Playback needs internet
and an up-to-date Android System WebView. The player retains YouTube controls and
branding, supports fullscreen, and includes **Close video** and an optional
**Open on YouTube** fallback. Closing the player, leaving Videos, or backgrounding
the app stops playback.

The PC preview cannot run Android WebView; it shows an explanatory dialog instead.
Native playback still needs physical-device validation. A publisher may disable
embedding, or restrict playback by region, age, or availability. Such restrictions
are not bypassed. Error messages and the YouTube fallback remain available.

The Android bridge and `INTERNET` permission are configured in `buildozer.spec`.
The WebView identifies itself with the installed application's actual package
name, as required by the [YouTube embedded-player identity guidance](https://developers.google.com/youtube/terms/required-minimum-functionality#embedded-player-api-client-identity).

## Design and behaviour

- Single-column pages with a quiet green palette, original line icons, existing
  video thumbnails and team photos, and comfortable touch targets.
- A dismissible drawer; Android Back closes dialogs and the menu before navigating.
- Short screen fades and a sliding drawer, with a reduced-motion preference.
- Saved appearance, text-size, language, and optional sound preferences. Sound
  starts off; the original click and answer effects are retained.
- One offline dictionary and the original eight situational quiz questions in
  English and Tagalog. The quiz uses a two-column answer grid, green/red feedback,
  automatic advancement after one second, and Yes/No choices to try again.
  Repeated taps cannot change the score. Opening the menu, leaving the quiz, or
  backgrounding the app pauses the pending transition. Completed scores are saved.
- A Home page explaining the app, its learning sections, and how to begin.

Unfinished practice is retained while the process stays alive. Android can end a
background process; unfinished sessions do not survive process termination.
Settings and completed scores use atomically written local `learning.json` in the
app's user-data directory. Device backups may also apply. There is no login,
advertising SDK, or analytics integration of its own. Streaming connects to
YouTube, whose privacy policy, advertising, and data processing apply.

## Check and build

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe tools/smoke_ui.py
```

The GUI check uses isolated preferences and exports phone previews to
`artifacts/mobile-v1.2/`. It never opens a real external browser. It simulates
phone dimensions on a computer and mocks the native-player route; it does not
prove streaming playback on Android.

To build on GitHub without installing WSL, use the **Build Android APK** workflow
in `.github/workflows/android-apk.yml`. Upload the project to a GitHub repository,
including `.github`, `android_src`, `Images`, `FONTS`, and `Sounds`. In **Actions**,
select the workflow, review the Android SDK terms and select the license checkbox,
then choose **Run workflow**. After success, download **Curiocitech-debug-apk** from
the run's **Artifacts** section and extract the ZIP to get the APK. The workflow
must be on the repository's default branch to appear as a manual workflow.

This creates a test APK. It does not publish the app or create a signed store
release. The workflow has been checked locally but has not run on GitHub yet.

Android builds also use `buildozer.spec` on Linux or WSL. See
[docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) and [docs/VALIDATION.md](docs/VALIDATION.md).
No APK is included: the current Windows environment has no installed Linux/WSL
distribution or Android build toolchain.

## Files

- `main.py`: mobile lifecycle, preferences, localisation, navigation, dialogs.
- `Manager.py`: floating menu, drawer, home.
- `ui.py` / `ui.kv`: mobile components, line icons, styling.
- `i18n.py` / `content_tl.py`: interface and learning translations.
- `content.py`: English source content, resource URLs, credits.
- `lessons.py`: original bilingual, step-by-step reading guides.
- `player.py`: secure embed HTML and the PyJNIus player bridge.
- `android_src/`: native Android WebView, fullscreen and player lifecycle code.
- `core.py`: UI-independent search, scoring, navigation, storage.
- Feature modules: individual learning screens and settings.

The previous source design is archived in `.backups/before-mobile-redesign.zip`;
the original project is in `.backups/original-source.zip`. Previous Windows
artifacts in `dist/` belong to version 1.0 and do not contain this mobile redesign.
Desktop build configuration has been removed from the active project.

Before publishing, review translations with native-speaking target users, check
external content and captions, confirm rights to existing photos/fonts/audio,
and verify the support address. The geometric icon assets are generated by
`tools/prepare_brand_assets.py` using Pillow as an optional development tool.
