from gtts import gTTS

"""
    Convert text to speech and save it as an MP3 file.

    :param text: The text to convert to speech.
    :param lang: The language for the speech (default is English).
    :param filename: The name of the output MP3 file (default is 'output.mp3').
"""

text = "Hello, this is a text-to-speech conversion example."
lang = "en"
filename = "output.mp3"

tts = gTTS(text=text, lang=lang)
tts.save(filename)
print(f"Saved speech to {filename}")


