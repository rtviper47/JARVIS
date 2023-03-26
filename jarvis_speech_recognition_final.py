"""
    Name: jarvis_speech_recognition_final.py
    Purpose: Voice recognition from Google
    JARVIS repeats words you say
    Have Jarvis say today's date when you ask what is today
"""

# pip install SpeechRecognition
from sys import exit
import speech_recognition as sr

# pip install pyttsx3 for text to speech
import pyttsx3

# To get today's date and time
# Examples taken from:
# https://www.programiz.com/python-programming/datetime/current-datetime
from datetime import date
from datetime import datetime

import wikipedia 

class Jarvis:
    def __init__(self) -> None:
        # Create object
        self.r = sr.Recognizer()
        
        self.today = date.today()   # For Jarvis to say today's date
        self.dt = datetime.now()  # Get today's date and time for printing
        
        # Textual month, day and year for printing
        self.date = self.today.strftime("%B %d, %Y")
        self.time = self.dt.strftime("%H:%M:%S")
        
        """
            Initialize jarvis tts
        """
        # Change these constants to experiment with the speech engine
        RATE = 150  # integer default 200 wpm
        VOLUME = 0.9    # float 0.0-1.0 inclusive default 1.0
        VOICE = 1       # Set 1 for Zira (female), 0 for David (male)
        # Initialize the pyttsx3 voice engine
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", RATE)        # Speed for wpm
        self.engine.setProperty("volume", VOLUME)    # Volume 0.0 - 1.0
        # Retrieve all available voices from your system into a list
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[VOICE].id)
        self.engine.runAndWait()
    
    def take_user_input(self):
        """
            Recognize user voice input using Speech Recognition
            module, converts it to text.
        """
        print( "-" * 30)
        # JARVIS says "Hello today is + date_and_time"
        self.engine.say(f"Hello, it is {self.today}")
        print(self.date)
        print(self.time)
        self.engine.runAndWait()
        
        # Have Jarvis list the menu items
        self.menu()
        
        # with your local microphone as the source
        with sr.Microphone() as source:
            print("Listening...")
            self.r.pause_threshold = 1
            # Start listening for speech
            audio = self.r.listen(source)
            
            try:
                print('Recognizing...')
                # Capture the recognized word in a string variable
                recognized_words = self.r.recognize_google(
                    audio, language='en-US', show_all=True)
                # Google Speech Recognition returns a list of dictionaries
                # Pull only the transcript with the highest confidence
                self.query = recognized_words['alternative'][0]['transcript']
                print(self.query)
                
                if self.query == "one" or "wikipedia":
                    
                    self.engine.runAndWait()
                else:    
                    # Have Jarvis repeat the word(s)
                    self.engine.say(self.query)
                    self.engine.runAndWait()
                
            except sr.UnknownValueError:
                print('Google Speech Recognition could not understand audio')
                self.engine.say("I didn't understand what you said.")
                self.engine.runAndWait()
                
            except sr.RequestError as e:
                # if there was an error communicating with Google Speech
                print(f"Google Speech did not respond: {e}")
                self.engine.say("I didn't recognize what you said.")
                self.engine.runAndWait()       
            
            except:
                self.engine.say("I didn't recognize what you said.")
                print("I didn't recognize what you said.")
                self.engine.runAndWait()
                
    def voice_commands(self):
        if self.query == "quit":
            print("Goodbye")
            exit()
        
    def menu(self):
        self.engine.say("Choose an option from the menu")
        print("Choose an option from the menu: ")
        self.engine.say("Wikipedia")
        print("1. Wikipedia")
        self.engine.say("Quit")
        print("2. Quit")
        self.engine.runAndWait()

jarvis = Jarvis()
while True:
    jarvis.take_user_input()
    jarvis.voice_commands()