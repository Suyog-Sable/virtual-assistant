import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning..")

    elif hour>=12 and hour<18:
        speak("Good Afternoon..")

    else:
        speak("Good Evening..")

    speak("I am Jarvis Sir, how may I help you. ")

def takeCommand():
    #this one takes input from user ad returns string out put

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language ='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)   
        print("say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP(smtp.gmail.com, 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    WishMe()
    while True:
       query = takeCommand().lower()

       #logig for executing tasks based on query
       if 'wikipedia' in query:
           speak('Searching Wikipedia...')
           query = query.replace("wikipedia","")
           results = wikipedia.summary(query, sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)

       elif 'open youtube' in query:
            webbrowser.open("youtube.com")

       elif 'open google' in query:
            webbrowser.open("google.com")

       elif 'open google' in query:
            webbrowser.open("google.com")

       elif 'play music' in query:
            music_dir ='C:\\Users\\suyog\\musics'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

       elif 'the current time' in query:
           strtime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"sir, the time is {strtime}")

       elif 'open code' in query:
           codePath = "C:\\Users\\suyog\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)

       elif 'email to shelly ' in query:
            try:
                speak('what should I say?')
                content = takeCommand()
                to = "shellyyourEmail@gmail.com"
                sendEmail(to, content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("email was not send... ")

       elif 'computer science department' in query:
           speak ("he Department of Computer Science was established in the year 1999. The Department of Computer Science is well equipped with highly qualified teaching faculty to impart budding technocrats an insight into the world of computers, its applications, and latest developments in the industry, through professional engagements,Computer Science is a three-year undergraduate degree course that deals with the principles and applications of the computer.The program creates opportunities of hands-on learning through projects and gives knowledge and practical experience of the latest technologies.  ")
        
       elif 'head of department' in query:
           speak (" miss Suchita Revankar is the head of SIWS computer science department. and their qualifications are M Sc (Electronics), M Phil  (I T), Diploma in Cyber Law ")
       
       elif 'shraddha' in query:
         speak ("miss Shraddha Kshirsagar is currently teaching in SIWS college as an Assistant Professor , her qualifications are MSc. Computer Science. and Masters in computer applications ")

       elif 'muskan' in query:
          speak (" miss muskaan kursija is currently teaching in SIWS college as a assistant professor and her qualification is M Sc (I.T.) ")

       elif 'ruhi' in query:
          speak ("miss Ruuhe is currently teaching in SIWS college as an Assistant Professor , her qualifications are MSc. Computer Science. and Masters in computer applications ")

       elif 'madhu' in query:
          speak ("miss Madhu is currently teaching in SIWS college as an Assistant Professor , her qualifications are MSc. Computer Science. and Masters in computer applications ")

       elif 'quit' in query or 'goodbye' in query:
          speak (" quitting sir . thankyou for your time ")
          exit()

       rollnumbers = []