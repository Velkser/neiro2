import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3 as p3
from finder import find


def talk(words):
    print(words)
    #os.system("say " + words)
    engine = p3.init()
    engine.say(words)
    engine.runAndWait()
    
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 5)
        audio = r.listen(source)
    try:
        zadanie = r.recognize_google(audio).lower()
        print("Вы сказали: " + zadanie)
    except sr.UnknownValueError:
        talk("Простите, я вас не поняла.")
        zadanie = command()
    return zadanie


def make(zadanie):
    if "open website" in zadanie:
        #words = zadanie.split(" ")
        #site = words[words.index("website")+1]
        talk("Уже открываю.")
        url = "https://www.youtube.com/watch?v=iIOKHKwi2TE"    
        #url = find(site)
        #print(url)
        webbrowser.open(url)
    elif "stop" in zadanie:
        talk("Уже закрываю.")
        sys.exit()
        

    
while True:
    make(command())