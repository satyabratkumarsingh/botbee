import speech_recognition as sr

def listen_mic_text(): 
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Speak now to bot...")
        audio = r.listen(source, phrase_time_limit = 5, timeout=5)
    text = r.recognize_google(audio)
    return text