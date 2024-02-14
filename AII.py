import pyttsx3
import speech_recognition as sr   #speech recognitaion
import datetime                   #date and time
import wikipedia             
import webbrowser
import os
import smtplib                     #smtlipb



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voice[1].id)
engine.setProperty('voices',voices[0].id)#voice[0]=male;voice[1]=female


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour <18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am shadow sir. Please tell me how may I help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_thershold=1
        audio =r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    sever = smtplib.SMTP('smpt.gmail.com',587)
    sever.ehlo()
    server.starttls()
    server.login("yuvanprasath1234@gmail.com", "22330011")
    server.sendmail ("yuvanprasath1234@gmail.com", to, content)
    server.close()

if __name__=="__main__":
    wishMe ()
    while True:
        
        
        query = takeCommand().lower ()
#Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak ('Searching Wikipedia...')
            query = query.replace ("wikipedia", "")
            try:
                results = wikipedia.summary (f' {query}',sentences=5) 
                speak ("According to Wikipedia")
                print (results)
                speak (results)
            except wikipedia.exceptions.PageError:
                 pass
                                 
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")
        elif 'open whatsup' in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif 'play music' in query:
            music_dir = 'D:\music' # your music playlist location path
            songs = os. listdir (music_dir)
            print (songs)
            os. startfile (os.path. join (music_dir, songs [0]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime ("%H:%M:%S")
            speak (f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "D:\yuvan"
        elif 'open photo' in query:
            photoPath = "D:\photo"
            os.startfile (photoPath)
                    
        elif 'email to friend' in query:
            try:
                speak ("What should I say?")
                content = takeCommand()
                to = "lalithakumar0877@gmail.com"
                sendEmail (to, content)
                speak ("Email has been sent!")
            except Exception as e:
                print(e)
                speak ("Sorry. I am not able to send this email")
                         
                      
                     
                  

                        



                            


