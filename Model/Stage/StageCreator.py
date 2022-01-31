from Model.Stage.StageSaver import StageSaver
from Model.Stage.Stage import Stage
from Model.Stage.Music import Music
import os
import shutil
import re

class StageCreator:
    def __init__(self, stage_name: str, screen, illustration_path: str, background_path: str, music_path: str):
        self.is_usable = True
        if re.search("\w+", stage_name):
            self.is_usable = False
            return
        os.makedirs("Stages/" + self.stage.name)
        stage_path = "Stages/" + stage_name.lower() + '/' + stage_name.lower() + ".issou"
        self.stage = Stage(stage_path, screen)
        self.stage.name = stage_name

        if ".mp3" not in music_path:
            self.is_usable = False
            return
        if os.path.isfile(music_path):
            stage_music_path = stage_path[0:stage_path.find(".issou")] + ".mp3"
            shutil.copy2(music_path, stage_music_path)
            self.stage.stage_music = Music(music_path)
        else:
            self.is_usable = False
            return

        if ".png" not in illustration_path or ".jpg" not in illustration_path or ".jpeg" not in illustration_path:
            self.is_usable = False
            return
        if os.path.isfile(illustration_path):
            stage_illustration_path = stage_path[0:stage_path.find(".issou")] + \
                               illustration_path[illustration_path.find('.',
                                                                len(illustration_path) - 6):len(illustration_path) - 1]
            shutil.copy2(illustration_path, stage_illustration_path)
        else:
            self.is_usable = False
            return

        if ".png" not in background_path or ".jpg" not in background_path or ".jpeg" not in background_path:
            self.is_usable = False
            return
        if os.path.isfile(background_path):
            stage_background_path = "Stages/" + stage_name.lower() + "/background" + \
                               background_path[background_path.find('.',
                                                                len(background_path) - 6):len(background_path) - 1]
            shutil.copy2(illustration_path, stage_illustration_path)
        else:
            self.is_usable = False
            return

        os.makedirs("Stages/" + self.stage.name + "/specialTargets")

        self.targets = []

    def add_target(self, target: Target):
        self.targets.append(target)

    def rewind(self, ratio: float):
        self.stage(ratio, self.targets)

    def save(self):
        self.stage_saver = StageSaver(self.stage)
        self.stage_saver = None
