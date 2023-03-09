import speech_recognition as sr
import pyttsx3 
import pywhatkit 


listener=sr.Recognizer()
engine=pyttsx3.init()

 

def talk(text):
    engine.say(text)
    engine.runAndWait()
     

def take_command(): 
    command = None
    try:
        with sr.Microphone() as source:
            print('listening..')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'ALEXA' in command:
                command=command.replace('ALEXA','')
                print(command)
    except:
        pass
     
    return command 

def run_ALEXA():
    command = take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+ song)
        pywhatkit.playonyt(song)
        print(song)

run_ALEXA()


