[app]
title = Curiocitech
package.name = curiocitech
# Replace with a domain/identifier you own before publishing. Changing it later
# creates a different Android application.
package.domain = org.curiocitech
source.dir = .
source.include_exts = py,kv,png,jpg,ttf,mp3
source.exclude_dirs = tests,tools,docs,.backups,.runtime,.venv,.venv-android,build,dist,artifacts,.git,android_src
version = 1.2.0
requirements = python3,kivy==2.3.1,pyjnius
orientation = portrait
fullscreen = 0
icon.filename = %(source.dir)s/Images/app-icon.png
presplash.filename = %(source.dir)s/Images/presplash.png
android.archs = arm64-v8a, armeabi-v7a
android.minapi = 24
android.api = 36
# Current Buildozer develop toolchain; use host Python 3.14 and Java 17.
p4a.branch = develop
android.ndk = 29
# Recheck the store's target API requirements before publishing.
# Streaming video uses the native Android WebView and needs internet access.
android.permissions = INTERNET
android.add_src = %(source.dir)s/android_src
android.enable_androidx = True
android.accept_sdk_license = False
android.debug_artifact = apk
android.release_artifact = aab

[buildozer]
log_level = 2
warn_on_root = 1
