from pygame import mixer
from abc import ABC, abstractmethod
from Music import Music
import time

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

    def play(self):
        if is_stage_usable:
            stage_music.play()
            while len(targets) > 0 and len(activeTargets) > 0 and is_stage_usable:
                time.sleep(0.1)
                targets[0][1] -= 0.1
                while targets[0][1] <= 0:
                    activeTargets.append(targets.pop(0))
                    #TODO Display the target
                for iterator in range(len(activeTargets) -1, 0, -1):
                    activeTargets[iterator][1] -= 0.1
                    if activeTargets[iterator][1] == 0:
                        activeTargets.pop(iterator)
                        #TODO Undisplay the target

    def pause(self):
        is_stage_usable = False
        stage_music.pause()