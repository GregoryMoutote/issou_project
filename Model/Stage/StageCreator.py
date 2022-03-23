from Model.Stage.StageSaver import StageSaver
from Model.Stage.Stage import Stage
from Model.Stage.Music import Music
from Targets.Target import Target
import os
import shutil
import re
from Model.Constants import Constants

class StageCreator:
    def __init__(self,screen, stage_name: str="",  illustration_path: str="", background_path: str="", music_path: str="",settings: str=""):
        self.is_usable = True
        if not re.search("\w+", stage_name):
            self.is_usable = False
            return
        os.makedirs("Stages/" + stage_name)
        stage_path = "Stages/" + stage_name.lower() + '/' + stage_name.lower() + ".issou"
        self.stage = Stage(stage_path, screen,True,settings)
        self.stage.is_stage_usable=True
        self.stage_name = stage_name
        self.background_path=background_path

        while self.background_path.find(".") != -1:
            self.background_path = self.background_path[self.background_path.find(".")+1:]

        if ".mp3" not in music_path:
            self.is_usable = False
            return
        if os.path.isfile(music_path):
            stage_music_path = stage_path[0:stage_path.find(".issou")] + ".mp3"
            shutil.copy2(music_path, stage_music_path)
            self.stage.stage_music = Music(music_path)
            self.stage.stage_music.load()
            self.stage.stage_music.pause()
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

        os.makedirs("Stages/" + self.stage_name + "/specialTargets")

        self.targets = []
        self.targets_index=-1
        self.active_target_index=-1
        self.moving_target_index=-1

        self.currently_modified_target_index = -1

    """
    Ajoute une cible au tableau des cibles non affichées et le tableau de toutes les cibles
    """
    def add_target(self, target: Target):
        if self.is_usable:
            self.targets_index=len(self.targets)
            self.targets.append(target)
            self.stage.targets.append(target)

    """
    Retire une cible du tableau
    """
    def remove_target(self):
        self.targets.pop(self.targets_index)
        self.stage.active_targets.pop(self.active_target_index)
        self.targets_index=-1
        self.active_target_index = -1
        self.moving_target_index=-1

    """
    Ajoute une texture de cible spéciale dans le niveau
    """
    def add_special_target(self,target):
        if ".png" not in target:
            self.is_usable = False
            return
        if os.path.isfile(target):
            name=target
            while name.find("\\") != -1:
                name = name[name.find("\\") + 1:]
            target_path = "Stages/" + self.stage_name.lower() + "/specialTargets/" +name

            shutil.copy2(target, target_path)

        else:
            self.is_usable = False
            return

    """
    Rembobine ou déroule un niveau en fonction d'un ratio entre 0 et 1
    """
    def rewind(self, ratio: float):
        self.stage.set_pose(ratio, self.targets)

    """
    Permet de sauvegarder un niveau en cours de création
    """
    def save(self):
        self.stage_saver = StageSaver(self.stage)

    """
    Permet de tester si un cible à été touché pour la selectionner
    """
    def set_target_to_modify(self, x, y):
        found_target = None
        self.active_target_index=0
        for target, delay in self.stage.active_targets:
            if int(target.coordinates.x - x) ** 2 + int(target.coordinates.y - y) ** 2 <= Constants.TARGET_RADIUS ** 2:
                print("Found a target")
                found_target = target
                break
            self.active_target_index+=1
        if found_target != None:
            self.targets_index = 0
            for target in self.targets:
                if found_target == target:
                    return
                self.targets_index += 1
        print("active target index",self.active_target_index,"               target index",self.targets_index)

    """
    Permet l'import des textures du niveau
    """
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

    """
    Retourne la cible actuellement selectionnée pour la modifier
    """
    def get_currently_modified_target(self):
        if 0 <= self.currently_modified_target_index < self.targets.len:
            return self.targets[self.currently_modified_target_index]