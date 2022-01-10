from pygame import mixer
from abc import ABC, abstractmethod
from Music import Music
import time

class Stage:
    def __init__(self, file_path):
        self.targets = []
        self.difficulty = 0
        self.name = ""
        self.best_score = 0
        self.activeTargets = []
        self.stage_music = None
        self.is_stage_usable = False
        self.pre_load_stage(file_path)
        #TODO get the best score from the file on the preloading

    def pre_load_stage(self, file_path):
        if ".issou" not in file_path:
            return
        self.stage_music = Music(file_path[0:file_path.find(".issou") - 1] + ".wav")
        with open(file_path, 'r') as file:
            line = file.readline()
            if "ext=issou" not in line:
                file.close()
                return
            line = file.readline()
            if "type=stage" not in line:
                file.close()
                return
            line = file.readline()
            if "owner=" not in line:
                file.close()
                return
            line = file.readline()
            if "$" not in line:
                file.close()
                return
            line = file.readline()
            if "title=" not in line:
                file.close()
                return
            else:
                self.name = line[6:-1]
            line = file.readline()
            if "difficulty=" not in line:
                file.close()
                return
            else:
                self.difficulty = int(line[11])
                if self.difficulty < 0 or self.difficulty > 5:
                    self.difficulty = 0
            line = file.readline()
            if "$" not in line:
                file.close()
                return
            line = file.readline()
            if "title=" not in line:
                file.close()
                return
            else:
                self.stage_music.name = line[6:-1]
            while line and line.find('§') != len(line) - 2:
                line = file.readline()
                delimiter = line.find('§')
                if delimiter != -1:
                    if delimiter == len(line) - 2:
                        self.stage_music.description += line[:delimiter - 1]
                    else:
                        self.stage_music.description += line[delimiter + 1:-1]
                else:
                    self.stage_music.description += line[:]
                self.stage_music.description += '\n'
            line = "pass"
            while line and line.find('§') != len(line) - 2:
                line = file.readline()
                delimiter = line.find('§')
                if delimiter != -1:
                    if delimiter == len(line) - 2:
                        self.stage_music.authors.append(line[:delimiter - 1])
                    else:
                        self.stage_music.authors.append(line[delimiter + 1:-1])
                else:
                    self.stage_music.authors.append(line[0:-1])
            file.close()
            self.load_best_score(file_path)

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

    def load_stage(self, file_path):
        if self.stage_music and self.targets:
            self.is_stage_usable = self.stage_music.is_music_loaded

    def display_test(self):
        print(self.name, self.difficulty, self.stage_music.name)
        print(self.best_score)
        print(self.stage_music.description, self.stage_music.authors)

    def load_best_score(self, file_path):
        if ".issou" not in file_path:
            return
        best_score_path = file_path[0:file_path.find(".issou")] + "_bs.issou"
        with open(best_score_path, 'r') as file:
            line = file.readline()
            if "ext=issou" not in line:
                file.close()
                return
            line = file.readline()
            if "type=best_score" not in line:
                file.close()
                return
            line = file.readline()
            if "owner=" not in line:
                file.close()
                return
            line = file.readline()
            if "$" not in line:
                file.close()
                return
            line = file.readline()
            if "val=" not in line:
                file.close()
                return
            self.best_score = int(line[line.find('=') + 1:len(line)])