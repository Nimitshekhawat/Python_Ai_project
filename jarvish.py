import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import os 
import wikipedia
import webbrowser
import urls
import email_ids
import smtplib
import utils


engine= pyttsx3.init('sapi5')
voices =engine.getProperty('voices')

# Set the path to the Chrome executable (modify the path according to your system)
chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

# Open the URL in Google Chrome
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))


#voice[0] is for the david(male voice) and voice[1]is for the female voice
#print(voices[0].id)

engine.setProperty('voice',voices[0].id)

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
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f"User said: {query}\n")
            speak(query)


        except Exception as e:
            #print(e)

            print("Say that again please...")
            return "None"
        return query

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('email@gmail.com','passs')
    server.sendmail('reciveremail',to,content)
    server.close()


if __name__ =="__main__":
    #wishMe()
    if 1:
        query = takeCommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)
        elif 'open youtube' in query:
            webbrowser.get('chrome').open(urls.url_youtube)
        
        elif 'open google' in query:
            webbrowser.get('chrome').open(urls.url_google)
        elif 'open whatsapp' in query:
            webbrowser.get('chrome').open(urls.url_whatsapp)

        elif 'play songs' or 'play music' in query:
            music_dir="C:\\Users\\NIMIT\\Music\\nimit_songs"
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        #Send Email to your friends
        elif 'send email' in query:
            try:
                speak("what should i say")
                content= takeCommand()
                to=email_ids.shivam
                sendemail(to,content)
                speak('email has been send!')

            except Exception as e:
                print(e)
                speak("bhai maaf kriyo but teri email na bhej paya mai iss baar")





        
