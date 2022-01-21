

class Date:
    def __init__(self, day, month, year):
        self.day = str(day)
        self.month = str(month)
        self.year = str(year)

    def __str__(self):
        return self.day + '/' + self.month + '/' + self.year