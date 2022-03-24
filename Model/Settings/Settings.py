import pygame

class Settings:

    def __init__(self):
        self.load_change()

    def set_animation(self, anim):
        self.animation = anim

    """
    Change l'état de l'affichage des animations (activé ou désactivé) en inversant l'état actuel
    """
    def change_animation(self):
        if self.animation:
            self.animation = False
        else:
            self.animation = True


    def get_animation(self):
        return self.animation

    def set_volume(self, vol):
        self.volume = vol
        pygame.mixer.music.set_volume(self.volume * 0.1)

    def get_volume(self):
        return self.volume

    """
    Sauvegarde l'état acutel des paramètres dans le fichier
    """
    def save_change(self):
        file = open("Model/Settings/data.issou", "w")
        file.write("Data file ISSOU\n")
        file.write(str(self.volume) + "\n")
        file.write(str(self.animation) + "\n")
        file.close()

    """
    Charge les paramètres stockés dans le fichier
    """
    def load_change(self):
        with open("Model/Settings/data.issou", "r") as file:
            line = file.readline()
            if line == "Data file ISSOU\n":
                self.volume = int(file.readline())
                if file.readline() == "True\n":
                    self.animation = True
                else:
                    self.animation = False
            else:
                print("erreur chargement du fichier de settings")
                self.volume = 5
                self.animation = True
        pygame.mixer.music.set_volume(self.volume*0.1)
