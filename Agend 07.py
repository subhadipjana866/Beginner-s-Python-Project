
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
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12 :
        speak("Good morning")
    elif hour >=12 and hour <18 :
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Agend 07. Please tell me how can I help you ?")
def takeCommand():
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
def sendmail():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("subhadipjana866@gmail.com","subhadip2003")
    server.sendmail("subhadipjana866@gmail.com",to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

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
            music_dir = 'D:\\All files\\my phone\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strtime("%H:%M:%S")
            speak(f"The time is {strtime}")
        elif "open code" in query:
            codepath = "C:\\Users\\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile(codepath)

        elif "send email to esha" in query:
            try:
                speak("What should I say ?")
                content = takeCommand()
                to = input("Enter the reciever's email address : ")
                sendmail(to,content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send emails right now. PLease try again.")


