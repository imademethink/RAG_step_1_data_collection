from gtts import gTTS
import os

# Audio Generation and Synthesis:
#       Use generative AI models to create entirely new music or synthesize human-like speech (Text-to-Speech).
# Speech/ Audio to text






# # simple text to speech
# text = "Hello! I am a generative AI voice. How can I help you today?"
# # Initialize the engine and save to file
# tts = gTTS(text=text, lang='en', slow=False)
# tts.save("speech_output.mp3")
#
# # Play the file (OS dependent)
# os.system("start speech_output.mp3")




# simple speech to text
import whisper
from pathlib import Path

# Load the desired model (e.g., 'tiny', 'base', 'small', 'medium', 'large')
# The 'tiny' model is the fastest but less accurate; 'base' is a good balance.
model = whisper.load_model('base')
# Specify your MP3 file path
path_aud1 = "data\\audio\\sample1.wav"

audio_file_path = Path(path_aud1)
# Transcribe the audio file
result = model.transcribe(str(audio_file_path), language='en')
# Print or save the transcribed text
transcribed_text = result["text"]
print("Transcription===>:", transcribed_text)



