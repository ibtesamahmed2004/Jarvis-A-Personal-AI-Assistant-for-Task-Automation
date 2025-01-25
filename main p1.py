import speech_recognition as sr

import webbrowser

import pyttsx3

import musicLibrary

import requests

from openai import OpenAI

from gtts import gTTS

import pygame

import os



recognizer = sr.Recognizer()
engine = pyttsx3.init() 
newsapi = "150dfeb571144e6f82e8c88c5305b484"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 
    
    
    pygame.mixer.init()
    
    pygame.mixer.music.load('temp.mp3')
    
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 
    
    
    
def aiProcess(command):
    client = OpenAI(api_key="<I dont have an API Key for now, if you have then paste the key over here>",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )
    
    return completion.choices[0].message.content



def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
        
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
        
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
        
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
        
    elif "open snapchat" in c.lower():
        webbrowser.open("https://www.snapchat.com")
        
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
        
    elif "open spotify" in c.lower():
        webbrowser.open("https://www.spotify.com")
        
    elif "open amazon" in c.lower():
        webbrowser.open("www.amazon.com")
        
    elif "open flipkart" in c.lower():
        webbrowser.open("www.flipkart.com")
        
    elif "open netflix" in c.lower():
        webbrowser.open("www.netflix.com")
        
    elif "open amazon prime video" in c.lower():
        webbrowser.open("www.primevideo.com")
        
    elif "open twitter (X)" in c.lower():
        webbrowser.open("www.x.com")
        
    elif "open telegram" in c.lower():
        webbrowser.open("www.telegram.org")
        
    elif "open phonepe" in c.lower():
        webbrowser.open("www.phonepe.com")
        
    elif "open google pay" in c.lower():
        webbrowser.open("pay.google.com")
        
    elif "open uber" in c.lower():
        webbrowser.open("www.uber.com")
        
    elif "open ola" in c.lower():
        webbrowser.open("www.olacabs.com")
        
    elif "open rapido" in c.lower():
        webbrowser.open("www.rapido.bike")
        
    elif "open google maps" in c.lower():
        webbrowser.open("maps.google.com")
        
    elif "open weather forecast" in c.lower():
        webbrowser.open("www.weather.com")
        
    elif "open google photos" in c.lower():
        webbrowser.open("photos.google.com")
    
        
    elif "open money control" in c.lower():
        webbrowser.open("https://www.moneycontrol.com")
        
    elif "open swiggy" in c.lower():
        webbrowser.open("www.swiggy.com")
        
    elif "open zomato" in c.lower():
        webbrowser.open("www.zomato.com")
        
    elif "open microsoft teams" in c.lower():
        webbrowser.open("https://www.microsoft.com/en/microsoft-teams/group-chat-software")
        
    elif "open google drive" in c.lower():
        webbrowser.open("https://drive.google.com")
        
    elif "open microsoft office" in c.lower():
        webbrowser.open("https://www.office.com")
        
    elif "open notion" in c.lower():
        webbrowser.open("https://www.notion.so")
        
    elif "open google fit" in c.lower():
        webbrowser.open("https://www.google.com/fit")
        
    elif "open paytm" in c.lower():
        webbrowser.open("https://www.paytm.com")
        
    elif "open google news" in c.lower():
        webbrowser.open("https://news.google.com")
        
    elif "open razor pay" in c.lower():
        webbrowser.open("https://www.razorpay.com")
        
    elif "open udemy" in c.lower():
        webbrowser.open(" www.udemy.com")
        
    elif "open coursera" in c.lower():
        webbrowser.open("www.coursera.org")
        
    elif "open gmail" in c.lower():
        webbrowser.open("https://mail.google.com")
        
        
        
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link) 
        
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            
            data = r.json()
            
            
            articles = data.get('articles', [])
            
            
            for article in articles:
                speak(article['title'])

    else:
        
        output = aiProcess(c)
        speak(output) 






if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                
                with sr.Microphone() as source:
                    print("Jarvis Actived...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            
            print("Error; {0}".format(e))