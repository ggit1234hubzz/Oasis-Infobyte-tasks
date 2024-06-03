import streamlit as st
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import cv2

#Setup
print('Your personal assistant at service')
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
def speak(text):
    engine.say(text)
    engine.runAndWait()
#Function to wish based on current time
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
#Taking user command
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Capturing...")
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")
        except Exception as e:
            speak("Pardon me,could you please say that again")
            return "None"
        return statement
speak("Your personal assistant at service")
wishMe()
#main
if __name__=='__main__':
    while True:
        speak("Please tell me whatcan I do for you?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        #Stopping the assistant on bye and stop commands
        if "good bye" in statement or "ok bye" in statement or "stop" in statement or "bye" in statement:
            speak('shutting down,Good bye')
            print('shutting down,Good bye')
            break
        #Searching wikipedia for any input
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            if len(statement) !=0:
                try:
                    results = wikipedia.summary(statement, sentences=3)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except wikipedia.exceptions.DisambiguationError as e:
                    print("Error: {0}".format(e))
            else:
                speak("No search command")
            time.sleep(3)
        #Opening youtube
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)
        #Opening google
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)
        #Opening gmail
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
        #Telling the weather with API form open weather map for city name
        elif "weather" in statement:
            api_key="109419feee88a944945869eab5d04d1e"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
        
            if x["cod"]!="404":
                y=x["main"]
                kelvin_temperature = y["temp"]
                celcius_temperature =round(kelvin_temperature - 273.15,2)
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = x["weather"][0]["description"]
                speak(" Temperature in celcius unit is " +
                     str(celcius_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidity) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in celcuis unit = " +
                      str(celcius_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidity) +
                      "\n description = " +
                      str(weather_description))
            else:
                speak(" City Not Found ")
                continue
        #Saying the time
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        #Answering to some basic questions
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am a personal assistant who is programmed to perform tasks like'
                  'opening google,youtube,google chrome,gmail ,tell time,search wikipedia,tell weather' 
                  'in different cities , get top headline news from times of india and you can ask computational or geographical questions with ask command!')
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Raaga Priya")
            print("I was built by Raaga Priya")
        #Telling the news 
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://www.bbc.co.uk/news/world")
            speak('Here are some headlines from the BBC for you to read')
            time.sleep(6)
        #opening google chrome for user to search on search command
        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
        #Answering computational and geographical question with ask command from wolfrmaalpha api
        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="RUU6X5-65PW3Y9PYW"
            client = wolframalpha.Client('RUU6X5-65PW3Y9PYW')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
time.sleep(3)