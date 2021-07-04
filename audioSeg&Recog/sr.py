import speech_recognition as sr
AUDIO_FILE=("audio-extract.wav")
# use audio file as source
r=sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
try:
    print("audio file contains:"+r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google cannot understand")
except sr.RequestError:
    print("couldnt get the results from google speech Recognition")
