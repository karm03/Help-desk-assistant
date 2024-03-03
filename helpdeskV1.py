import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import smtplib
import ssl
import wikipedia
import mysql.connector
from email.message import EmailMessage


leave_and_off_days = [
    "2023-09-23",
    "2023-10-02",
    "2023-12-25",
]

def check_calendar():
    today_date = datetime.datetime.now().date().strftime('%Y-%m-%d')
    
    if today_date in leave_and_off_days:
        talk("Today is a leave or off day. Enjoy your day off!")
    else:
        talk("Today is a regular working day.")


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 150)

email_sender = 'karmbhatt819@gmail.com'
email_password = 'fakeaccount0101'
email_receiver = "karmbhatt9429234@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 465  
app_pass = 'edax xdkn dngc epnu'

def email(text):
    subject = 'Regarding Leave application '
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(text)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as smtp:
        smtp.login(email_sender, app_pass)
        smtp.sendmail(email_sender, email_receiver,em.as_string())
        smtp.quit()
        talk("Email sent successfully")

def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        talk("Good morning sir! I'm your help desk assistant!")
    elif hour>=12 and hour<18:
        talk("Good afternoon sir I'm your help desk assistant!")
    else:
        talk("Good evening sir! I'm your help desk assistant!")

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source,timeout=7, phrase_time_limit=7)
            command = listener.recognize_google(voice)
            command = command.lower()
            return command

    except: 
        print("PLease repeat your command")      
        return None
     

def request_leave():
    talk('Sure! Can you please tell me the reason for your leave?')
    
    
    with sr.Microphone() as source:
        print("Listening for reason...")
        voice = listener.listen(source, timeout=7, phrase_time_limit=7)
        reason = listener.recognize_google(voice)
        reason = reason.lower()
        print("Reason for leave:", reason)
        #TODO: yes/no/modify-
        email(reason)
    
def play_music():
    webbrowser.open("https://open.spotify.com")


def run_alexa():
    command = take_command()
    print(command)
    

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)

    elif 'yearly' in command:
        check_calendar()

    elif 'manager cabin' in command:
        talk('Sure!')
        talk("The manager's cabin is located on first floor! cabin number 02.")
        

    elif 'request leave' in command:
         request_leave() 
         #email(command)
         
         
    elif 'gmit website' in command:
        talk('Sure!')
        webbrowser.open("https://newsite.gmit.edu.in")

    elif 'youtube' in command:
        talk('Sure!')
        webbrowser.open("https://www.youtube.com")

    elif 'need help' in command:
        talk('Sure!')
        talk('You can ask mr xyz he can help you with your concern. You can contact him in his cabin 03 at first floor next to managers cabin thank you!')

    elif 'about' in command:
        talk('Sure!')
        talk('The Gyanmanjari Institute of Technology has been found with sole purpose to create world class engineers for converting global challenges into opportunities through “Value Embedded Quality Technical Education”')
        talk('You can visit our website for more details let me open the website')
        webbrowser.open("https://newsite.gmit.edu.in/")

    elif 'wikipedia' in command:
        person = command.replace('tell me', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)

    elif 'play music' in command:
        play_music()

        
    if 'search' in command:
        # Extracting the query from the command
        query = command.replace('search', '')
        search_google(query)
        
    else:
        talk('please repeat the command again!')


def search_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)


if __name__ == '__main__':
    wishme()
    talk("How may I help you?")
    #while 1:
    run_alexa()