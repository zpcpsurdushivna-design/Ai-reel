from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
import uvicorn
import os

app = FastAPI()

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

@app.get("/", response_class=HTMLResponse)
def index():
    return f"""<html><body>
    <h2>AI Reel Agent Backend</h2>
    <p>Use the Android app to connect accounts.</p>
    <a href='/oauth/youtube/start'>Connect YouTube (start)</a><br/>
    <a href='/oauth/instagram/start'>Connect Instagram (start)</a><br/>
    <p>Endpoints:</p>
    <ul>
    <li>/oauth/youtube/start</li>
    <li>/oauth/youtube/callback</li>
    <li>/oauth/instagram/start</li>
    <li>/oauth/instagram/callback</li>
    <li>/start-auto</li>
    </ul>
    </body></html>"""

@app.get("/oauth/youtube/start")
def youtube_start():
    # Redirect user to Google OAuth consent screen (placeholder)
    redirect = f"https://accounts.google.com/o/oauth2/v2/auth?client_id=YOUR_GOOGLE_CLIENT_ID&redirect_uri={BASE_URL}/oauth/youtube/callback&response_type=code&scope=https://www.googleapis.com/auth/youtube.upload"
    return RedirectResponse(redirect)

@app.get("/oauth/youtube/callback")
def youtube_callback(code: str = None):
    return {"status":"ok","message":"YouTube callback placeholder. Exchange code for tokens here."}

@app.get("/oauth/instagram/start")
def instagram_start():
    redirect = f"https://www.facebook.com/v15.0/dialog/oauth?client_id=YOUR_META_APP_ID&redirect_uri={BASE_URL}/oauth/instagram/callback&scope=instagram_basic,instagram_content_publish,pages_show_list"
    return RedirectResponse(redirect)

@app.get("/oauth/instagram/callback")
def instagram_callback(code: str = None):
    return {"status":"ok","message":"Instagram callback placeholder. Exchange code for tokens here."}

@app.get("/start-auto")
def start_auto():
    # In production, start background scheduler or confirm automation enabled.
    return {"status":"ok","message":"Auto reels generation started (placeholder)."}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
