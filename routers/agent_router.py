from agent.caivaAgent import Caiva
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from controllers.agent_controller import return_agent_response
from controllers.speech_recognition_controller import SpeechRecognitionController
from controllers.play_sound_controller import PlaySoundController
import random

agent_router = APIRouter()

abot = Caiva()


agent_router = APIRouter()


@agent_router.get('/agent_response')
def get_agent_response():
    speaker = PlaySoundController()
    speech_recoginizer = SpeechRecognitionController()
    speech_recoginizer.optimize_recognizer()

    try:
        text = speech_recoginizer.recognize_speech_from_mic()
        print(text)
        agent_response = return_agent_response(input=text, agent=abot)
        print(agent_response)
        speaker.conver(agent_response)

    except Exception as e:
        print("Noise in input voice")
        agent_response = get_random_noise_phrase()
        print(agent_response)
        speaker.conver(agent_response)
    
    
    return JSONResponse(
        content=agent_response
    )

# Define a function to select a random phrase
def get_random_noise_phrase():
    noise_phrases = [
        "I'm having trouble hearing you; there's a lot of background noise.",
        "It sounds like there's noise around you, and I can't hear you clearly.",
        "Your voice is hard to hear because of some surrounding noise.",
        "There's too much noise around you; I can't hear you properly.",
        "I can't hear you well with all the noise in the background.",
        "There's background noise that's making it difficult to hear you.",
        "It's tough to hear you due to the noise around you.",
        "The noise around you is making it hard to understand you.",
        "I can barely hear you over the noise in the background.",
        "There’s too much noise; I’m struggling to hear you.",
        "It’s noisy around you, and I can’t hear what you’re saying.",
        "I can’t hear you clearly because of the background noise.",
        "All the noise is making it difficult to hear your voice.",
        "Your voice is being drowned out by noise around you.",
        "With all that noise, I can't hear you very well.",
        "The noise near you is making it hard for me to hear.",
        "It sounds noisy around you, and I’m having trouble hearing you.",
        "There’s too much background noise; I can’t hear you properly.",
        "I'm finding it hard to hear you over the noise around you.",
        "It’s difficult to understand you because of the noise."
    ]
    return random.choice(noise_phrases)

# Call the function and print the result
print()
