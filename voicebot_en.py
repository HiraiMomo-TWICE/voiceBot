import pyttsx3
import datetime
import os
import speech_recognition as sr
import webbrowser as wb

en_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'

voicebot = pyttsx3.init()
voices = voicebot.getProperty('voices')
voicebot.setProperty('voice', voices[1].id)

def Speak(audio):
    print('Sana-chan: ' + audio)
    voicebot.say(audio)
    voicebot.runAndWait()

def Time():
    Time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    Speak(Time)

def Welcome():
    hour = datetime.datetime.now().hour

    if (hour >= 5 and hour < 12):
        Speak('Good morning sir')
    if (hour >= 12 and hour < 17):
        Speak('Good afternoon sir')
    if (hour >= 17 and hour < 21):
        Speak('Good evening sir')
    else:
        Speak('Good night sir')
    Speak('How can I help you')

def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)

    try:
        query = c.recognize_google(audio, language = 'en')
        print('Owner: ' + query)
    except sr.UnknownValueError:
        print('Repeat or type order')
        query = str(input('Type an order, sir: '))

    return query
        