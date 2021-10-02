import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyaudio

print('program started')
NAME = 'gizmo'
# sets up listener
listener = sr.Recognizer()

# indicates which microphone to use MAKE SURE TO SPECIFY
mic = sr.Microphone(device_index=0)
engine = pyttsx3.init()
#engine.setProperty('age')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say('Hi Bestie')
engine.say('How can I help you')

# Reminder the user
time = datetime.datetime.now().strftime('%I:%M %p')
engine.say('How can I help you')
engine.runAndWait()



def talk(text):
    engine.say(text)
    engine.runAndWait()

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
            else:
                print("nothing heard")
    except:
        print('i cannot hear anything')
        pass
    return command

# Performs the command accordingly
def doTask():
    task = findTask()
    print(task)
    if 'play' in task:
        song = task.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in task:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Hi bestie! the time is ' + time)
    elif 'what is ' in task:
        thing = task.replace('what is', '')
        info = wikipedia.summary(thing,2)
        print(info)
        talk(info)
    elif 'do you like me' in task:
        talk('You are my best friend')
    elif 'shut up' in task:
        talk('Okay meanie. I will go now. Goodbye.')
        pass
    elif 'joke' in task:
        talk(pyjokes.get_joke())
    else:
        talk('Sorry bestie not that smart')

while True:
    doTask()
