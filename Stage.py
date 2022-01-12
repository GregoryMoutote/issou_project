from pygame import mixer
from abc import ABC, abstractmethod
from Music import Music
from Target import Target
from Date import Date
import time
#TODO Add the creation date
class Stage:
    def __init__(self, file_path):
        self.path = file_path
        self.targets = []
        self.difficulty = 0
        self.name = ""
        self.best_score = 0
        self.activeTargets = []
        self.stage_music = None
        self.date = None
        self.is_stage_usable = False
        self.pre_load_stage()
        self.load_targets()

    def pre_load_stage(self):
        if ".issou" not in self.path:
            return
        self.stage_music = Music(self.path[0:self.path.find(".issou") - 1] + ".wav")
        with open(self.path, 'r') as file:
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
            if "crea_date=" not in line:
                file.close()
                return
            else:
                first_delimiter = line.find('/')
                day = line[10:first_delimiter]
                second_delimiter = line.find('/', first_delimiter + 1)
                month = line[first_delimiter + 1: second_delimiter]
                year = line[second_delimiter + 1: -1]
                self.date = Date(day, month, year)
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
            self.load_best_score()

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

    def load_best_score(self, ):
        if ".issou" not in self.path:
            return
        best_score_path = self.path[0:self.path.find(".issou")] + "_bs.issou"
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

    def save_best_score(self):
        if ".issou" not in self.path:
            return
        best_score_path = self.path[0:self.path.find(".issou")] + "_bs.issou"
        with open(best_score_path, 'w') as file:
            file.write("ext=issou\ntype=best_score\nowner=player\n$\nval=" + str(self.best_score))
            file.close()

    def load_targets(self):
        if ".issou" not in self.path:
            return
        with open(self.path, 'r') as file:
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
            line = file.readline()
            if "difficulty=" not in line:
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
            line = file.readline()
            while line and '$' not in line:
                line = file.readline()
            if not line:
                file.close()
                return
            line = file.readline()
            while line:
                targetData = []
                if "type=" not in line or not line or '\n' not in line:
                    break
                targetData.append(int(line[5:-1]))
                line = file.readline()
                if "coo=" not in line or '|' not in line or not line or '\n' not in line:
                    break
                targetData.append(int(line[4:line.find('|')]))
                targetData.append(int(line[line.find('|') + 1:-1]))
                line = file.readline()
                if "dur=" not in line or not line or '\n' not in line:
                    break
                targetData.append(float(line[4:-1]))
                line = file.readline()
                if "del=" not in line or not line or '\n' not in line:
                    break
                targetData.append(float(line[4:-1]))
                line = file.readline()
                if "val=" not in line or not line or '\n' not in line:
                    break
                targetData.append(int(line[4:-1]))
                line = file.readline()
                if "col=" not in line or not line:
                    break
                firstSeparator = line.find('|')
                secondSeparator = line.find('|', firstSeparator + 1)
                targetData.append(int(line[4:firstSeparator]))
                targetData.append(int(line[firstSeparator + 1:secondSeparator]))
                targetData.append(int(line[secondSeparator + 1:len(line)]))
                line = file.readline()
                self.targets.append(Target(targetData))
                #TODO Adapt to the target the number of lines
            for target in self.targets:
                target.display()
            file.close()

    def display_test(self):
        print(self.name, self.difficulty, self.stage_music.name)
        print(self.best_score, self.date)
        print(self.stage_music.description, self.stage_music.authors)

    def __del__(self):
        if self.targets != None:
            self.targets.clear()
        self.stage_music = None