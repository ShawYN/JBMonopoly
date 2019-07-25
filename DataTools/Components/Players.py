class Player(object):
    def __init__(self, name, index, currentPosition, property, characterIndex):
        self.name = name
        self.index = index
        self.currentPosition = currentPosition
        self.property = property
        self.characterIndex = characterIndex

    def getName(self):
        return self.name

    def getcurrentPostion(self):
        return self.currentPosition

    def getProperty(self):
        return self.property
