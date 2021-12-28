import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') #sapi5 is microsoft API for speech recognition
voices = engine.getProperty('voices') #configuring system inbuilt voice
engine.setProperty('voice', voices[0].id) #voices[0] for male and voices[1] for female
# print(voices[1])
#contact is data base for mails
contact = {
    "bella": "aakanksha8826@gmail.com",
    "hulk": "utkarshtyagi.ut12@gmail.com",
    "darshika": "darshikasrivastava29@gmail.com"
}
def speak(audio): #audio will be spoken
    engine.say(audio)
    engine.runAndWait()
def wish(): #wishing the user
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<= 12:
        speak("Good morning")
    elif hour>12 and hour<=18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak(" i am jarvis sir, how i can help you today?")
def CommandME():
    #it takes input from user by microphone and return string
    r = sr.Recognizer() #recognizer is class which have various controlling attributes
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #google API is used for voice recognition
        print("User said: ",query)
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query
def Email_send(to,context):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('enter id you want to send email with','enter the pasword')
    server.sendmail('enter id you want to send email with', to, context)
    server.close()

if __name__ == '__main__':
    wish()
    while(True):
        query = CommandME().lower() #logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir= 'C:\\Users\\darshika\\Music'
            songs= os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[2]))
        elif 'the time' in query:
            timenow= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {timenow}")
        elif 'open code' in query:
            dpath= "C:\\Users\\darshika\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #path of the file you want to open
            os.startfile(dpath)
        elif 'send email' in query:
            try:
                speak("who you want to send email?")
                person = CommandME()
                to = contact[person]
                speak("what you want to send?")
                context = CommandME()
                Email_send(to, context)
                speak("the email is send, do you want any more help?")
            except Exception as e:
                print(e)
                speak("Email not sent, please try again")

        elif 'thank you jarvis' in query:
            speak("welcome, jarvis signing off")
            break








