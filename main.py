import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import pyjokes
import webbrowser
from openai import OpenAI
from config import api_key
from AppOpener import open

listner = sr.Recognizer()
engine = pyttsx3.init()

client = OpenAI(api_key=api_key)


def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def chat(c):
    response = client.completions.create(
        model="text-davinci-003",
        prompt=c,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    talk(response.choices[0].text)


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            print(command)
    except:
        pass
    return command


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 00 and hour <= 11:
        talk("good morning sir")
    elif hour >= 12 and hour <= 18:
        talk("good afternoon sir")
    elif hour >= 19 and hour <= 21:
        talk("good evening sir")
    elif hour >= 22 and hour <= 23:
        talk('good night sir')


def runa():
    wishMe()
    while True:
        command = take_command()
        if "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            talk("current time is " + time)
        elif "joke" in command:
            talk(pyjokes.get_joke())
        elif "play" in command:
            song = command.replace("play", "")
            talk("playing " + song)
            pywhatkit.playonyt(song)
            exit(0)
        elif "game" in command:
            talk("opening space invader")
            webbrowser.open("https://ayush2006128.github.io/space-avenger-by-Ayush/index.html")
        elif "bye" in command:
            talk("good bye sir")
            exit(0)
        elif "open" in command:
            app = command.replace("open", "")
            open(app)
        elif "who are you" in command:
            talk("I am project ultron")
        else:
            chat(command)


if __name__ == "__main__":
    runa()
