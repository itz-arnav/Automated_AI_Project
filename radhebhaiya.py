import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init() 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)



def voicechange():
    voice = engine.getProperty('voices')
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    newVoiceRate = 170
    engine.setProperty('rate',newVoiceRate)



def date():
    Year = datetime.datetime.now().year
    Month = datetime.datetime.now().month
    Day = datetime.datetime.now().day
    speak("The present day is {} and the month is {} and the year is {}".format(Day,Month,Year))  



def greet():
    speak("Raadhey Bhaiyya aapki kiya sayvaa kar sakta hai?")



def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        speak(query)
    except Exception as e:
        print(e)
        speak("Unable to recognize sir")
        return "None"
    
    return query



def sendemail(to = "arnavjha07@gmail.com", content = "Python se mail"):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("priyanshurcciit@gmail.com","CSE2019/101")
    server.sendmail("priyanshurcciit@gmail.com",to,content)
    server.close()
    
    
    
def screenshot():
     img =pyautogui.screenshot()
     img.save("C://Users//arnav//Music//RADHE_BHAIYA//SS.png")
     
     
def stats():
    usage = str(psutil.cpu_percent())  
    speak("CPU is at : " + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at : " + str(battery.percent))
    
def jokes():
    speak(pyjokes.get_joke())

   
if __name__ == '__main__':

    voicechange()
    greet()
    engine.runAndWait()
    
    while True:
        query = takecommand().lower()
        
        if "time" in query:
            time()
            
            
        elif "date" in query:
            date()
        
        
        elif "wikipedia" in query:
            speak("Searching")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
            
            
        elif "email" in query:
            speak("What should be the content of the email?")    
            result = takecommand().lower()
            sendemail(content = result)
            speak("Email sent successfully")
            
            
        elif "google" in query:
            speak("What should I search sir?")
            chromepath = "C://Program Files//Google//Chrome//Application//chrome.exe %s"
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
            
            
        elif "song" in query:
            songs_dir = "C:/Users/arnav/Music/PYTHON_MUSIC"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
        
        
        elif "remember" in query:
            speak("What should I remember?")
            data = takecommand()
            remember = open("data.txt","w")  
            remember.write(data) 
            remember.close()
            speak("You said me to remember ")
            speak(data)
            
            
        elif "recall" in query:
              remember = open("data.txt","r")  
              speak("You told me to remember " + remember.read())
            
              
        elif "screenshot" in query:
            screenshot()
            speak("Ho gaayaa bhaii")      
              
        
        elif "cpu" in query:
            stats()
            
        elif "joke" in query:
            jokes()    
              
        elif "exit" in query:
            break 
        
        elif "logout" in query:
            os.system("shutdown - l")    
        
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
            
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        else:
            speak("Could you repeat that again?")

