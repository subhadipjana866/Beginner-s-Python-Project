# Importing modules

import datetime
import smtplib
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

# Speak function

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wish me function

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12 :
        speak("Good morning")
    elif hour >=12 and hour <18 :
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Agend 07. Please tell me how can I help you ?")
    
# Taking voice command 

def takeCommand1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try: 
        print("Recognizing ...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said :{query}\n")
    except Exception as e:
        print("Please say that again ")
        return "none"
    return query

# Taking keyboard command
    
def takeCommand2():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
    try:
        print("Recognizing...")
        query = input()
        print(f"User said :{query}\n")
    except Exception as e:
        print("Please say that again ")
        return "none"
    return query
        
# Email sending function

def sendmail():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("subhadipjana866@gmail.com","subhadip2003")
    server.sendmail("subhadipjana866@gmail.com",to,content)
    server.close()

# Main function

if __name__ == "__main__":
    wishMe()
    speak("Enter the method of input : 'v' for voice and 'k' for keyboard: ")
    choice = input("Enter the method of input : 'v' for voice and 'k' for keyboard: ")
    while True:
        
        if choice == "v":
            query = takeCommand1().lower()
        elif choice == "k":
            query = takeCommand2().lower()
        if "who are you" in query:
            speak("I am Agend 07. I am your virtual assistant from now on.")
        if "what can you do" in query:
            speak("I can do many things like playing music and browsing for you.")
        if "how old are you" in query:
            speak("I am as little as you are. So treat me like a child.")
        
        
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia"," ")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        if "open youtube" in query:
            speak("opening youtube ...")
            webbrowser.open("youtube.com")
        if "open instagram" in query:
            speak("opening instagram ...")
            webbrowser.open("instagram.com")
        if "open facebook" in query:
            speak("opening facebook ...")
            webbrowser.open( "facebook.com")
        if "open gmail" in query:
            speak("opening gmail ...")
            webbrowser.open("mail.google.com")
        if "open amazon" in query:
            speak("opening amazon ...")
            webbrowser.open("amazon.com")
        if "open google" in query:
            speak("opening google ...")
            webbrowser.open("google.com")
        elif "play music" in query:
            music_dir = 'Path' # Enter the location of music folder
            songs = os.listdir(music_dir)
            i = 0
            for j in songs:
                print(f" {i}  {songs[i]}")
                i = i+1
            speak("please enter the number of the song you want to play ")
            s = int(input("Enter the number of the song : "))
            os.startfile(os.path.join(music_dir,songs[s]))
        

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strtime}")
            speak(f"The time is {strtime}")
        elif "open code" in query:
            codepath = "C:\\Users\\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" # Enter the path of code editor
            os.startfile(codepath)

        elif "send email to susmita" in query:
            try:
                speak("What should I say ?")
                if choice == "v":
                    content = takeCommand1()
                elif choice == "k":
                    content = takeCommand2()
                to = input("Enter the reciever's email address : ")
                sendmail(to,content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send emails right now. PLease try again.")


