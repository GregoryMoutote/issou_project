from Buttons.CheckButton import *
from Buttons.Button import *

class MultipleButton(Button):

    def __init__(self, x, y, width, height, screen, true_color, false_color, nb_button, nb_active):
        super().__init__(x,y,width,height,screen)
        self.nb_button = nb_button
        self.nb_active = nb_active
        self.true_color = true_color
        self.false_color = false_color
        self.check = []

        for i in range(0, self.nb_button):
            if i < self.nb_active:
                self.check.append(CheckButton(self.x + i * self.width / (self.nb_button + 1), self.y, self.height, self.height, self.screen, self.true_color, self.false_color, True))
            else:
                self.check.append(CheckButton(self.x + i * self.width / (self.nb_button + 1), self.y, self.height, self.height, self.screen, self.true_color, self.false_color, False))
        self.show_button()

    """
    affiche le bouton
    """
    def show_button(self):
        for i in range(0, self.nb_button):
             self.check[i].show_button()

    """
    change le nombre de bouton activé et désactivé
    """
    def change_stat(self, nb_active):
        self.nb_active = nb_active

        for i in range(0, self.nb_button):
            if i < self.nb_active:
                self.check[i].active = True
            else:
                self.check[i].active = False
        self.show_button()

    def __del__(self):
        self.check.clear()