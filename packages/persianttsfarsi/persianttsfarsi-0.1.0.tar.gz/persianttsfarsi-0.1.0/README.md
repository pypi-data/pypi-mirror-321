# PersianTTS

PersianTTS is a Python library for text-to-speech (TTS) synthesis in Persian using Microsoft Azure's speech service. It provides an easy-to-use interface for generating audio files from Persian text with options for voice selection, pitch, rate, and volume adjustment.

# Installation

pip install persianttsfarsi


# Usage

from persianttsfarsi import PersianTTS

tts = PersianTTS()
tts.synthesize("سلام دنیا! این یک مثال از تبدیل متن به گفتار فارسی است.", "output.mp3")
