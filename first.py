# Problem 1. 
#  Multiline Strings (Printing Multiple Lines Together)

print('''
      Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.

Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.''')

# Problem 2.
#Install an External Module and use it to perform an opration 
import pyttsx3
engine = pyttsx3.init()
engine.say("Poem completed!")
engine.runAndWait()


#Problem 3. 
#Program to print contents of a directory using OS Module
import os

# Specify the directory path
path = "/"

# Print all files and folders in the directory
for item in os.listdir(path):
    print(item)

