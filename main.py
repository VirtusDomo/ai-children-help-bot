import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
print('program started')
NAME = 'alexa'
# sets up listener
listener = sr.Recognizer()

# indicates which microphone to use MAKE SURE TO SPECIFY
mic = sr.Microphone(device_index=2)
engine = pyttsx3.init()
engine.say('Hi Friend')
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
            voice = listener.listen(source) # here
            print('i heard a voice')
            command = listener.recognize_google(voice)
            print('i heard a command')
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
            else:
                print("nothing heard")
    except:
        print('i cannot hear anything')
        
    return command

def doTask():
    task = findTask()
    print(task)
    if 'play' in task:
        song = task.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in task:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('HI! the time is ' + time)
    elif 'what is ' in task:
        thing = task.replace('what is', '')
        info = wikipedia.summary(thing,2)
        print(info)
        talk(info)
    elif 'do you like me' in task:
        talk('You are my best friend')
    elif 'joke' in task:
        talk(pyjokes.get_joke())
    else:
        talk('Sorry could you repeat that')

while True:
    doTask()
