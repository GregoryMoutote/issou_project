from pygame import mixer
from abc import ABC, abstractmethod
from Music import Music

class Stage(ABC):
    def __init__(self, music, file_path):
        targets = []
        difficulty = 0
        name = ""
        best_score = 0
        load_stage(file_path)
        activeTargets = []
        stage_music = None
        if isinstance(music, Music):
            stage_music = music
        is_stage_usable = False
        if stage_music and targets:
            is_stage_usable = stage_music.is_music_loaded

    def load_stage(self, file_path):
        pass