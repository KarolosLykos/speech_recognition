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
* **PyAudio** 0.2.11+ (required only if you need to use microphone input, ``Microphone``)
* **PocketSphinx** (required only if you need to use the Sphinx recognizer, ``recognizer_instance.recognize_sphinx``)
* **Google API Client Library for Python** (required only if you need to use the Google Cloud Speech API, ``recognizer_instance.recognize_google_cloud``)
* **FLAC encoder** (required only if the system is not x86-based Windows/Linux/OS X)

The following requirements are optional, but can improve or extend functionality in some situations:

* On Python 2, and only on Python 2, some functions (like ``recognizer_instance.recognize_bing``) will run slower if you do not have **Monotonic for Python 2** installed.
* If using CMU Sphinx, you may want to `install additional language packs <https://github.com/Uberi/speech_recognition/blob/master/reference/pocketsphinx.rst#installing-other-languages>`__ to support languages like International French or Mandarin Chinese.

The following sections go over the details of each requirement.

Python
~~~~~~

The first software requirement is `Python 2.6, 2.7, or Python 3.3+ <https://www.python.org/download/releases/>`__. This is required to use the library.

PyAudio (for microphone users)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`PyAudio <http://people.csail.mit.edu/hubert/pyaudio/#downloads>`__ is required if and only if you want to use microphone input (``Microphone``). PyAudio version 0.2.11+ is required, as earlier versions have known memory management bugs when recording from microphones in certain situations.

If not installed, everything in the library will still work, except attempting to instantiate a ``Microphone`` object will raise an ``AttributeError``.

The installation instructions on the PyAudio website are quite good - for convenience, they are summarized below:

* On Windows, install PyAudio using `Pip <https://pip.readthedocs.org/>`__: execute ``pip install pyaudio`` in a terminal.
* On Debian-derived Linux distributions (like Ubuntu and Mint), install PyAudio using `APT <https://wiki.debian.org/Apt>`__: execute ``sudo apt-get install python-pyaudio python3-pyaudio`` in a terminal.
    * If the version in the repositories is too old, install the latest release using Pip: execute ``sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && sudo pip install pyaudio`` (replace ``pip`` with ``pip3`` if using Python 3).
* On OS X, install PortAudio using `Homebrew <http://brew.sh/>`__: ``brew install portaudio``. Then, install PyAudio using `Pip <https://pip.readthedocs.org/>`__: ``pip install pyaudio``.
* On other POSIX-based systems, install the ``portaudio19-dev`` and ``python-all-dev`` (or ``python3-all-dev`` if using Python 3) packages (or their closest equivalents) using a package manager of your choice, and then install PyAudio using `Pip <https://pip.readthedocs.org/>`__: ``pip install pyaudio`` (replace ``pip`` with ``pip3`` if using Python 3).

PyAudio `wheel packages <https://pypi.python.org/pypi/wheel>`__ for common 64-bit Python versions on Windows and Linux are included for convenience, under the ``third-party/`` `directory <https://github.com/Uberi/speech_recognition/tree/master/third-party>`__ in the repository root. To install, simply run ``pip install wheel`` followed by ``pip install ./third-party/WHEEL_FILENAME`` (replace ``pip`` with ``pip3`` if using Python 3) in the repository `root directory <https://github.com/Uberi/speech_recognition>`__.

PocketSphinx-Python (for Sphinx users)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`PocketSphinx-Python <https://github.com/bambocher/pocketsphinx-python>`__ is **required if and only if you want to use the Sphinx recognizer** (``recognizer_instance.recognize_sphinx``).

PocketSphinx-Python `wheel packages <https://pypi.python.org/pypi/wheel>`__ for 64-bit Python 2.7, 3.4, and 3.5 on Windows are included for convenience, under the ``third-party/`` `directory <https://github.com/Uberi/speech_recognition/tree/master/third-party>`__. To install, simply run ``pip install wheel`` followed by ``pip install ./third-party/WHEEL_FILENAME`` (replace ``pip`` with ``pip3`` if using Python 3) in the SpeechRecognition folder.

On Linux and other POSIX systems (such as OS X), follow the instructions under "Building PocketSphinx-Python from source" in `Notes on using PocketSphinx <https://github.com/Uberi/speech_recognition/blob/master/reference/pocketsphinx.rst>`__ for installation instructions.

Note that the versions available in most package repositories are outdated and will not work with the bundled language data. Using the bundled wheel packages or building from source is recommended.

See `Notes on using PocketSphinx <https://github.com/Uberi/speech_recognition/blob/master/reference/pocketsphinx.rst>`__ for information about installing languages, compiling PocketSphinx, and building language packs from online resources. This document is also included under ``reference/pocketsphinx.rst``.

Google API Client Library for Python (for Google Cloud Speech API users)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Google API Client Library for Python <https://developers.google.com/api-client-library/python/>`__ is required if and only if you want to use the Google Cloud Speech API (``recognizer_instance.recognize_google_cloud``).

If not installed, everything in the library will still work, except calling ``recognizer_instance.recognize_google_cloud`` will raise an ``RequestError``.

According to the `official installation instructions <https://developers.google.com/api-client-library/python/start/installation>`__, the recommended way to install this is using `Pip <https://pip.readthedocs.org/>`__: execute ``pip install google-api-python-client`` (replace ``pip`` with ``pip3`` if using Python 3).

Alternatively, you can perform the installation completely offline from the source archives under the ``./third-party/Source code for Google API Client Library for Python and its dependencies/`` directory.
