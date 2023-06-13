import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import random
from requests import get

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Boss")

    elif hour >= 12 and hour < 15:
        speak("Good noon Boss")

    elif hour >= 15 and hour < 17:
        speak("Good Afternoon Boss")

    elif hour >= 17 and hour < 20:
        speak("Good evening Boss")

    else:
        speak("Good Night boss")

    print("I am SIOM. Please tell me how can I help you?")
    speak("I am SIOM. Please tell me how can I help you?")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Please, say that again Boss...")
        speak("Please, say that again Boss...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shuvrod2021@gmail.com', '')
    server.sendmail('shuvrod2021@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if ' tell me about ' in query:
            speak("Here you are, Boss!")
            query = query.replace("tell me about ", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'how are you' in query:
            speak("I am fine Boss! How are you going my dear Boss")

        elif 'i am also fine' in query:
            speak("nice hearing it Boss")

        elif 'i am not well' in query:
            speak("Oh, sorry to hear that Boss? what happened")

        elif 'you cannot understand' in query:
            speak("Ok Boss")

        elif 'you are really amazing' in query:
            speak("Thank you boss")

        elif 'you are blushing' in query:
            speak("oh boss you understood")

        elif 'play ' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'open youtube' in query:
            speak("Here you are, Boss!")
            webbrowser.open("https://www.youtube.com/")

        elif 'open tw' in query:
            speak("Here you are, Boss!")
            webbrowser.open("https://10fastfingers.com/typing-test/english")

        elif 'open google' in query:
            speak("What should I search on google, Boss!")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open facebook' in query:
            speak("Here you are, Boss!")
            webbrowser.open("https://facebook.com/")

        elif 'open instagram' in query:
            speak("Here you are, Boss!")
            webbrowser.open("https://instagram.com/")

        elif 'open whatsapp' in query:
            speak("Here you are, Boss!")
            webbrowser.open("https://web.whatsapp.com/")

        elif 'send message in whatsapp ' in query:
            speak("What should I send on whatsapp, Boss!")
            whm = takeCommand().lower()
            pywhatkit.sendwhatmsg("", f"{whm}")

        elif 'music time' in query:
            speak("Here you are, Boss!")
            music_dir = "C:\\Users\\shuvr\\Music\\My_music"
            songs = os.listdir(music_dir)
            print(songs)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'the time  ' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%p")
            speak(f"Boss, the time is {strTime}")

        elif 'open vs code' in query:
            speak("Here you are, Boss!")
            codePath = "C:\\Users\\shuvr\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = ""
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Boss. I am not able to send this email")

        elif 'open command prompt' in query:
            speak("Here you are, Boss!")
            os.system("start cmd")

        elif 'what is my ip address ' in query:
            ip = get('https://api.ipify.org').text
            print("Ip address is {ip}")
            speak(f"Ip address is {ip}")

        elif 'shutdown' in query:
            speak("Ok, have a good day Boss!")
            exit()
