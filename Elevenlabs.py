from elevenlabs import set_api_key
from elevenlabs import generate, play

set_api_key('')

def Speak(Text):
    Text = str(Text)
    audio = generate(
    text=Text,
    voice="Matilda",
    model="eleven_monolingual_v1"
    )
    print(f"Jarvis : {Text}")
    play(audio)

Speak("Hello")