from unittest import result
import pyttsx3
import wikipedia


# let name of our assistance  will be 'chris'

chris = pyttsx3.init()

In = input("Search wikipedia/google: ")
result = wikipedia.summary(In, sentences=2)
print(result)
chris.say(result)
chris.runAndWait()
