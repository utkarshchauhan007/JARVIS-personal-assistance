import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
name="Utkarsh , how may i help you" 
engine.setProperty('voice',voices[0].id)
chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12:
        speak("Good Morning!"+name)
    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON!"+name)
    else:
        speak("GOOD EVENING!")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        print("pass1")
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        print("pass2")
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        
        speak("Say that again please...")
        return "None"
    return query
if __name__=="__main__":
    wishMe()
    while True:    
        query=takeCommand().lower()
        var=query
        if ('shut down' in query or 'shutdown' in query):
            break
        if 'wikipedia' in query:
            print('searching in Wikipedia...')
            query=query.replace("wikipedia","") 
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'search for' in query:
            var=var.replace("search for ","")
            print(f"{var}")
            webbrowser.get(chrome_path).open(f"{var}")
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%H:%S")
            speak(f"sir, the time is {strTime}")
        elif 'open code' in query:
            path="C:\\Users\\National\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        