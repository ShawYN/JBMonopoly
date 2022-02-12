import pygame
from pygame.locals import *
import sys
import time
import realMainMenu
from realMainMenu import Button, downButton
import random
import constants as c
import threading

move = False
change = False
totalstep = 0

def blit_text(surface, text, pos, font, color = (255,255,255)):
    words = [word.split(' ') for word in text.splitlines()]   # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    max_width -= 50
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

class gameUI(object):
	def __init__(self, allgroup):
		pygame.init()
		pygame.mixer.init()
		self.screen = pygame.display.set_mode((1280, 720))
		pygame.display.set_caption("Monopoly!")
		self.framerate = pygame.time.Clock()

		pygame.font.init()
		self.font1 = pygame.font.Font(c.chalk_Font, 40)
		self.font1.set_bold(False)
		self.font2 = pygame.font.Font(c.chalk_Font, 20)
		self.font2.set_bold(False)
		self.text = self.font1.render(c.station_Name[0], True, (255,255,255))
		self.screen.blit(self.text,(805,150))
		blit_text(self.screen,c.station_Description[0],(810,250),self.font2)
		#self.text2 = self.font2.render(c.station_Description[0], True, (255,255,255))
		#self.screen.blit(self.text2,(810,250))

	def setup(self,allgroup, backgroundgroup, playergroup, buttongroup):
		#self.bg = realMainMenu.background(c.blank_Background, pygame.math.Vector2(0, 0), allgroup, backgroundgroup)
		self.map = realMainMenu.background(c.gaming_Map, pygame.math.Vector2(0, 0), allgroup, backgroundgroup)
		#self.logo = realMainMenu.background(c.gaming_UI_Logo, pygame.math.Vector2(260, 160), allgroup, backgroundgroup)
		#self.playerProfile = realMainMenu.background(c.player_Profile, pygame.math.Vector2(1030, 0), allgroup, backgroundgroup)

		i = 0
		self.block = [None for i in range(36)] 
		for i in range(0,10):
			self.block[i] = blocks(i, pygame.math.Vector2(640-i*60,595), 60, 70)

		for i in range(10,19):
			self.block[i] = blocks(i, pygame.math.Vector2(100,595-(i-9)*60), 70, 60)

		for i in range(19,28):
			self.block[i] = blocks(i, pygame.math.Vector2(100+(i-18)*60,55), 60, 70)

		for i in range(28,36):
			self.block[i] = blocks(i, pygame.math.Vector2(640,55+(i-27)*60), 70, 60)


		self.player1 = player(self.screen, allgroup, playergroup)
		self.player1.load(c.player_Anime1,64,64,pygame.math.Vector2(640,595), 2)

		self.button1 = realMainMenu.Button(c.start_Button_Up, pygame.math.Vector2(790, 606), 2, allgroup, buttongroup)
		self.downButton1 = realMainMenu.downButton(c.start_Button_Down, pygame.math.Vector2(790, 608), -2, allgroup, buttongroup)
		self.button2 = realMainMenu.Button(c.setting_Button_Up, pygame.math.Vector2(1177,605), 2, allgroup, buttongroup)
		self.downButton2 = realMainMenu.downButton(c.setting_Button_Down, pygame.math.Vector2(1177,605), -2, allgroup, buttongroup)
		
		
		self.dice = dice(self.screen, allgroup, playergroup)
		self.dice.load(c.Dice_Anime,100,100,pygame.math.Vector2(794,40))

		pygame.mixer.music.load(c.gaming_UI_BGM)
		pygame.mixer.music.set_volume(1)
		pygame.mixer.music.play(-1, 0)

		pygame.display.update()

		return allgroup


	def update(self,allgroup):
		while True:
			self.framerate.tick(360)
			ticks = pygame.time.get_ticks()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			'''if event.type == pygame.MOUSEBUTTONDOWN:
				
				if self.button1.isOver():
					step = threading.Thread(target = self.dice.roll).start()
					#step = self.dice.roll()
					#global totalstep
					#totalstep += step
					#print(step)
					#global move 
					#move = True
					#sys.exit()

				time.sleep(1)
			global change

			if move:
				if not change:
					self.player1.changeImg()
					change = True'''
			if event.type == pygame.MOUSEBUTTONDOWN:
				global change
				if self.button1.isOver() and not change:
					step = threading.Thread(target=self.dice.roll).start()
					self.player1.changeImg()
					change = True
				time.sleep(1)
			if move:
				#if not change:
					#self.player1.changeImg()
					#change = True

				self.player1.movePlayer(step, ticks, self.block)
				self.text = self.font1.render(c.station_Name[totalstep%36], True, (255,255,255))
				#self.text2 = self.font2.render(c.station_Description[totalstep], True, (255,255,255))
		
				#print("tot",totalstep)

			allgroup.update(ticks,allgroup)
			allgroup.draw(self.screen)
			self.screen.blit(self.text,(805,150))
			blit_text(self.screen,c.station_Description[totalstep%36],(810,250),self.font2)
			pygame.display.update()


