# 3. Install an external module and use it to perform an operation of your interest

import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Try voices[1].id if 0 doesn't work
engine.say("hi vivek")
engine.runAndWait()

