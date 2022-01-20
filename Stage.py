import pygame.display

from Music import Music
from Targets.Target import Target
from Targets.Dynamic_target import Dynamic_target
from Targets.Moving_target import Moving_target
from Targets.Rail_target import Rail_target
from Date import Date
from pygame import mixer
from StageSaver import Stage_Saver
import time
import os

from Constants import Constants

#TODO Add the creation date
class Stage:
    def __init__(self, file_path,screen):
        self.screen=screen
        self.path = file_path
        self.score = 0
        self.targets = []
        self.difficulty = 0
        self.name = ""
        self.best_score = 0
        self.activeTargets = []
        self.stage_music = None
        self.date = None
        self.is_stage_usable = False
        self.pre_load_stage()
        self.spend = -1
        self.start = -1
        self.next_action = -1

    def load(self):
        self.score = 0
        self.targets.clear()
        self.activeTargets.clear()
        self.is_stage_usable = False
        self.spend = -1
        self.start = -1
        self.next_action = -1
        self.load_targets()
        self.stage_music.load()
        self.load_stage()
        """ Stage saver test
        self.name = "test"
        Stage_Saver(self)
        self.name = "test_v2"
        """

    def pre_load_stage(self):
        if ".issou" not in self.path:
            return
        if os.path.isfile(self.path[0:self.path.find(".issou")] + ".mp3"):
            self.stage_music = Music(self.path[0:self.path.find(".issou")] + ".mp3")
        else:
            self.stage_music = Music(self.path[0:self.path.find(".issou")] + ".wav")
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
                self.name = line[6:-1].lower()
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
        if self.is_stage_usable:
            if self.spend > 0:
                print("Delay application")
                for iterator in range (0, len(self.activeTargets)):
                    print(self.activeTargets[iterator][1])
                    self.activeTargets[iterator][1] += self.spend
                    print(self.activeTargets[iterator][1])
                if self.start <= 0:
                    self.stage_music.play()
                print()
                print(self.start)
                self.start += self.spend
                print(self.start)
                self.spend = -1
            elif not mixer.music.get_busy():
                self.start = time.time()
                self.stage_music.play()
            if self.is_stage_usable:
                if len(self.targets) > 0:
                    self.next_action = self.start + self.targets[0].delay
                    if self.next_action <= time.time():
                        self.activeTargets.append([self.targets[0], time.time() + self.targets[0].duration])
                        self.targets.pop(0)
                if len(self.activeTargets) > 0:
                    for iterator in range(len(self.activeTargets) - 1, -1, -1):
                        if self.activeTargets[iterator][1] <= time.time():
                            print(self.activeTargets[iterator], time.time())
                            self.activeTargets.pop(iterator)

    def show_targets(self):
        for target,delay in self.activeTargets:
            target.showTarget()
 
    def pause(self):
        print(time.time(), self.next_action)
        self.spend = time.time()
        self.is_stage_usable = False
        self.stage_music.pause()

    def resume(self):
        self.load_stage()
        self.spend = time.time() - self.spend
        print(time.time(), self.next_action)

    def load_stage(self):
        if self.stage_music and self.targets:
            self.is_stage_usable = self.stage_music.is_music_loaded

    def load_best_score(self):
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
        if self.best_score < self.score:
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
            if "crea_date=" not in line:
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
                targetData.append(float(line[4:line.find('|')]))
                targetData.append(float(line[line.find('|') + 1:-1]))
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
                if "texture=" not in line or not line:
                    break
                if '\n' in line:
                    targetData.append(line[8:-1])
                else:
                    targetData.append(line[8:len(line)])
                line = file.readline()
                if targetData[0] == 2:
                    if "end_coo=" not in line or not line:
                        break
                    if "coo=" not in line or '|' not in line or not line:
                        break
                    targetData.append(float(line[8:line.find('|')]))
                    targetData.append(float(line[line.find('|') + 1:-1]))
                    line = file.readline()
                elif targetData[0] == 3:
                    if "end_val=" not in line or not line:
                        break
                    targetData.append(int(line[8:-1]))
                    line = file.readline()
                elif targetData[0] == 4:
                    if "step=" not in line or not line:
                        break
                    delimiter = line.find('§')
                    while '§' in line[delimiter + 1: len(line)]:
                        next_delimiter = line.find('§', delimiter + 1)
                        toProcess = line[delimiter + 1: next_delimiter - 1]
                        targetData.append(float(toProcess[0:toProcess.find('|')]))
                        targetData.append(float(toProcess[toProcess.find('|') + 1:len(toProcess)]))
                        delimiter = next_delimiter
                    line = file.readline()
                if targetData[0] == 2:
                    self.targets.append(Moving_target(targetData,self.screen))
                elif targetData[0] == 3:
                    self.targets.append(Dynamic_target(targetData,self.screen))
                elif targetData[0] == 4:
                    self.targets.append(Rail_target(targetData,self.screen))
                else:
                    self.targets.append(Target(targetData,self.screen))
            file.close()

    def display_test(self):
        print(self.name, self.difficulty, self.stage_music.name)
        print(self.best_score, self.date)
        print(self.stage_music.description, self.stage_music.authors)

    def __del__(self):
        if self.targets != None:
            self.targets.clear()
        self.stage_music = None

    def test_collision(self, x, y):
        iterator = 0
        for target, delay in self.activeTargets:
            if isinstance(target, Rail_target):
                target.actualise(Coordinates(x, y))
                if target.is_achieved:
                    self.score += self.activeTargets[iterator][0].value
                    del self.activeTargets[iterator]
            if int(target.coordinates.x - x) ** 2 + int(target.coordinates.y - y) ** 2 <= Constants.TARGET_RADIUS**2:
                self.score += self.activeTargets[iterator][0].value
                del self.activeTargets[iterator]
            iterator += 1