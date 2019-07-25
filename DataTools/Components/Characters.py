import pygame as pg



class Characters(pg.sprite.Sprite):
    def __init__(self, index, setPainting, backgroundStory, soundEffect):
        self.setPainting = setPainting
        self.backgroundStory = backgroundStory
        self.soundEffect = soundEffect
        self.index = index

    def getSetPainting(self):
        return self.setPainting

    def getBackgroundStory(self):
        return self.backgroundStory

    def playSouncEffect(self):
        return self.soundEffect