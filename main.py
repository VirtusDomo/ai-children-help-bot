import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyaudio

# for reading in a web page
from bs4 import BeautifulSoup
import urllib2
import html2text



print('Program started')
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
        talk('playing' + song)
        pywhatkit.playonyt(song)

    # Reports time
    elif 'time' in task:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Hi bestie! the time is ' + time)

    # Defines or describes Wikipedia entry
    elif 'what is ' in task:
        thing = task.replace('what is', '')
        info = wikipedia.summary(thing,2)
        print(info)
        talk(info)

    # Appointments
    elif 'I forgot my next appointment' in task:
        talk('Not to worry. You are scheduled to see Dr. Chen on December 2nd. That is in a month.')

    # Emotional support ( Do you like me?)
    elif 'Do you like me' in task:
        talk('You are my best friend')

    elif "I'm scared" in task:
        talk('Everything will be okay. We are all here for you.')

    # Shuts down the program
    elif 'shut up' in task:
        talk('Okay meanie. I will go now. Goodbye.')
        pass

    # Tells a joke
    elif 'joke' in task:
        talk(pyjokes.get_joke())

    # Birthday
    elif "It's my birthday" in task:
        engine.setProperty('voice', voices[18].id)
        talk("Happy birthday to you, happy birthday to you, happy birthday dear bestie, happy birthday to you")
        engine.setProperty('voice', voices[16].id)

    # Education
    elif ('Can you explain' or 'Tell more more about' 'What do you mean by') and (
            'down syndrome') in task:
        soup = BeautifulSoup(urllib2.urlopen('https://www.cdc.gov/ncbddd/birthdefects/' + 'downsyndrome' + '.html').read())
        talk(soup)

    # Sass
    else:
        talk('Sorry bestie not that smart')

# Use a while loop to keep the inputs going until user requests otherwise
while True:
    doTask()
