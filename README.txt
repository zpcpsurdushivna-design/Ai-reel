AI Reel Agent - Package
=======================

Contents:
- ai-reel-agent-backend/   (FastAPI backend)
- ai-reel-agent-android/   (Android Studio project - source)
- build_instructions.txt   (how to build backend & APK)
- env_examples/.env.example

Quick start (local docker for backend):
1. Backend
   - cd ai-reel-agent-backend
   - python3 -m venv venv
   - source venv/bin/activate
   - pip install -r requirements.txt
   - copy .env.example to .env and edit with your details
   - uvicorn main:app --reload --host 0.0.0.0 --port 8000

2. Android (build APK)
   - Open ai-reel-agent-android/ in Android Studio
   - Update BACKEND_URL in MainActivity.java to your backend URL
   - Build -> Build Bundle(s) / APK(s) -> Build APK
   - Install generated APK on your Android device

Notes:
- The backend contains placeholder OAuth flows. Replace placeholders with real OAuth exchange logic.
- For production hosting use Render.com, Railway, or any VPS and set BASE_URL accordingly.
