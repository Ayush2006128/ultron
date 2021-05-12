import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listner = sr.Recognizer()
engine = pyttsx3.init()


# bad_words = ["mad", "stupid", "foolish"]
# good_words = ["smart", "clavier", "nice"]


def talk(text):
    engine.say(text)
    engine.runAndWait()
    print(text)


# talk("i am your assistant")
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            if "Ayush" in command:
                command = command.replace("Ayush", "")
                print(command)
    except:
        pass
    return command





def runa():
    command = take_command()
    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        talk("current time is " + time)
    elif "joke" in command:
        talk(pyjokes.get_joke())
    elif "play" in command:
        song = command.replace("play", "")
        talk("playing " + song)
        pywhatkit.playonyt(song)
    elif "tell me about" in command:
        obj = command.replace("tell me about", "")
        talk(wikipedia.summary(obj, 1))
    else:
        talk("try again")


runa()

