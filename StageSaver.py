from Stage import Stage
from Targets.Rail_target import Rail_target
from Targets.Dynamic_target import Dynamic_target
from Targets.Moving_target import Moving_target
from Targets.Target import Target


class Stage_Saver:
    def __init__(self, stage: Stage):
        self.stage = stage

    def save_header(self):
        with open("stages/" + self.stage.name + "/" + self.stage.name + ".issou", "w") as file:
            file.write("ext=issou")
            file.write("type=stage")
            file.write("owner=game")
            date = datetime.datetime.now()
            file.write("crea_date=" + date.day + '/' + date.month + '/' + date.year)
            file.write("$")
            file.close()

    def save_stage_header(self):
        with open("stages/" + self.stage.name + "/" + self.stage.name + ".issou", "a") as file:
            file.write("title=" + self.stage.name)
            file.write("difficulty" + self.difficulty)
            file.writer("$")
            file.close()

    def save_music_header(self):
        with open("stages/" + self.stage.name + "/" + self.stage.name + ".issou", "a") as file:
            #TODO Meta data
            file.write("title=" + self.stage.stage_music.title)
            file.write("desc=" + "Benjamin is not yours ;) !")
            file.write("authors=§" + "" + "§")
            file.writer("$")
            file.close()

    def save_targets(self):
        with open("stages/" + self.stage.name + "/" + self.stage.name + ".issou", "a") as file:
            for target in self.stage.targets:
                if isinstance(target, Rail_target):
                    file.write("type=4")
                elif isinstance(target, Dynamic_target):
                    file.write("type=3")
                elif isinstance(target, Moving_target):
                    file.write("type=2")
                else:
                    file.write("type=1")
                file.write("coo=" + target.coordinates.x + '|' + target.coordinates.y)
                file.write("dur=" + target.duration)
                file.write("del=" + target.delay)
                file.write("val=" + target.value)
                file.write("texture=" + target.image)
                if isinstance(target, Rail_target):
                    string = "steps=§"
                    for coordinates in target.steps:
                        string += coordinates.x + '|' + coordinates.y + '§'
                    file.write(string)
                elif isinstance(target, Dynamic_target):
                    file.write("end_val=" + target.end_value)
                elif isinstance(target, Moving_target):
                    file.write("end_coo=" + target.end_coordinates.x + '|' + target.end_coordinates.y)

