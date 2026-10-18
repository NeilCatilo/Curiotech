package org.curiocitech.player;

import android.app.Activity;
import android.app.AlertDialog;
import android.app.Dialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.graphics.Color;
import android.net.Uri;
import android.view.KeyEvent;
import android.view.View;
import android.view.ViewGroup;
import android.view.Window;
import android.view.WindowManager;
import android.webkit.WebChromeClient;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.FrameLayout;
import android.widget.LinearLayout;
import java.util.Locale;

/** In-app YouTube player. No JavaScript-to-native bridge or stream extraction. */
public final class VideoPlayer {
    private static volatile Dialog current;
    private static volatile Activity owner;

    private VideoPlayer() {}

    public static void show(final Activity activity, final String html, final String videoId,
                            final String title, final String closeText, final String openText,
                            final String failureText, final boolean dark) {
        if (videoId == null || !videoId.matches("[A-Za-z0-9_-]{11}")) {
            throw new IllegalArgumentException("Invalid video ID");
        }
        activity.runOnUiThread(new Runnable() {
            @Override public void run() {
                if (activity.isFinishing() || activity.isDestroyed()) return;
                if (current != null) current.dismiss();
                try {
                    openPlayer(activity, html, videoId, title, closeText, openText, failureText, dark);
                } catch (RuntimeException error) {
                    if (current != null) current.dismiss();
                    new AlertDialog.Builder(activity).setMessage(failureText)
                        .setNegativeButton(closeText, null)
                        .setPositiveButton(openText, new DialogInterface.OnClickListener() {
                            @Override public void onClick(DialogInterface dialog, int which) {
                                openExternal(activity, videoId, failureText);
                            }
                        }).show();
                }
            }
        });
    }

    private static void openPlayer(final Activity activity, String html, final String videoId,
                                   String title, String closeText, String openText, final String failureText, boolean dark) {
        final Dialog dialog = new Dialog(activity, dark ? android.R.style.Theme_Material_NoActionBar : android.R.style.Theme_Material_Light_NoActionBar);
        dialog.requestWindowFeature(Window.FEATURE_NO_TITLE);
        dialog.setTitle(title);
        final FrameLayout root = new FrameLayout(activity);
        final LinearLayout body = new LinearLayout(activity);
        body.setOrientation(LinearLayout.VERTICAL);
        body.setBackgroundColor(Color.parseColor(dark ? "#11191c" : "#f6f8f5"));
        LinearLayout controls = new LinearLayout(activity);
        controls.setOrientation(LinearLayout.HORIZONTAL);
        Button back = new Button(activity);
        back.setText(closeText);
        Button external = new Button(activity);
        external.setText(openText);
        controls.addView(back, new LinearLayout.LayoutParams(0, ViewGroup.LayoutParams.WRAP_CONTENT, 1));
        controls.addView(external, new LinearLayout.LayoutParams(0, ViewGroup.LayoutParams.WRAP_CONTENT, 1));
        body.addView(controls, new LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT));

        final WebView web = new WebView(activity);
        WebSettings settings = web.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setMediaPlaybackRequiresUserGesture(true);
        settings.setAllowFileAccess(false);
        settings.setAllowContentAccess(false);
        settings.setMixedContentMode(WebSettings.MIXED_CONTENT_NEVER_ALLOW);
        settings.setSupportMultipleWindows(false);
        settings.setJavaScriptCanOpenWindowsAutomatically(false);
        web.setBackgroundColor(Color.parseColor(dark ? "#11191c" : "#f6f8f5"));
        final String baseUrl = "https://" + activity.getPackageName().toLowerCase(Locale.ROOT) + "/";
        web.setWebViewClient(new WebViewClient() {
            @Override public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
                // Embedded frames may navigate normally; the top-level document
                // stays in our player. Only the explicit native button leaves it.
                return request.isForMainFrame();
            }
            @Override public boolean shouldOverrideUrlLoading(WebView view, String url) {
                return true;
            }
        });
        final FullscreenClient chrome = new FullscreenClient(root, body);
        web.setWebChromeClient(chrome);
        body.addView(web, new LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, 0, 1));
        root.addView(body, new FrameLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));
        dialog.setContentView(root);
        back.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View view) { dialog.dismiss(); }
        });
        external.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View view) {
                dialog.dismiss();
                openExternal(activity, videoId, failureText);
            }
        });
        dialog.setOnKeyListener(new DialogInterface.OnKeyListener() {
            @Override public boolean onKey(DialogInterface target, int keyCode, KeyEvent event) {
                if (keyCode == KeyEvent.KEYCODE_BACK && chrome.isFullscreen()) {
                    if (event.getAction() == KeyEvent.ACTION_UP) chrome.onHideCustomView();
                    return true;
                }
                return false;
            }
        });
        dialog.setOnDismissListener(new DialogInterface.OnDismissListener() {
            @Override public void onDismiss(DialogInterface target) {
                chrome.onHideCustomView();
                web.stopLoading();
                web.loadUrl("about:blank");
                web.onPause();
                body.removeView(web);
                web.removeAllViews();
                web.destroy();
                if (current == dialog) { current = null; owner = null; }
            }
        });
        current = dialog;
        owner = activity;
        Window window = dialog.getWindow();
        if (window != null) window.addFlags(WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED);
        dialog.show();
        if (window != null) window.setLayout(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT);
        // Use the real application ID as the Referer/base URL required by YouTube.
        web.loadDataWithBaseURL(baseUrl, html, "text/html", "UTF-8", null);
    }

    private static void openExternal(Activity activity, String videoId, String errorText) {
        try {
            activity.startActivity(new Intent(Intent.ACTION_VIEW,
                Uri.parse("https://www.youtube.com/watch?v=" + videoId)));
        } catch (RuntimeException error) {
            new AlertDialog.Builder(activity).setMessage(errorText)
                .setPositiveButton(android.R.string.ok, null).show();
        }
    }

    public static void close() {
        Activity activity = owner;
        if (activity == null) return;
        activity.runOnUiThread(new Runnable() {
            @Override public void run() { if (current != null) current.dismiss(); }
        });
    }

    private static final class FullscreenClient extends WebChromeClient {
        private final FrameLayout root;
        private final View body;
        private View fullscreen;
        private CustomViewCallback callback;
        FullscreenClient(FrameLayout root, View body) { this.root = root; this.body = body; }
        boolean isFullscreen() { return fullscreen != null; }
        @Override public void onShowCustomView(View view, CustomViewCallback customCallback) {
            if (fullscreen != null) { customCallback.onCustomViewHidden(); return; }
            fullscreen = view;
            callback = customCallback;
            body.setVisibility(View.GONE);
            root.addView(view, new FrameLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));
        }
        @Override public void onHideCustomView() {
            if (fullscreen == null) return;
            root.removeView(fullscreen);
            fullscreen = null;
            body.setVisibility(View.VISIBLE);
            CustomViewCallback finished = callback;
            callback = null;
            if (finished != null) finished.onCustomViewHidden();
        }
    }
}
