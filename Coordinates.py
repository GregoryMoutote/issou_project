

class Coordinates:
    def __init__(self, x, y):
        try:
            self.x = float(x)
            self.y = float(y)
        except:
            self.x = 0
            self.y = 0