# speech_recognition
A first attempt to python and speech recognition

Installing
----------

First, make sure you have all the requirements listed in the "Requirements" section. 

The easiest way to install this is using ``pip install SpeechRecognition``.

Otherwise, download the source distribution from `PyPI <https://pypi.python.org/pypi/SpeechRecognition/>`__, and extract the archive.

In the folder, run ``python setup.py install``.

Requirements
------------

To use all of the functionality of the library, you should have:

* **Python** 2.6, 2.7, or 3.3+ (required)
* **PocketSphinx** (required only if you need to use the Sphinx recognizer, ``recognizer_instance.recognize_sphinx``)
* **Google API Client Library for Python** (required only if you need to use the Google Cloud Speech API, ``recognizer_instance.recognize_google_cloud``)
* **FLAC encoder** (required only if the system is not x86-based Windows/Linux/OS X)


Running
------------

First,  make sure you input audio file is in .wav,flac format
In linux you can convert your audio files with the following command
``ffmpeg -i inp0ut.* input.wav``

if you use the google api there is a limit one the requests.
So you have to split the audio.(here we split the file in 10 seconds parts)
In linux you can do this with the command
``ffmpeg -i input.wav -f segment -segment_time 10 -c copy parts/%03d.wav``
