import os
from dotenv import load_dotenv
from elevenlabs import ElevenLabs
from elevenlabs import play

class Speaker:
    def __init__(self, text: str, voice_id: str = "TumdjBNWanlT3ysvclWh"):
        self.text = text
        self.voice_id = voice_id

    def text_to_speech(self):
        load_dotenv()
        
        api_key = os.getenv("ELEVENLABS_API_KEY")
        
        elevenlabs = ElevenLabs(
            api_key=api_key,
        )

        audio = elevenlabs.text_to_speech.convert(
            text=self.text,
            voice_id=self.voice_id,
            model_id="eleven_flash_v2_5",
            output_format="mp3_44100_128",
        )

        play(audio)