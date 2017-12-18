#!/usr/bin/env python3

import speech_recognition as sr
import sphinxbase
import pocketsphinx
import logging
from datetime import datetime 
import os
from os import path

# Total Time
startTime = datetime.now()

# Find current directory
dir_path = os.path.dirname(os.path.realpath(__file__))

# Due to google's speech recognition api limitation we have to split audio
# the folder of the splitted audio
folder = dir_path+'/parts/'

# Iterate over files in directory
for root, dirs, filenames in os.walk(folder):
    for f in sorted(filenames):
        fileProccessTime= datetime.now() 
        AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), 'parts/'+f)

        # Get the name of the clip
        textFile = f.split(".")[0]

        r = sr.Recognizer()

        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  
            # read the entire audio file

            # recognize speech using Sphinx
            # try:
            #      # The file which we will write to
            #     fileName = 'output.txt'
            #     with open(fileName, "a+") as myfile:
            #         myfile.write("Audio Input:" +textFile + "\n")
            #         myfile.write(r.recognize_sphinx(audio) + "\n")
            #     print("Sphinx thinks you said " + r.recognize_sphinx(audio))
            # except sr.UnknownValueError:
            #     print("Sphinx could not understand audio")
            # except sr.RequestError as e:
            #     print("Sphinx error; {0}".format(e))
            # logging.info('recognize speech using Google Speech Recognition') 
            try:
                # The file which we will write to
                fileName = 'output.txt'
                with open(fileName, "a+") as myfile:
                    myfile.write("Audio Input:" +textFile + "\n")
                    myfile.write(r.recognize_google(audio) + "\n")
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

            totalFileTime = datetime.now() - fileProccessTime
            print('Time elpased (hh:mm:ss.ms) {}'.format(totalFileTime))

totalTime=datetime.now()-startTime 
print('Time elpased (hh:mm:ss.ms) {}'.format(totalTime))