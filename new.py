# # import speech_recognition as sr
# # import pyttsx3

# # engine = pyttsx3.init()
# # recognizer = sr.Recognizer()

# # def speak(text):
# #     engine.say(text)
# #     engine.runAndWait()

# # def listen(timeout=5, phrase_time=3):
# #     with sr.Microphone() as source:
# #         print("Listening...")
# #         recognizer.adjust_for_ambient_noise(source, duration=0.5)
# #         audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time)
# #     return audio

# # if __name__ == "__main__":
# #     speak("Initializing Jarvis")

# #     while True:
# #         try:
# #             audio = listen(timeout=5, phrase_time=3)
# #             word = recognizer.recognize_google(audio)
# #             print("Heard:", word)

# #             if "jarvis" in word.lower():
# #                 speak("Yes, I am listening")

# #                 audio = listen(timeout=5, phrase_time=5)
# #                 command = recognizer.recognize_google(audio)
# #                 print("Command:", command)
# #                 speak(f"You said {command}")

# #         except sr.WaitTimeoutError:
# #             print("No speech detected")

# #         except sr.UnknownValueError:
# #             print("Could not understand audio")

# #         except sr.RequestError as e:
# #             print("API error:", e)

import pyttsx3

engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 170)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

engine.say("Jarvis test successful")
engine.runAndWait()

# import speech_recognition as sr
# import pyttsx3
# import time

# recognizer = sr.Recognizer()

# engine = pyttsx3.init("sapi5")
# engine.setProperty("rate", 170)

# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()
#     engine.stop()   # 🔑 important

# def listen(timeout=5, phrase_time=3):
#     with sr.Microphone() as source:
#         recognizer.adjust_for_ambient_noise(source, duration=0.5)
#         print("Listening...")
#         audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time)
#     return audio

# if __name__ == "__main__":
#     speak("Initializing Jarvis")
#     time.sleep(0.5)

#     while True:
#         try:
#             audio = listen(5, 3)
#             word = recognizer.recognize_google(audio)
#             print("Heard:", word)

#             if "jarvis" in word.lower():
#                 speak("Yes")
#                 time.sleep(0.3)

#                 audio = listen(5, 5)
#                 command = recognizer.recognize_google(audio)
#                 print("Command:", command)
#                 speak(f"You said {command}")

#         except sr.UnknownValueError:
#             print("Didn't understand")

#         except sr.WaitTimeoutError:
#             print("No speech")

#         except sr.RequestError as e:
#             print("API error:", e)


# import speech_recognition as sr
# import pyttsx3
# import time

# recognizer = sr.Recognizer()

# def speak(text):
#     engine = pyttsx3.init("sapi5")   # 🔑 re-init every time
#     engine.setProperty("rate", 170)
#     voices = engine.getProperty("voices")
#     engine.setProperty("voice", voices[0].id)
#     engine.say(text)
#     engine.runAndWait()
#     engine.stop()

# def listen(timeout=5, phrase_time=3):
#     with sr.Microphone() as source:
#         recognizer.adjust_for_ambient_noise(source, duration=0.4)
#         print("Listening...")
#         audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time)
#     return audio   # mic is now fully released

# if __name__ == "__main__":
#     speak("Initializing Jarvis")
#     time.sleep(0.6)

#     while True:
#         try:
#             audio = listen(5, 3)
#             word = recognizer.recognize_google(audio)
#             print("Heard:", word)

#             if "jarvis" in word.lower():
#                 time.sleep(0.4)    # 🔑 let Windows release audio device
#                 speak("Yes")

#                 audio = listen(5, 5)
#                 command = recognizer.recognize_google(audio)
#                 print("Command:", command)
#                 speak(f"You said {command}")

#         except sr.WaitTimeoutError:
#             print("No speech")

#         except sr.UnknownValueError:
#             print("Could not understand")

#         except sr.RequestError as e:
#             print("API error:", e)

