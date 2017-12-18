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
