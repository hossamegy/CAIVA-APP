import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to capture and recognize speech


class SpeechRecognitionController:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize_speech_from_mic(self):
        with sr.Microphone() as source:
            print("Adjusting for ambient noise, please wait...")
            
            # Adjust for ambient noise and set the dynamic energy threshold
            recognizer.adjust_for_ambient_noise(source, duration=2)  # Increased duration for noise calibration
            
            print("Ready to receive speech...")

            try:
                # Listen to the source for input (non-blocking and timeout to handle silence)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)

                # Recognize speech using Google Web API
                print("Recognizing speech...")
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for speech.")
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    # Additional function to improve recognition performance for low-volume audio and noisy environments
    def optimize_recognizer(self):
        # Fine-tune energy threshold to ignore noise, but capture quiet sounds
        self.recognizer.energy_threshold = 4000  # You can dynamically adjust this depending on noise level
        self.recognizer.dynamic_energy_threshold = True  # Enable dynamic adjustment of the threshold
        
        # Adjust pause threshold (for handling slow speakers)
        self.recognizer.pause_threshold = 0.8  # Increases time before considering input as finished
        self.recognizer.operation_timeout = None  # No timeout during speech recognition

