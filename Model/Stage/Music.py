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
        try:
            self.music = mixer.Sound(self.music_path)
            self.duration = self.music.get_length()
        except FileNotFoundError:
            pass
        if self.music:
            self.music = None

    """
    Met en route la musique s'il y en a une chargée
    """
    def play(self):
        if self.is_music_loaded:
            mixer.music.unpause()

    """
    Charge une musique
    """
    def load(self):
        try:
            self.music = mixer.Sound(self.music_path)
        except FileNotFoundError:
            pass
        if self.music:
            self.is_music_loaded = True
            self.music = None
            mixer.music.load(self.music_path)
            mixer.music.play(-1)
            mixer.music.pause()

    """
    Met en pause une musique s'il y en a une chargée
    """
    def pause(self):
        if self.is_music_loaded:
            mixer.music.pause()

    """
    Permet de changer l'instant de la musique joué en fonction d'un ration entre 0 et 1
    """
    def set_pose(self, ratio: float):
        if self.is_music_loaded and 0 >= ratio >= 1:
            mixer.music.set_pose(ratio * self.duration)