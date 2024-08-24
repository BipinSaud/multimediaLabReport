#text to speech
from gtts import gTTS
import os

# Define the text to be spoken
text = "Neelam Bista"

# Create a gTTS object
tts = gTTS(text=text, lang='en')

# Save the audio to a file
tts.save("output.mp3")

# Play the saved audio file (using afplay on macOS)
os.system("afplay output.mp3")

# Optionally, remove the saved audio file
os.remove("output.mp3")
