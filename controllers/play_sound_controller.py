from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.playback import play
import io
import playsound

class PlaySoundController:

    def conver(self, text):
        
            # Generate speech in memory
            tts = gTTS(text=text, lang='en', slow=False)
            
            # Create a BytesIO buffer to hold the audio in memory
            tts.save("output.mp3")


    def speak_text(self):
    
        # Define the file path
        audio_file = "output.mp3"
        
        # Play the audio file
        playsound.playsound(audio_file)
        
        # Optionally, remove the file after playing
        