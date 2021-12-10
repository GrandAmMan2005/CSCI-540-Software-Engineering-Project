

class Position:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def setNumber(self, number):
        self.number = number

    def setColor(self, color):
        self.color = color

    def getNumber(self):
        return self.number

    def getColor(self):
        return self.color

    def positionStr(self):
        return self.color + " " + str(self.number)

