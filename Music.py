from pygame import mixer

class Stage:
    def __init__(self, music_path, music_details_path):
        music = None
        is_music_loaded = False
        duration = 0
        try:
            music = mixer.Sound(music_path)
            duration = music.get_length()
        except FileNotFoundError:
            pass
        if music:
            is_music_loaded = True
        name = ""
        description = ""
        illustration_path = ""
        authors = [""]

    def load_details(self, music_details_path):
        pass