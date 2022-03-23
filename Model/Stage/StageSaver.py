from Targets.RailTarget import RailTarget
from Targets.DynamicTarget import DynamicTarget
from Targets.MovingTarget import MovingTarget
from Model.Stage import Stage
import mutagen
import os
import datetime
import ctypes

class StageSaver:
    def __init__(self, stage: Stage):
        self.stage = stage
        self.save_header()
        self.save_stage_header()
        self.save_music_header()
        self.save_targets()
        self.create_best_score()

    def save_header(self):
        with open("Stages/" + self.stage.name + "/" + self.stage.name + ".issou", "w",encoding="ISO-8859-1") as file:
            file.write("ext=issou\n")
            file.write("type=stage\n")
            file.write("owner=player\n")
            date = datetime.datetime.now()
            file.write("crea_date=" + str(date.day) + '/' + str(date.month) + '/' + str(date.year) + '\n')
            file.write("$\n")
            file.close()

    def save_stage_header(self):
        with open("Stages/" + self.stage.name + "/" + self.stage.name + ".issou", "a",encoding="ISO-8859-1") as file:
            file.write("title=" + self.stage.name + '\n')
            file.write("difficulty=" + str(self.stage.difficulty) + '\n')
            file.write("$\n")
            file.close()

    def save_music_header(self):
        with open("Stages/" + self.stage.name + "/" + self.stage.name + ".issou", "a",encoding="ISO-8859-1") as file:
            #if os.path.isfile("Stages/" + self.stage.name + "/" + self.stage.name + ".mp3"):
            if os.path.isfile("Stages/" + "test_v2" + "/" + "test_v2" + ".mp3"):
                #audio_reader = mutagen.File("Stages/" + self.stage.name + "/" + self.stage.name + ".mp3")
                audio_reader = mutagen.File("Stages/" + "test_v2" + "/" + "test_v2" + ".mp3")
                file.write("title=" + str(audio_reader["TIT2"]) + '\n')
                file.write("desc=§" + str(audio_reader["COMM::fra"]) + "\n§\n")
                file.write("authors=§" + str(audio_reader["TPE1"]).replace('/', '\n') + "§\n")
            else:
                file.write("title=" + self.stage.stage_music.name + '\n' )
                file.write("desc=" + "No description\n")
                file.write("authors=§" + "Unknown author" + "§\n")
            file.write("$\n")
            file.close()

    def save_targets(self):
        with open("Stages/" + self.stage.name + "/" + self.stage.name + ".issou", "a",encoding="ISO-8859-1") as file:
            screen = ctypes.windll.user32
            width = screen.GetSystemMetrics(0)
            for target in self.stage.targets:
                if isinstance(target, RailTarget):
                    file.write("type=4\n")
                elif isinstance(target, DynamicTarget):
                    file.write("type=3\n")
                elif isinstance(target, MovingTarget):
                    file.write("type=2\n")
                else:
                    file.write("type=1\n")
                file.write("coo=" + str(float(width) / float(target.coordinates.x)) +
                           '|' + str(float(width) - float(target.coordinates.y)) + '\n')
                file.write("dur=" + str(target.duration) + '\n')
                file.write("del=" + str(target.delay) + '\n')
                file.write("val=" + str(target.value) + '\n')

                file.write("texture=" + target.image + '\n')

                if isinstance(target, RailTarget):
                    string = "steps=§"
                    for coordinates in target.steps:
                        string += str(float(width) - float(coordinates.x)) + '|' +\
                                  str(float(width) - float(coordinates.y)) + '§'
                    file.write(string + '\n')
                elif isinstance(target, DynamicTarget):
                    file.write("end_val=" + str(target.end_value) + '\n')
                elif isinstance(target, MovingTarget):
                    file.write("end_coo=" + str(float(width) - float(target.end_coordinates.x)) + '|' +
                               str(float(width) - float(target.end_coordinates.y)))
                    file.write('\n')

    def create_best_score(self):
        with open("Stages/" + self.stage.name + "/" + self.stage.name + "_bs.issou", "w",encoding="ISO-8859-1") as file:
            file.write("ext=issou\ntype=best_score\nowner=player\n$\nval=0")
            file.close()
