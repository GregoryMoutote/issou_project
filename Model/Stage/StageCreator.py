from Model.Stage.StageSaver import StageSaver
from Model.Stage.Stage import Stage
from Model.Stage.Music import Music
from Targets.Target import Target
import os
import shutil
import re
from Targets import *
from Model.Constants import Constants

class StageCreator:
    def __init__(self,screen, stage_name: str="",  illustration_path: str="", background_path: str="", music_path: str=""):
        self.is_usable = True
        if not re.search("\w+", stage_name):
            self.is_usable = False
            return
        os.makedirs("Stages/" + stage_name)
        stage_path = "Stages/" + stage_name.lower() + '/' + stage_name.lower() + ".issou"
        self.stage = Stage(stage_path, screen,True)
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

        if ".png" not in illustration_path and ".jpg" not in illustration_path and ".jpeg" not in illustration_path:
            self.is_usable = False
            return
        if os.path.isfile(illustration_path):
            stage_illustration_path = stage_path[0:stage_path.find(".issou")] + \
                               illustration_path[illustration_path.find('.',
                                                                len(illustration_path) - 6):len(illustration_path)]
            shutil.copy2(illustration_path, stage_illustration_path)
        else:
            self.is_usable = False
            return

        if ".png" not in background_path and ".jpg" not in background_path and ".jpeg" not in background_path:
            self.is_usable = False
            return
        if os.path.isfile(background_path):
            stage_background_path = "Stages/" + stage_name.lower() + "/background" + \
                               background_path[background_path.find('.',
                                                                len(background_path) - 6):len(background_path)]
            shutil.copy2(background_path, stage_background_path)
        else:
            self.is_usable = False
            return

        os.makedirs("Stages/" + self.stage.name + "/specialTargets")

        self.targets = []

    def add_target(self, target: Target):
        if self.is_usable:
            self.targets.append(target)

    def rewind(self, ratio: float):
        self.stage.set_pose(ratio, self.targets)

    def save(self):
        self.stage_saver = None
        self.stage_saver = StageSaver(self.stage)

    def get_target_to_modify(self, x, y):
        for target, delay in self.stage.active_targets:
            if int(target.coordinates.x - x) ** 2 + int(target.coordinates.y - y) ** 2 <= Constants.TARGET_RADIUS ** 2:
                return target
        return target

    def target_texture_import(self, texture_path: str):
        if not self.is_usable:
            return
        if ".png" not in background_path and ".jpg" not in background_path and ".jpeg" not in background_path:
            self.is_usable = False
            return
        if os.path.isfile(texture_path):
            delimiter = texture_path.find("\\")
            while "\\" in texture_path[texture_path.find("\\", delimiter + 1):]:
                delimiter = texture_path.find("\\", delimiter + 1)

            target_texture_path = "Stages/" + self.stage.name + "/" + texture_path[delimiter:]
            shutil.copy2(texture_path, target_texture_path)

