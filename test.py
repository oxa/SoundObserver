from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file("./sounds/AirHorn.mp3", format="mp3")

adjusted_sound = sound - 10  # Decreases volume by 10 dB

# Play the adjusted sound
play(adjusted_sound)
play(sound )