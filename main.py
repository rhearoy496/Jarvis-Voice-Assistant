import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import time
import musicLibrary
from ai_client import ask_ai
import asyncio
import edge_tts
import tempfile
import os
from playsound import playsound
from dotenv import load_dotenv

load_dotenv()

newsapiKey = os.getenv("NEWS_API_KEY")

recognizer = sr.Recognizer()
# recognizer.pause_threshold = 1   # default ~0.8
# recognizer.energy_threshold = 300
# recognizer.dynamic_energy_threshold = True

# newsapiKey = "cbc1894dcad82d90c900585598d85ad3"

#engine = pyttsx3.init()

# def speak(text) :
#     engine = pyttsx3.init("sapi5")
#     voices = engine.getProperty("voices")
#     engine.setProperty("voice", voices[0].id)  # David
    
#     engine.setProperty("rate", 150)   # slower = deeper feel
#     engine.setProperty("volume", 0.6)
    #engine.setProperty("rate", 210)
    # voices = engine.getProperty("voices")
    # engine.setProperty("voice", voices[0].id)
    # engine.say(text)
    # engine.runAndWait()
    # engine.stop()



async def async_speak(text):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        filename = tmp_file.name

    communicate = edge_tts.Communicate(
        text,
        voice="en-US-GuyNeural",   # Deep male
        rate="-5%",
        pitch="-5Hz"
    )

    await communicate.save(filename)
    playsound(filename)
    os.remove(filename)

def speak(text):
    asyncio.run(async_speak(text))

# def listen(timeout=8):
#     with sr.Microphone() as source:
#         # recognizer.adjust_for_ambient_noise(source, duration=0.4)
#         print("Listening...")
#         audio = recognizer.listen(source, timeout=timeout)
#     return audio

def listen(timeout=10):
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        audio = recognizer.listen(source, timeout=timeout)
    return audio



# def processCommand(c) :
    # print("Command:", c)
    # # speak(f"Understood. I will {c} right now")
    # if "google" in c.lower() :
    #     webbrowser.open("https://www.google.com/")
    # elif "youtube" in c.lower() :
    #     webbrowser.open("https://www.youtube.com/")
    # elif "facebook" in c.lower() :
    #     webbrowser.open("https://www.facebook.com/")
    # # elif c.lower().startswith("play") :
    # #     song = c.lower().split(" ")[1]
    # #     link = musicLibrary.music[song]
    # #     webbrowser.open(link)
    # elif c.lower().startswith("play"):
    #     song = c.lower().replace("play", "").strip()

    # if song in musicLibrary.music:
    #     link = musicLibrary.music[song]
    #     speak(f"Playing {song}")
    #     webbrowser.open(link)
    # else:
    #     speak("Song not found in library")

def processCommand(c):
    print("Command:", c)
    # speak(f"Understood. I will {c} right now")

    if "google" in c.lower():
        webbrowser.open("https://www.google.com/")

    elif "youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")

    elif "facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")

    # elif "news" in c.lower() :
    #     r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapiKey}")
    #     if r.status_code == 200 :
    #         data = r.json()
    #         articles = data.get('articles', [])
    #         for article in articles :
    #             speak(article['title'])

    
    elif "play" in c.lower():
        song = c.lower().replace("play", "").strip()

        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak("Song not found")

    elif "news" in c.lower():
        speak("Fetching the latest news")

        r = requests.get(
        f"https://gnews.io/api/v4/search?q=kolkata&country=in&lang=en&token={newsapiKey}")

        # print("Status code:", r.status_code)

        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])

            if not articles:
                speak("No news articles found")
                return

            for article in articles[:10]:
                print(article["title"])
                speak(article["title"])

        else:
            print("Error response:", r.text)
            speak("I could not fetch the news")
    else : #let AI handle the request
        speak("Hmm..Thinking...")
        reply = ask_ai(c)
        print(reply)
        speak(reply)

    

if __name__ == "__main__" :
    speak("Initializing....")
    speak("Hello I am Jarvis!")

    assistant_active = False
    last_interaction_time = 0

    while True:
        try:
            audio = listen(timeout=10)
            text = recognizer.recognize_google(audio, language="en-US").lower()
            # print("Heard:", text)

            # Wake word detection
            if not assistant_active:
                if "jarvis" in text:
                    assistant_active = True
                    print("Jarvis is active")
                    speak("Yes?")
                    last_interaction_time = time.time()
                continue

            # If already active → process command directly
            processCommand(text)
            last_interaction_time = time.time()

            # Auto sleep after 30 seconds of inactivity
            if time.time() - last_interaction_time > 30:
                assistant_active = False
                print("Jarvis is sleeping")
                speak("Going back to sleep.")

        except sr.UnknownValueError:
            print("Speak clearly...")

        except sr.WaitTimeoutError:
            print("Waiting for speech...")

    # while True:
    #     #Listen for the word Jarvis
    #     #obtain audio from microphone
    #     #r = sr.Recognizer()
    #     print("recognizing...")
    #     try:
    #         with sr.Microphone() as source:
    #             #recognizer.adjust_for_ambient_noise(source, duration=1)
    #             audio = listen()
    #             word = recognizer.recognize_google(audio)
            
    
    #         if "jarvis" in word.lower() :
    #             # time.sleep(0.4)
    #             speak("Yes..?")
    #             print("Waiting for command...")
    #             audio = listen()
    #             command = recognizer.recognize_google(audio)
    #             processCommand(command)
                
            
        
    #     except sr.WaitTimeoutError:
    #         print("Say Jarvis to start..")

    #     except sr.UnknownValueError:
    #         print("Say Jarvis to start....")

    #     except sr.RequestError as e:
    #         print("API error:", e)







