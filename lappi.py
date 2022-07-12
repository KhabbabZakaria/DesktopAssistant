# importing libraries 
from functions import *
import pyttsx3

import time
from pygame import mixer

import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
r = sr.Recognizer()

def runBeep():
   mixer.init()
   mixer.music.load("C:\\Users\\zakar\\OneDrive\\Desktop\\Desktop Assistant\\Lappi.mp3")
   mixer.music.play()
   while mixer.music.get_busy():  # wait for music to finish playing
      time.sleep(1)

while True:
   try:
      with sr.Microphone() as source:
         # read the audio data from the default microphone
         audio_data = r.record(source, duration=4)
         print("Recognizing...")
         # convert speech to text
         text = r.recognize_google(audio_data)
         print(text)
         if "hey lappi" in text or "lappi" in text or "lappy" in text or "hey" in text:
            runBeep()
            if 'open' in text:
               index = text.index('open')
            f = text[index+5:]
            voice = openFile(f)
            engine = pyttsx3.init()
            engine.say(voice)
            engine.runAndWait()
         if 'search for' in text:
            runBeep()
            index = text.index('for')
            voice = text[index+4:]
            openWebPage(voice)

         if 'tell' in text and 'joke' in text:
            tellJoke()

         '''else:
               print('False')'''
   except:
      continue