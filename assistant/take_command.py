import speech_recognition as sr
import pyttsx3

engine =pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def speak(text):
    engine.say(text)
    text="SAM said:" +text
    print(text)
    engine.runAndWait()

def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold= 1
        r.energy_threshold = 300
        audio =r.listen(source)
        
        try:
            print("Recognizing.....")
            said = r.recognize_google(audio) #type:ignore
            print(f"User said: {said}\n")
            return said.lower()
        except Exception as e:
            speak("..Please say that again")
            return ""