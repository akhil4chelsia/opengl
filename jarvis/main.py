import os
import time
from time import ctime

import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 125)
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen()

    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data


def jarvis(data):
    if "how are you" in data:
        speak("I am fine")

    if "what time is it" in data:
        speak(ctime())

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Akhil, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")


# initialization
time.sleep(2)
speak("Hi Akhil, what can I do for you?")
while 1:
    data = listen()
    jarvis(data)
