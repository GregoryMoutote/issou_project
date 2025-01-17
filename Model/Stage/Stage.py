from Animation import *
from Model.Stage.Music import Music
from Targets.Target import Target
from Targets.DynamicTarget import DynamicTarget
from Targets.MovingTarget import MovingTarget
from Targets.RailTarget import RailTarget
from Model.Stage.Date import Date
from pygame import mixer
from Model.Stage.Coordinates import Coordinates
import time
import os

from Model.Constants import Constants

class Stage:
    def __init__(self, file_path, screen, is_creation,settings):
        self.screen = screen
        self.settings=settings
        self.path = file_path
        self.score = 0
        self.targets = []
        self.difficulty = 0
        self.name = ""
        self.best_score = 0
        self.active_targets = []
        self.stage_music = None
        self.date = None
        self.is_stage_usable = False
        if not is_creation:
            self.pre_load_stage()
        self.spent = -1
        self.start = -1
        self.next_action = -1
        self.animationList=[]
        self.sprites=[]
        for path in os.listdir("Pictures/Animations/explosion_v2"):
            self.sprites.append(pygame.transform.scale(pygame.image.load("Pictures/Animations/explosion_v2/" + path), (200, 200)))

    """
    Charge un niveau complètement pour le rendre utilisable
    Chargement des cibles et de la musique ainsi qu'initialisation des variables utiles
    """
    def load(self):
        self.score = 0
        self.targets.clear()
        self.active_targets.clear()
        self.is_stage_usable = False
        self.spent = -1
        self.start = -1
        self.next_action = -1
        self.load_targets()
        self.stage_music.load()
        self.load_stage()

    """
    Charge l'en tête d'un fichier pour le rendre affichable dans la liste des niveaux jouables
    Chargement de l'en tête de la musique comprise
    """
    def pre_load_stage(self):
        if ".issou" not in self.path:
            return
        if os.path.isfile(self.path[0:self.path.find(".issou")] + ".mp3"):
            self.stage_music = Music(self.path[0:self.path.find(".issou")] + ".mp3")
        else:
            self.stage_music = Music(self.path[0:self.path.find(".issou")] + ".wav")
        with open(self.path, 'r', encoding="ISO-8859-1") as file:
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
                day = line[10: first_delimiter]
                second_delimiter = line.find('/', first_delimiter + 1)
                month = line[first_delimiter + 1:second_delimiter]
                year = line[second_delimiter + 1:-1]
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
                self.name = line[6: -1].lower()
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
                        if 'Â' in line:  # line.find('Â') - 1
                            self.stage_music.description += line[:delimiter - 1]
                        else:
                            self.stage_music.description += line[:delimiter]
                    else:
                        self.stage_music.description += line[delimiter + 1:len(line)]
                else:
                    self.stage_music.description += line[:len(line)]
            while '\n' in self.stage_music.description:
                self.stage_music.description = self.stage_music.description.replace('\n', ' ')
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

    """
    Execute un cycle en jeu en gérant la pause et les cibles à afficher et faire disparaître
    """
    def play(self):
        if self.is_stage_usable:
            if self.spent > 0:
                for iterator in range (0, len(self.active_targets)):
                    self.active_targets[iterator][1] += self.spent
                    if isinstance(self.active_targets[iterator][0], MovingTarget) or \
                            isinstance(self.active_targets[iterator][0], DynamicTarget):
                        self.active_targets[iterator][0].begin_time += self.spent
                if self.start > 0:
                    self.stage_music.play()
                self.start += self.spent
                self.spent = -1
            elif not mixer.music.get_busy():
                self.start = time.time()
                self.stage_music.play()
            if self.is_stage_usable:
                self.actualise_active_targets()
                if len(self.active_targets) > 0:
                    for iterator in range(len(self.active_targets) - 1, -1, -1):
                        if self.active_targets[iterator][1] <= time.time():
                            self.active_targets.pop(iterator)

    """
    Ajoute les cibles à afficher à l'écran et les retires des cibles qui n'ont pas été affichées
    """
    def actualise_active_targets(self):
        if len(self.targets) > 0:
            self.next_action = self.start + self.targets[0].delay
            if self.next_action <= time.time():
                self.active_targets.append([self.targets[0], time.time() + self.targets[0].duration])
                self.targets.pop(0)

    """
    Fait s'actualiser les cibles actuellement affichées
    Destiné aux cibles avec des changements dans le temps
    """
    def update_targets(self):
        for target, delay in self.active_targets:
            target.update()

    """
    S'occupe d'afficher les cibles qui sont dans le tableaux des cibles actives en gérant les animations
    """
    def show_targets(self):
        for target, delay in self.active_targets:
            target.show_target()
        if self.settings.animation:
            for animation in self.animationList:
                if animation.show():
                    self.animationList.remove(animation)

    """
    Met en pause le niveau ainsi que la musique
    """
    def pause(self):
        self.spent = time.time()
        self.is_stage_usable = False
        self.stage_music.pause()

    """
    Permet de savoir si un niveau est terminé
    """
    def is_ended(self):
        return self.start + self.stage_music.duration < time.time()

    """
    Permet de reprendre un niveau au moment où la pause a été activée
    """
    def resume(self):
        self.load_stage()
        self.spent = time.time() - self.spent

    """
    Permet de valider le chargement d'un niveau
    """
    def load_stage(self):
        if self.stage_music and self.targets:
            self.is_stage_usable = self.stage_music.is_music_loaded

    """
    Charge le niveau de meilleur score pour en récuperer le score contenu
    """
    def load_best_score(self):
        if ".issou" not in self.path:
            return
        best_score_path = self.path[0:self.path.find(".issou")] + "_bs.issou"
        with open(best_score_path, 'r', encoding="ISO-8859-1") as file:
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

    """
    Permet de sauvegarder le score obtenu s'il est meilleur que le celui actuellement stocké
    """
    def save_best_score(self):
        if ".issou" not in self.path:
            return
        if self.best_score < self.score:
            best_score_path = self.path[0:self.path.find(".issou")] + "_bs.issou"
            with open(best_score_path, 'w', encoding="ISO-8859-1") as file:
                file.write("ext=issou\ntype=best_score\nowner=player\n$\nval=" + str(self.score))
                file.close()
                self.best_score = self.score

    """
    Charge les cibles d'un niveau depuis le fichier les contenant et les ajoute aux tableaux du niveau
    """
    def load_targets(self):
        if ".issou" not in self.path:
            return
        with open(self.path, 'r', encoding="ISO-8859-1") as file:
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
                target_data = []
                if "type=" not in line or not line or '\n' not in line:
                    break
                target_data.append(int(line[5:-1]))
                line = file.readline()
                if "coo=" not in line or '|' not in line or not line or '\n' not in line:
                    break
                target_data.append(float(line[4:line.find('|')]))
                target_data.append(float(line[line.find('|') + 1:-1]))
                line = file.readline()
                if "dur=" not in line or not line or '\n' not in line:
                    break
                target_data.append(float(line[4:-1]))
                line = file.readline()
                if "del=" not in line or not line or '\n' not in line:
                    break
                target_data.append(float(line[4:-1]))
                line = file.readline()
                if "val=" not in line or not line or '\n' not in line:
                    break
                target_data.append(int(line[4:-1]))
                line = file.readline()
                if "texture=" not in line or not line:
                    break
                if '\n' in line:
                    target_data.append(line[8:-1])
                else:
                    target_data.append(line[8:len(line)])
                line = file.readline()
                if target_data[0] == 2:
                    if "end_coo=" not in line or not line:
                        break
                    if "coo=" not in line or '|' not in line or not line:
                        break
                    target_data.append(float(line[8:line.find('|')]))
                    target_data.append(float(line[line.find('|') + 1:-1]))
                    line = file.readline()
                elif target_data[0] == 3:
                    if "end_val=" not in line or not line:
                        break
                    target_data.append(int(line[8:-1]))
                    line = file.readline()
                elif target_data[0] == 4:
                    if "steps=" not in line or not line:
                        break
                    delimiter = line.find('§')
                    while '§' in line[delimiter + 1: len(line)]:
                        next_delimiter = line.find('§', delimiter + 1)
                        to_process = line[delimiter + 1: next_delimiter]
                        target_data.append(float(to_process[0:to_process.find('|')]))
                        target_data.append(float(to_process[to_process.find('|') + 1:len(to_process)]))
                        delimiter = next_delimiter
                    line = file.readline()
                if target_data[0] == 2:
                    self.targets.append(MovingTarget(target_data, self.screen, self.name))
                elif target_data[0] == 3:
                    self.targets.append(DynamicTarget(target_data, self.screen, self.name))
                elif target_data[0] == 4:
                    self.targets.append(RailTarget(target_data, self.screen, self.name))
                else:
                    self.targets.append(Target(target_data,self.screen,self.name))
            file.close()

    def __del__(self):
        if self.targets != None:
            self.targets.clear()
        self.stage_music = None

    """
    Teste si des cibles sont touchées par le joueur et les retire du tableau si besoin
    """
    def test_collision(self, x, y):
        iterator = 0
        for target, delay in self.active_targets:
            if isinstance(target, RailTarget):
                target.actualise(Coordinates(x, y))
                if target.is_achieved:
                    self.score += self.active_targets[iterator][0].value
                    if self.settings.animation:
                        self.animationList.append(
                            Animation(self.screen, Coordinates(self.active_targets[iterator][0].steps[len(
                                self.active_targets[iterator][0].steps) - 1].x + Constants.TARGET_RADIUS - 100,
                                                               self.active_targets[iterator][0].steps[len(
                                                                   self.active_targets[iterator][
                                                                       0].steps) - 1].y + Constants.TARGET_RADIUS - 100),
                                      self.sprites))
                    del self.active_targets[iterator]
            elif int(target.coordinates.x - x) ** 2 + int(target.coordinates.y - y) ** 2 <= Constants.TARGET_RADIUS**2:
                self.score += self.active_targets[iterator][0].value
                if self.settings.animation:
                    self.animationList.append(Animation(self.screen, Coordinates(self.active_targets[iterator][0].coordinates.x - 100,
                                           self.active_targets[iterator][0].coordinates.y - 100),self.sprites))
                del self.active_targets[iterator]
            iterator += 1

    """
    Permet de rembobiner ou de débobiner un niveau en actualisant les cibles et la musique
    """
    def set_pos(self, ratio: float, targets: list):
        self.spent = -1
        self.start = time.time() - (float(self.stage_music.duration) * ratio) / 1000

        if ratio < 0 or ratio > 1:
            print("return ratio")
            return
        new_pos = self.stage_music.duration * ratio
        before = False
        if mixer.music.get_pos() > new_pos:
            before = True
        self.targets = targets
        if before:
            self.active_targets.clear()

            self.next_action = -1
            if len(self.targets)>0:
                self.next_action=self.start + self.targets[0].delay
        print("target len:"+str(len(self.targets))+"before:"+str(before))
        for target in self.targets:
            print("delay: "+str(target.delay))
            if target.delay < new_pos:
                if target.delay + target.duration > new_pos:
                    self.active_targets.append((target,
                                               time.time() + target.delay + target.duration - new_pos))
                self.targets.pop(0)
            else:
                break
        mixer.music.play()
        mixer.music.rewind()
        mixer.music.set_pos(float(ratio * float(self.stage_music.duration)))
        mixer.music.pause()