import pyttsx3
import datetime
import SpeechRecognition




engine= pyttsx3.init('sapi5')
voices =engine.getProperty('voices')

#voice[0] is for the david(male voice) and voice[1]is for the female voice
#print(voices[0].id)

engine.setProperty('voice',voices[1].id)

#sapi5 is a window api for inbuilt voices

#speak function (audio arrgumnet)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("good Evening!")
    speak("hi my name is Jarvish! ,how may i help you ")

def takeCommand():
    """It takes microphones imput from the user and returns 
        string output 
    """
   r=sr.Recognizer()
   with sr.Microphone() as source:
if __name__ =="__main__":
    wishMe()