import os
from gtts import gTTS
import playsound

class PlaySoundController:

    def conver(self, text):
        try:
            # Define the output file path
            audio_file = "output.mp3"
            

            # Generate speech and save as an MP3
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save(audio_file)

        except PermissionError as e:
            print(f"Permission error: {e}")
        except Exception as e:
            print(f"An error occurred while saving the audio file: {e}")

    def speak_text(self):
        try:
            # Define the file path
            audio_file = "output.mp3"
            
            # Play the audio file
            playsound.playsound(audio_file)
            
            # Optionally, remove the file after playing

        except FileNotFoundError:
            print("Audio file not found!")
        except Exception as e:
            print(f"An error occurred while playing the audio: {e}")
