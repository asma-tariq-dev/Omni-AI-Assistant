import speech_recognition as sr
from gtts import gTTS
import tempfile

def speech_to_text(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    try:
        return r.recognize_google(audio)
    except:
        return "Could not understand voice"

def text_to_speech(text):
    f = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    gTTS(text=text, lang="en").save(f.name)
    return f.name
