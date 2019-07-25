import pygame
from pygame.locals import *
import sys
import time
import main_menu,game_UI,realMainMenu
import os
#os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,100)
os.environ['SDL_VIDEO_CENTERED'] = '1'


allgroup = pygame.sprite.LayeredUpdates()
backgroundgroup = pygame.sprite.Group()
buttongroup = pygame.sprite.Group()
penguingroup = pygame.sprite.Group()
playergroup = pygame.sprite.Group()

'''
startMenu = main_menu.mainMenu(allgroup)
allgroup = startMenu.setup(allgroup, backgroundgroup, buttongroup, penguingroup)
startMenu.update(allgroup, backgroundgroup, buttongroup, penguingroup)
'''

startMenu = realMainMenu.mainMenu(allgroup)
allgroup = startMenu.setup(allgroup, backgroundgroup, buttongroup, penguingroup)
startMenu.update(allgroup, backgroundgroup, buttongroup, penguingroup)


pygame.quit()

inGame = game_UI.gameUI(allgroup)
allgroup = inGame.setup(allgroup, backgroundgroup, playergroup, buttongroup)
inGame.update(allgroup)

pygame.quit()