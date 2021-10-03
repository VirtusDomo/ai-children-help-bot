import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyaudio
from input import Regimen, docVisits
import syllables
import pygame as pg
import time
import sys

pg.init()

black = (0,0,0)
white = (255,255,255)

faceImg = pg.image.load('default-face.jpg')
talkingImg = pg.image.load('eyes-mouth.jpg')
talkingImg2 = pg.image.load('mouth2.jpeg')
talkingImg3 = pg.image.load('mouth3.jpeg')

clock = pg.time.Clock()
gameDisplay = pg.display.set_mode((537,403))


def talking(seconds):
    t_end = time.time() + seconds
    speed = 5
    while time.time() < t_end:
        gameDisplay.blit(talkingImg, (0,0))
        pg.display.flip()
        clock.tick(speed)
        gameDisplay.blit(talkingImg2, (0,0))
        pg.display.flip()
        clock.tick(speed)
        gameDisplay.blit(talkingImg2, (0,0))
        pg.display.flip()
        clock.tick(speed)
        gameDisplay.blit(faceImg, (0,0))
        pg.display.flip()
        clock.tick(speed)
    return

def speak(syllables):
    close = time.time() + syllables
    while time.time() < close:
        wait = time.time() + 5
        while time.time() < wait:
            gameDisplay.blit(faceImg, (0,0))
            pg.display.flip()
        talking(syllables/4)

    pg.display.quit()
    pg.quit()
    sys.exit()

NAME = 'gizmo'
# sets up listener
listener = sr.Recognizer()

# indicates which microphone to use MAKE SURE TO SPECIFY
mic = sr.Microphone(device_index = 0)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# IMPORTANT: Voices[12] is only based on Mike's local machine.
engine.setProperty('voice', voices[18].id)
#9 calm voice, 25 laugh, 61, 4, 16 robo sing, 18 base, 24 long song

# Greet the user, first time activation
engine.say('Hi Bestie! How can I help you')
engine.runAndWait()

# Remind the user
time = datetime.datetime.now().strftime('%I:%M %p')
engine.say('The time is' + time + ". Don't forget to take your medication!")

# Speaks whatever text is passed into the function
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Finds the instructions, hands over the resulting text to talk() to be read aloud
def findTask():
    try:
        with mic as source:
            print(sr.Microphone.list_microphone_names())
            print('Im listening :)')
            listener.adjust_for_ambient_noise(source)
            print('Say something')
            listener.energy_threshold = 4000

            # Hears a voice
            voice = listener.listen(source) # here
            print('i heard a voice')

            # Recognizes the voice
            command = listener.recognize_google(voice)
            print('i heard a command')
            command = command.lower()

            # Listens for its name, if the name is called, the command will execute
            if NAME in command:
                command = command.replace(NAME, '')
                print(command)

            # If Program cannot hear anything
            else:
                print("nothing heard")
    except:
        print('i cannot hear anything')
        pass
    return command

# Performs the command accordingly to what the user instructed
def doTask():
    task = findTask()
    print(task)

    # Play music
    if 'play' in task:
        song = task.replace('play', '')
        speak(2)
        talk('playing' + song)
        pywhatkit.playonyt(song)

    # Reports time
    elif 'time' in task:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(3)
        talk('Hi bestie! the time is ' + time)

    # Defines or describes Wikipedia entry
    elif 'what is ' in task:
        thing = task.replace('what is', '')
        info = wikipedia.summary(thing,2)
        sylls = syllables.estimate(info)
        speak(sylls)
        print(info)
        talk(info)

    # Appointments
    elif 'I forgot my next appointment' in task:
        speak( 15)
        talk('Not to worry. You are scheduled to see Dr. Chen on December 2nd. That is in a month.')

    # Emotional support ( Do you like me?)
    elif 'Do you like me' in task:
        speak(3)
        talk('You are my best friend')

    elif "I'm scared" in task:
        speak(5)
        talk('Everything will be okay. We are all here for you.')

    # Shuts down the program
    elif 'shut up' in task:
        speak(5)
        talk('Okay meanie. I will go now. Goodbye.')
        pass

    # Tells a joke
    elif 'joke' in task:
        joke = pyjokes.get_joke()
        sylla = syllables.estimate(joke)
        speak(sylla)
        talk(pyjokes.get_joke())

    elif "medicine" in task:
        sylla = syllables.estimate(Regimen)
        speak(sylla)
        talk (Regimen)

    elif "doctor visit" in task:
        sylla = syllables.estimate(docVisits)
        speak(sylla)
        talk (docVisits)

    # Birthday
    elif "It's my birthday" in task:
        engine.setProperty('voice', voices[18].id)
        speak(15)
        talk("Happy birthday to you, happy birthday to you, happy birthday dear bestie, happy birthday to you")
        engine.setProperty('voice', voices[16].id)

    # Sass
    else:
        speak(5)
        talk('Sorry bestie not that smart')

# Use a while loop to keep the inputs going until user requests otherwise
while True:
    doTask()
