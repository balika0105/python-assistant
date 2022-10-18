# Python personal assistant base with Voice and Voice Control
# By Balázs M. 2022

# pip install pyttsx3
# pip install speechrecognition

# For Windows: pip install pyaudio
# For Linux: install python3-pyaudio from your distro's repo

import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
username = ''
ama = "Ask me anything!"

def ReadOut(input):
    tts = pyttsx3.init()
    tts.say(input)
    tts.runAndWait()

def recogniseSpeech():
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)

            print("Speak > ", end = '')

            audio2 = r.listen(source2)

            SpeechText = r.recognize_google(audio2)
            return SpeechText
    except:
        print("An error occured in speech recognition")

def askUserName():
    askusername = "Hello user! What is your name?"
    print(askusername)
    ReadOut(askusername)

    username = recogniseSpeech()

    # Confirm phase
    print("Is your name " + username + "? (yes/no)\n")
    ReadOut("Is your name " + username + "?")

    choice = recogniseSpeech()
    if choice == 'yes':
        mainLoop()
    else:
        askUserName()


def mainLoop():
    
    print(ama)
    ReadOut(ama)

    val = processcommand(recogniseSpeech())
    print(val)
    ReadOut(val)

    mainLoop()

def processcommand(command):
    match command:
        case "help":
            return "No help yet"
        case "exit":
            exit()


# Starts the whole process
askUserName()