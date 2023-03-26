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
from datetime import date

import wikipedia
import wikipedia_2_oop

class Jarvis:
    def __init__(self) -> None:
        # Create object
        self.r = sr.Recognizer()
        
        self.today = date.today()  # Get today's date and time
        
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
        
    def menu(self):
        """
            Choose an option below:
            1. Wikipedia
            2. Quit
        """    
    
    def take_user_input(self):
        """Recognize user voice input using Speech Recognition
        module, converts it to text.
        """
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
                
                if self.query == "what is today":   # JARVIS tells me today's date
                    self.engine.say(self.today)
                    print(self.today)
                    self.engine.runAndWait()
                else:    
                    # Have Jarvis repeat the word(s)
                    self.engine.say(self.query)
                    self.engine.runAndWait()
                
            except sr.UnknownValueError:
                print('Google Speech Recognition could not understand audio')
                self.engine.say("I didn't understand what you said.")
                
            except sr.RequestError as e:
                # if there was an error communicating with Google Speech
                print(f"Google Speech did not respond: {e}")
                self.engine.say("I didn't understand what you said.")       
            
            except:
                self.engine.say("I didn't recogize what you said.")
                print("I didn't recognize what you said.")
                
    def voice_commands(self):
        if self.query == "quit":
            print("Goodbye")
            exit()

jarvis = Jarvis()
while True:
    jarvis.take_user_input()
    jarvis.voice_commands()