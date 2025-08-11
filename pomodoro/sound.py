import os
from nava import play

class Sound:
    def __init__(self):
        self.sounds_dir = os.path.join(os.path.dirname(__file__), "..", "sounds")

    
    def play_start(self):
        sound_path = os.path.join(self.sounds_dir, "start.wav")
        play(sound_path, async_mode=True)
        
    def play_end(self):
        sound_path = os.path.join(self.sounds_dir, "end.wav")
        play(sound_path, async_mode=True)
    
    def play_finish(self):
        sound_path = os.path.join(self.sounds_dir, "finish.wav")
        play(sound_path, async_mode=True)