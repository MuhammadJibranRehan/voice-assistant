# import speech_recognition as sr
# import pyttsx3
# import datetime
# import wikipedia
# import webbrowser
# import os
# import time
# import ecapture as ec

# print('Loading Walmart Siri By M.jibran')

# # Initialize the text-to-speech engine
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
# engine.setProperty('rate', 200)

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def wishMe():
#     hour = datetime.datetime.now().hour
#     if hour >= 0 and hour < 12:
#         speak("Good Morning!")
#     elif hour >= 12 and hour < 18:
#         speak("Good Afternoon!")
#     else:
#         speak("Good Evening!")

# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = r.listen(source)

#         try:
#             statement = r.recognize_google(audio, language='en-in')
#             print(f"user said: {statement}\n")
#         except Exception as e:
#             speak("I didn't hear you, please say that again.")
#             return "none"
#         return statement.lower()

# speak("Loading Walmart Siri By Muhammad jibran")
# wishMe()

# if __name__ == '__main__':  
#     while True:
#         speak("What can I do for you?")
#         statement = takeCommand()
#         if statement == "none":
#             continue

#         if "good bye" in statement or "ok bye" in statement or "turn off" in statement:
#             speak("See you later!")
#             break

#         if 'wikipedia' in statement:
#             speak('Searching in Wikipedia...')
#             statement = statement.replace("wikipedia", "")
#             results = wikipedia.summary(statement, sentences=3)
#             speak("According to Wikipedia")
#             speak(results)

#         elif 'open youtube' in statement:
#             speak('Ok wait youtube is opening')
#             print('Ok wait youtube is opening')
#             webbrowser.open_new_tab("https://youtube.com")
#             speak("YouTube is now open")
#             time.sleep(3)

#         elif 'open google' in statement:
#             speak('Ok wait google is opening')
#             webbrowser.open_new_tab("https://www.google.com")
#             print("Google Chrome is open now")
#             speak("Google Chrome is open now")
#             time.sleep(5)

#         elif 'open gmail' in statement:
#             speak('Ok wait gmail is opening')
#             webbrowser.open_new_tab("https://gmail.com")
#             print("Google Mail is open now")
#             speak("Google Mail is open now")
#             time.sleep(5)

#         # You can add more commands here




import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time

print('Loading Walmart Siri By M.jibran')

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said: {statement}\n")
        except Exception as e:
            speak("I didn't hear you, please say that again.")
            return "none"
        return statement.lower()

speak("Loading Walmart Siri By Muhammad jibran")
wishMe()

if __name__ == '__main__':
    while True:
        speak("What can I do for you?")
        statement = takeCommand()
        if statement == "none":
            continue

        if "good bye" in statement or "ok bye" in statement or "turn off" in statement:
            speak("See you later!")
            break

        if 'wikipedia' in statement:
            speak('Searching in Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in statement:
            speak('Ok wait, YouTube is opening')
            webbrowser.open_new_tab("https://youtube.com")
            speak("YouTube is now open")

        elif 'open google' in statement:
            speak('Ok wait, Google is opening')
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google Chrome is now open")

        elif 'open gmail' in statement:
            speak('Ok wait, Gmail is opening')
            webbrowser.open_new_tab("https://gmail.com")
            speak("Google Mail is now open")
