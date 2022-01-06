from pygame import mixer

class Music:
    def __init__(self, music_path):
        self.music = None
        self.is_music_loaded = False
        self.duration = 0
        self.music_path = music_path
        self.name = ""
        self.description = ""
        self.illustration_path = ""
        self.authors = []

    def play(self):
        if self.is_music_loaded:
            self.music.play()

    def load(self):
        try:
            self.music = mixer.Sound(self.music_path)
            self.duration = self.music.get_length()
        except FileNotFoundError:
            pass
        if self.music:
            self.is_music_loaded = True

    def pause(self):
        if self.is_music_loaded:
            self.music.stop()