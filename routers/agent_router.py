from fastapi import APIRouter
from fastapi.responses import JSONResponse
from agent.caivaAgent import Caiva
from controllers.agent_controller import return_agent_response
from controllers.speech_recognition_controller import SpeechRecognitionController
from controllers.play_sound_controller import PlaySoundController
from controllers.helper_controller import get_random_noise_phrase


agent_router = APIRouter()

abot = Caiva()


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
