from agent.caivaAgent import Caiva
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from controllers.play_sound_controller import PlaySoundController

play_sound_router = APIRouter()

@play_sound_router.get('/play_sound')
def play_sound():
    speaker = PlaySoundController()
    speaker.speak_text()
    
    return JSONResponse(
        content="Done" 
    )