class player(pygame.sprite.Sprite):
	def __init__(self, target, allgroup, penguingroup):
		self.group = allgroup, penguingroup
		self._layer = 2
		pygame.sprite.Sprite.__init__(self, self.group)
		self.target_surface = target
		self.image = None
		self.master_image = None
		self.rect = None
		self.topleft = 0, 0
		self.frame = 0
		self.old_frame = -1
		self.frame_width = 1
		self.frame_height = 1
		self.first_frame = 0
		self.last_frame = 0
		self.columns = 1
		self.last_time = 0

	def load(self, filename, width, height, position, columns):
		self.master_image = pygame.image.load(filename).convert_alpha()
		self.frame_width = width
		self.frame_height = height
		self.pos = position
		self.rect = self.master_image.get_rect()
		self.rect.x = self.pos.x
		self.rect.y = self.pos.y
		self.columns = columns
		rect = self.master_image.get_rect()
		self.last_frame = (rect.width // width) * (rect.height // height) - 1

		self.last_rect = self.pos
		self.last_rect.x = self.pos.x
		self.last_rect.y = self.pos.y


	def movePlayer(self, step, current_time, block):
		#self.pos.x += speed.x

		global totalstep

		if totalstep > 0 and totalstep < 9:
			if self.rect.x > block[totalstep].pos.x :
					self.rect.x -= 1

			else:
				self.last_rect.x = self.rect.x
				#print(1)
				global move
				move = False
				player.changeImg(self)
				global change
				change = False

		elif totalstep == 9:
			if self.rect.x > (block[9].pos.x):
					self.rect.x -= 1

			else:
				move = False
				player.changeImg(self)
				change = False

		elif totalstep > 9 and totalstep < 18:
			if self.rect.x > (block[9].pos.x):
					self.rect.x -= 1

			else:

				if self.rect.y > block[totalstep].pos.y:
					self.rect.y -= 1

				else:
					move = False
					player.changeImg(self)
					change = False

		elif totalstep == 18:
			if self.rect.y > block[18].pos.y:
					self.rect.y -= 1

			else:
				move = False
				player.changeImg(self)
				change = False

		elif totalstep > 18 and totalstep < 27:
			if self.rect.y > block[18].pos.y:
					self.rect.y -= 1

			else:
				if self.rect.x < block[totalstep].pos.x:
					self.rect.x += 1

				else:
					move = False
					player.changeImg(self)
					change = False

		elif totalstep == 27:
			if self.rect.x < block[27].pos.x:
					self.rect.x += 1

			else:
				move = False
				player.changeImg(self)
				change = False

		elif totalstep > 27 and totalstep < 36:
			if self.rect.x < block[27].pos.x:
					self.rect.x += 1

			else:

				if self.rect.y < block[totalstep].pos.y:
					self.rect.y += 1

				else:
					move = False
					player.changeImg(self)
					change = False

		elif totalstep == 0 or totalstep == 36:
			if self.rect.y < block[0]. pos.y:
					self.rect.y += 1

			else:
				move = False
				player.changeImg(self)
				change = False

		elif totalstep > 36 and totalstep < 45:
			if self.rect.y < block[0].pos.y:
					self.rect.y += 1

			else:
				totalstep -= 36
				

		'''
		if self.rect.y > (self.last_rect.y - step * 60):
			#if current_time > self.last_time + rate:
			self.rect.y -= 0.1

			print(self.rect.y)
			print(self.last_rect.y)
			print()

			#print(self.rect.y)
				#self.last_time = current_time
		else:
			self.last_rect.y = self.rect.y
			print(1)
			global move
			move = False
			player.changeImg(self)
			global change
			change = False
'''
	def changeImg(self):
		print(change, move)
		if move:
			player.load(self,c.player_Anime2,self.frame_width,self.frame_height,pygame.math.Vector2(self.rect.x,self.rect.y),4)
		else:
			player.load(self,c.player_Anime1,self.frame_width,self.frame_height,pygame.math.Vector2(self.rect.x,self.rect.y),2)

	def update(self, current_time, allgroup, rate=180):
		if current_time > self.last_time + rate:
			self.frame += 1
			if self.frame > self.last_frame:
				self.frame = self.first_frame
			self.last_time = current_time

		if self.frame != self.old_frame:
			frame_x = (self.frame % self.columns) * self.frame_width
			frame_y = (self.frame // self.columns) * self.frame_height
			rect = (frame_x, frame_y, self.frame_width, self.frame_height)
			self.image = self.master_image.subsurface(rect)
			self.old_frame = self.frame



'''
class player(pygame.sprite.Sprite):
	def __init__(self, image, position, layer, allgroup, playergroup, width, height, target, columns):
		self.group = allgroup,playergroup
		self._layer = layer
		pygame.sprite.Sprite.__init__(self,self.group)
		self.target_surface = target

		self.master_image = pygame.image.load(image).convert_alpha()
		self.image = None

		self.topleft = 0, 0
		self.frame = 0
		self.old_frame = -1
		self.frame_width = width
		self.frame_height = height
		self.first_frame = 0
		self.last_frame = (rect.width // width) * (rect.height // height) - 1
		self.columns = column


		self.pos = position
		self.rect = self.master_image.get_rect()
		self.rect.x = self.pos.x
		self.rect.y = self.pos.y
		self.last_time = 0
		self.last_rect = self.pos
		self.last_rect.x = self.pos.x
		self.last_rect.y = self.pos.y


	def movePlayer(self, step, current_time):
		#self.pos.x += speed.x
		if self.rect.y > (self.last_rect.y - step * 60):
			#if current_time > self.last_time + rate:
			self.rect.y -= 1

			print(self.rect.y)
			print(self.last_rect.y)
			print()

			#print(self.rect.y)
				#self.last_time = current_time
		else:
			self.last_rect.y = self.rect.y
			print(1)
			global move
			move = False


	def update(self,current_time, allgroup, rate = 60):
		if current_time > self.last_time + rate:
			self.frame += 1
			if self.frame > self.last_frame:
				self.frame = self.first_frame
			self.last_time = current_time

		if self.frame != self.old_frame:
			frame_x = (self.frame % self.columns) * self.frame_width
			frame_y = (self.frame // self.columns) * self.frame_height
			rect = (frame_x, frame_y, self.frame_width, self.frame_height)
			self.image = self.master_image.subsurface(rect)
			self.old_frame = self.frame

'''

class dice(realMainMenu.penguin):
	def __init__(self, target, allgroup, penguingroup):
		realMainMenu.penguin.__init__(self, target, allgroup, penguingroup)
		self.columns = 6
		self.status = False
		self.step = 1

	def load(self, filename, width, height, position):
		self.master_image = pygame.image.load(filename).convert_alpha()
		self.frame_width = width
		self.frame_height = height
		self.pos = position
		self.rect = self.master_image.get_rect()
		self.rect.x = self.pos.x
		self.rect.y = self.pos.y
		rect = self.master_image.get_rect()
		self.last_frame = (rect.width // width) * (rect.height // height) - 1

	def update(self, current_time, allgroup, rate=100):
		if self.status:
			if current_time > self.last_time + rate:
				self.frame += 1
				if self.frame > self.last_frame:
					self.frame = self.first_frame
				self.last_time = current_time

			if self.frame != self.old_frame:
				frame_x = (self.frame % self.columns) * self.frame_width
				frame_y = (self.frame // self.columns) * self.frame_height
				rect = (frame_x, frame_y, self.frame_width, self.frame_height)
				self.image = self.master_image.subsurface(rect)
				self.old_frame = self.frame
		else:
			rect = ((self.step-1)*self.frame_width, 0, self.frame_width, self.frame_height)
			self.image = self.master_image.subsurface(rect)


	def roll(self):
		self.status = True
		time.sleep(1)
		self.status = False
		self.step = random.randint(1,6)
		global totalstep
		totalstep += self.step
		print(self.step)
		global move
		move = True
		#return random.randint(1,6)
		return self.step

class blocks(object):
	def __init__(self, index, position, width, height):
		self.index = index
		self.pos = position
		#self.info = information
		self.center = pygame.math.Vector2((self.pos.x + width/2), (self.pos.y + height/2))






