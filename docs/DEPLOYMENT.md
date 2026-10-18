# Android deployment — Curiocitech 1.2

The app targets portrait mobile use. Windows is only a development-preview host.
The app's own top/bottom bars are absent; Android's system status and navigation
areas remain managed by the operating system.

## Build on GitHub Actions

The repository includes `.github/workflows/android-apk.yml`. You can build using
GitHub's Linux runner without installing WSL or the Android SDK on Windows.

1. Put this project in a GitHub repository. Include the hidden `.github` directory,
   all application Python files, `ui.kv`, `buildozer.spec`, `tests`, `android_src`,
   `Images`, `FONTS`, and `Sounds`. Keep `.gitignore`; do not upload virtual
   environments, local runtime downloads, backups, or previous build outputs.
2. Commit the workflow to the repository's default branch (usually `main`).
3. Open **Actions > Build Android APK > Run workflow**.
4. Review the [Android SDK terms](https://developer.android.com/studio/terms).
   Select the acceptance checkbox if you agree, then start the workflow.
5. Wait for the job to finish. The first build downloads and compiles the Android
   toolchain and both configured ARM architectures.
6. Open the completed run and download **Curiocitech-debug-apk** under **Artifacts**.
   Extract its ZIP and transfer the `.apk` to your phone. Allow installation from
   that source if Android prompts you.

The workflow uses Ubuntu 24.04, host Python 3.14, Java 17, and the current Buildozer
develop toolchain configured in `buildozer.spec`. It checks the existing unit tests
before building. The SDK-license override applies only to the disposable runner's
copy after the checkbox is selected; local automatic acceptance stays disabled.
The APK is kept for 14 days. A separate build-log artifact is kept for seven days
when a build log exists, including on build failure. Open the failed step in
Actions for errors occurring before compilation.

No secrets or signing keystore are required for this debug build. It runs only
when manually requested and does not publish a GitHub release or submit to a store.
The APK uses a generated debug signing key; separate fresh runners may produce
different keys. If Android rejects an update due to a signature mismatch, uninstall
the previous debug app first (this removes its saved settings and scores).
Use one securely stored signing key for distributed release builds.

The workflow has been checked locally but has not yet executed on GitHub. Download
and device playback still need end-to-end validation. The development toolchain
tracks upstream changes; pin verified tool revisions before a production release.

References: [manual workflow runs](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow),
[workflow artifacts](https://docs.github.com/en/actions/tutorials/store-and-share-data),
[Buildozer installation](https://buildozer.readthedocs.io/en/latest/installation/).

## Build on Linux or WSL

Install the system prerequisites from the
[Buildozer installation guide](https://buildozer.readthedocs.io/en/latest/installation/).
Use a supported Linux Python environment; follow the toolchain's current Python,
Cython, Java, SDK, and NDK requirements. Keep a WSL checkout inside the Linux
filesystem rather than `/mnt/c`. Do not copy the Windows `.venv` to Linux.

```bash
python3.14 -m venv .venv-android
source .venv-android/bin/activate
python -m pip install --upgrade pip
python -m pip install git+https://github.com/kivy/buildozer
python -m pip install legacy-cgi setuptools cython==0.29.34
buildozer -v android debug
```

The first build downloads the Android SDK/NDK and requires review and acceptance
of their licences. The configuration deliberately leaves automatic SDK-licence
acceptance disabled. Test the resulting APK on a connected device using the
Buildozer/ADB deploy and run commands or install it manually.

`buildozer.spec` packages Python code, KV styles, local fonts, images, and sounds.
It declares Kivy and PyJNIus, portrait orientation, ARM64/ARMv7, minimum API 24,
and target API 36. Recheck the intended store's
[target API policy](https://developer.android.com/google/play/requirements/target-sdk)
at release time. The settings file is private local app data; no contacts, storage,
camera, or microphone permission is requested by the app. The normal `INTERNET`
permission is declared for in-app video streaming. Optional further-reading links
open through an installed browser using Android ACTION_VIEW.

## Native video integration

`android.add_src` includes `android_src/org/curiocitech/player/VideoPlayer.java`
in the APK. Keep that directory in the checkout even though it is excluded from
the Python asset bundle. The fully qualified bridge class name is independent of
your eventual application ID.

The bridge creates a native Dialog/WebView on Android's UI thread. JavaScript and
DOM storage are enabled for the official iframe player; local-file/content access,
mixed content, pop-up windows, and a JavaScript-to-native interface are disabled.
The runtime package name supplies the HTTPS base URL/Referer. Do not replace it
with an invented website or remove player branding/controls.

Playback is initiated by the learner. Fullscreen uses WebChromeClient's custom
view callbacks. Close/dismiss destroys the WebView; backgrounding or leaving the
video screen also closes it. Optional external YouTube playback happens only
after tapping the explicitly labelled native button.

Verify on actual Android hardware:

- Play, pause, captions where available, fullscreen enter/exit, and Back.
- Native Close and optional Open on YouTube, including no-browser devices.
- Wi-Fi/mobile data, no connection, slow loading, and reconnecting.
- Background/resume, notifications, and absence of continuing audio after close.
- Owner-disabled embedding (101/150), unavailable/age-restricted content, and
  missing player identity (153). Do not bypass these restrictions.
- Small screens, native text scaling, device/theme changes, and status-bar insets.

References: [Android WebView](https://developer.android.com/develop/ui/views/layout/webapps/webview),
[YouTube player identity](https://developers.google.com/youtube/terms/required-minimum-functionality#embedded-player-api-client-identity),
[iframe API errors](https://developers.google.com/youtube/iframe_api_reference#onError).

## Language verification

- Change language from both the open drawer and Settings, then restart the app.
- Review all 25 definitions, eight original situational questions and choices with
  fluent Tagalog speakers from the intended audience.
- Confirm English and Tagalog searches return the expected definitions.
- Change language before and after submitting a quiz answer, and check that the
  answer order, selected choice, and score remain the same.
- Check the two-column quiz, green/red feedback, automatic advancement, and Yes/No
  summary controls. Open/close the menu and background/resume during feedback;
  verify that the question pauses and then advances once.
- Check long Tagalog text at larger text sizes, on 320/360 dp screens, and with
  Android system text scaling enabled.
- Confirm external links show the browser/language notice. The app translates
  its own guides and catalogue descriptions; third-party pages and videos are not
  translated. Check the optional Learn more link after the local numbered steps.

## Release requirements

- Replace the provisional `org.curiocitech` application ID with an identifier you
  control. Keep it stable after publishing.
- Update `VERSION` in `core.py` and `version` in `buildozer.spec` together.
- Build and test a compatible current SDK/NDK/python-for-android combination,
  including [16 KB memory-page support](https://developer.android.com/guide/practices/page-sizes).
- Test the drawer, scrim taps, Back button, keyboard, gesture-navigation insets,
  cold start, background/process termination, offline mode, and failed saves on
  physical Android devices. Check devices with and without a browser.
- Test reading and contrast with older learners. Custom Kivy widgets need actual
  accessibility testing; native screen-reader semantics are not guaranteed.
- Check asset redistribution rights, resource availability and captions, the
  public support contact, privacy-policy URL, and required store disclosures.
- Configure release signing with a securely stored keystore. Never commit signing
  keys or passwords. Build an AAB with `buildozer android release` and validate
  through internal testing before production distribution.

References: [Buildozer specifications](https://buildozer.readthedocs.io/en/stable/specifications.html),
[python-for-android build/signing options](https://python-for-android.readthedocs.io/en/latest/buildoptions/).
