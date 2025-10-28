from gtts import gTTS
import os

def text_to_speech(text, out_path):
    tts = gTTS(text=text, lang='en', tld='com', slow=False)
    tts.save(out_path)
    return out_path
