"""YouTube embed document and a small bridge to the Android in-app player.

Uses YouTube's supported iframe player; does not extract streams or download video.
"""

import html
import json
import re
import secrets
from urllib.parse import urlencode

from i18n import translate


def validate_video_id(video_id):
    if not isinstance(video_id, str) or not re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
        raise ValueError("Invalid YouTube video ID")
    return video_id


def app_origin(package_name):
    if not isinstance(package_name, str) or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*(?:\.[A-Za-z][A-Za-z0-9_]*)+", package_name):
        raise ValueError("Invalid Android application ID")
    return "https://" + package_name.lower()


def build_player_html(video_id, package_name, title, language="en", dark=False):
    """The base URL must match this origin when loading the page in WebView."""
    validate_video_id(video_id)
    origin = app_origin(package_name)
    t = lambda message: translate(message, language)
    nonce = secrets.token_hex(16)
    settings = urlencode({"enablejsapi": 1, "origin": origin, "autoplay": 0,
                          "controls": 1, "playsinline": 1, "fs": 1,
                          "hl": "tl" if language == "tl" else "en"})
    source = f"https://www.youtube-nocookie.com/embed/{video_id}?{settings}"
    messages = {
        "ready": t("Tap Play to start. Internet is required."),
        "error": t("Video could not load. Check your connection or try Open on YouTube."),
        "blocked": t("The publisher does not allow this video to play here. You can try Open on YouTube."),
        "identity": t("The player could not be verified. Try again or open the video on YouTube."),
    }
    js_messages = json.dumps(messages, ensure_ascii=True).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    background, foreground = ("#11191c", "#edf5ef") if dark else ("#f6f8f5", "#19302b")
    return f'''<!doctype html>
<html lang="{html.escape(language, quote=True)}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta http-equiv="Content-Security-Policy" content="default-src 'self' https:; script-src 'nonce-{nonce}' https://www.youtube.com https://s.ytimg.com; style-src 'unsafe-inline'; frame-src https://www.youtube-nocookie.com https://www.youtube.com; object-src 'none'; base-uri 'none'">
<title>{html.escape(title)}</title>
<style>body{{margin:0;padding:16px;background:{background};color:{foreground};font:16px/1.55 sans-serif}}
h1{{font-size:21px;line-height:1.4;margin:8px 0 20px}}.player{{position:relative;width:100%;aspect-ratio:16/9;min-height:200px;background:#000}}
iframe{{position:absolute;width:100%;height:100%;border:0}}p{{margin:18px 0}}small{{font-size:14px}}</style>
</head><body><h1>{html.escape(title)}</h1>
<div class="player"><iframe id="video-frame" title="{html.escape(title, quote=True)}"
src="{html.escape(source, quote=True)}" allow="encrypted-media; fullscreen; picture-in-picture" allowfullscreen
referrerpolicy="strict-origin-when-cross-origin"></iframe></div>
<p id="status" role="status" aria-live="polite">{html.escape(t("Loading video…"))}</p>
<small>{html.escape(t("Online video uses internet data. YouTube's privacy policy and any ads apply."))}</small>
<script nonce="{nonce}">
const messages={js_messages};let resolved=false;
function statusMessage(text){{document.getElementById('status').textContent=text;}}
window.onYouTubeIframeAPIReady=function(){{
  new YT.Player('video-frame',{{events:{{
    onReady:function(){{resolved=true;statusMessage(messages.ready);}},
    onError:function(event){{resolved=true;statusMessage([101,150].includes(event.data)?messages.blocked:(event.data===153?messages.identity:messages.error));}}
  }}}});
}};
const api=document.createElement('script');api.src='https://www.youtube.com/iframe_api';
api.onerror=function(){{resolved=true;statusMessage(messages.error);}};document.head.appendChild(api);
setTimeout(function(){{if(!resolved)statusMessage(messages.error);}},20000);
</script></body></html>'''


class AndroidYouTubePlayer:
    def __init__(self):
        self._native = None

    def open(self, video_id, title, language="en", dark=False):
        from jnius import autoclass
        activity = autoclass("org.kivy.android.PythonActivity").mActivity
        package_name = str(activity.getPackageName())
        document = build_player_html(video_id, package_name, title, language, dark)
        self._native = autoclass("org.curiocitech.player.VideoPlayer")
        t = lambda message: translate(message, language)
        self._native.show(activity, document, video_id, title, t("Close video"),
                          t("Open on YouTube"), t("Please update Android System WebView and try again. You can also use Open on YouTube."), dark)

    def close(self):
        if self._native:
            self._native.close()
