from Targets.Rail_target import Rail_target
from Targets.Dynamic_target import Dynamic_target
from Targets.Moving_target import Moving_target
from Targets.Target import Target
import mutagen
import os
import Stage
import datetime

class Stage_Saver:
    def __init__(self, stage: Stage):
        self.stage = stage
        self.save_header()
        self.save_stage_header()
        self.save_music_header()
        self.save_targets()
        self.create_best_score()

    def save_header(self):
        os.makedirs("stages/" + self.stage.name)
        with open("stages/" + self.stage.name + "/" + self.stage.name + ".issou", "w") as file:
            file.write("ext=issou\n")
            file.write("type=stage\n")
            file.write("owner=player\n")
            date = datetime.datetime.now()
            file.write("crea_date=" + str(date.day) + '/' + str(date.month) + '/' + str(date.year) + '\n')
            file.write("$\n")
            file.close()

    def save_stage_header(self):
        with open("stages/" + self.stage.name + "/" + self.stage.name + ".issou", "a") as file:
            file.write("title=" + self.stage.name + '\n')
            file.write("difficulty=" + str(self.stage.difficulty) + '\n')
            file.write("$\n")
            file.close()

    def save_music_header(self):
        with open("stages/" + self.stage.name + "/" + self.stage.name + ".issou", "a") as file:
            #if os.path.isfile("stages/" + self.stage.name + "/" + self.stage.name + ".mp3"):
            if os.path.isfile("stages/" + "test_v2" + "/" + "test_v2" + ".mp3"):
                #audioReader = mutagen.File("stages/" + self.stage.name + "/" + self.stage.name + ".mp3")
                audioReader = mutagen.File("stages/" + "test_v2" + "/" + "test_v2" + ".mp3")
                file.write("title=" + str(audioReader["TIT2"]) + '\n')
                file.write("desc=§" + str(audioReader["COMM::fra"]) + "§\n")
                file.write("authors=§" + str(audioReader["TPE1"]).replace('/', '\n') + "§\n")
            else:
                file.write("title=" + self.stage.stage_music.name + '\n' )
                file.write("desc=" + "No description\n")
                file.write("authors=§" + "Unknown author" + "§\n")
            file.write("$\n")
            file.close()

    def save_targets(self):
        with open("stages/" + self.stage.name + "/" + self.stage.name + ".issou", "a") as file:
            for target in self.stage.targets:
                if isinstance(target, Rail_target):
                    file.write("type=4\n")
                elif isinstance(target, Dynamic_target):
                    file.write("type=3\n")
                elif isinstance(target, Moving_target):
                    file.write("type=2\n")
                else:
                    file.write("type=1\n")
                file.write("coo=" + str(target.coordinates.x) + '|' + str(target.coordinates.y) + '\n')
                file.write("dur=" + str(target.duration) + '\n')
                file.write("del=" + str(target.delay) + '\n')
                file.write("val=" + str(target.value) + '\n')

                #file.write("texture=" + target.image + '\n')
                file.write("texture=basic_blue\n")

                if isinstance(target, Rail_target):
                    string = "steps=§"
                    for coordinates in target.steps:
                        string += str(coordinates.x) + '|' + str(coordinates.y) + '§'
                    file.write(string + '\n')
                elif isinstance(target, Dynamic_target):
                    file.write("end_val=" + str(target.end_value) + '\n')
                elif isinstance(target, Moving_target):
                    file.write("end_coo=" + str(target.end_coordinates.x) + '|' + str(target.end_coordinates.y))
                    file.write('\n')

    def create_best_score(self):
        with open("stages/" + self.stage.name + "/" + self.stage.name + "_bs.issou", "w") as file:
            file.write("ext=issou\ntype=best_score\nowner=player\n$\nval=0")
            file.close()
