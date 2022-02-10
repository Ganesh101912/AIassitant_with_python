from calendar import month
from re import search
from sqlite3 import Time
from tracemalloc import start
from unittest import result



import pyttsx3      #pip install pyttsx3 in command prompt 
import datetime
import speech_recognition   #pip install SpeechRecognition
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui        #pip install pyautogui
import psutil            #pip install psutil
import pyjokes           #pip install pyjokes
import webbrowser


engine = pyttsx3.init()

# edit voice and speed

voice = engine.getProperty('voices')         #getting details of the current voice
engine.setProperty('voice', voice[1].id)
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()             #Without this command, speech will not be audible to us.

def time():
    Time = datetime.datetime.now().strftime("     %I: %M: %S")
    speak("The current time is ")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("Current date is ")
    speak(day)
    speak(month)
    speak(year)
  

def wishme():
    speak("Welcome Back sir!")

    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Good morning")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good Evening")
    else :
        speak("Good Night")
    
    speak("Ganesh  at your service. How I can help you ?")


def takeCommand():
     #It takes microphone input from the user and returns string output

    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= "en-US")        #Using google for voice recognition.
        print(query)

    except Exception as e:
        print(e)                               # use only if you want to print the error!
        speak("Say that again please...")       #Say that again will be printed in case of improper voice 
        
        return "None"            #None string will be returned
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    speak("Tell me your email")
    yourMail = takeCommand()
    speak("Tel me your password too ")
    yourPass = takeCommand()
    server.login(yourMail, yourPass)
    server.sendmail(yourMail, to, content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)

    battery = psutil.sensors_battery()
    speak("Battery percentage ")
    speak(battery.percent )
    speak("Power plugged")
    speak(battery.power_plugged)

def jokes():
    speak(pyjokes.get_joke())

def screenshot():
    img = pyautogui.screenshot()
    img.save("Desktop\ss.png")

if __name__ == "__main__" :
    wishme()

    while True:
        query = takeCommand().lower()       #Converting user query into lower case
        print(query)

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "offline" in query:
            quit()

        elif "wikipedia" in query:
            #if wikipedia found in the query then this block will be executed

            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            speak(result)
            

        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open internshala' in query:
            webbrowser.open("internshala.com")

        elif 'open skype' in query:
            webbrowser.open("skype.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")  

        elif 'open udemy' in query:
            webbrowser.open("udemy.com")

        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("Who is take this email?")
                to = takeCommand()
                sendEmail(to, content)
                speak(content)
                speak("Email sent sucessfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")

        elif "search on chrome" in query:
            speak("What should I search?")
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        
        elif "logout" in query:
            os.system("shutdown - l")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("shutdown /r /t 1")
        
        elif "play songs" in query:
            songs_dir = "D:\musics\music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        
        elif "remember that" in query:
            speak("What should I remember")
            data = takeCommand()
            speak("you said me to remember" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you know anything" in query:
            remember = open("data.txt", "r")
            speak("you said to me to remember that" + remember.read())
        
        elif "screenshot" in query:
            screenshot()
            speak("Done!")

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()