import pygame
from pygame.locals import *
import sys
import time
from DataTools import constants as c
'''
upImageFilename1 = 'Resources/graphics/Main_Mune_buttom/Play_Unselected14050.png'
downImageFilename1 = 'Resources/graphics/Main_Mune_buttom/Play_selected14050.png'
upImageFilename2 = 'Resources/graphics/Main_Mune_buttom/option_UnSelected10060.png'
downImageFilename2 = 'Resources/graphics/Main_Mune_buttom/option_selected10060.png'
upImageFilename3 = 'Resources/graphics/Main_Mune_buttom/Exit_Unelected10060.png'
downImageFilename3 = 'Resources/graphics/Main_Mune_buttom/Exit_selected10060.png'
upImageFilename4 = 'Resources/graphics/Main_Mune_buttom/Brunch35172.png'

screen = pygame.display.set_mode((270, 360))
pygame.display.set_caption("Monopoly!")
'''


class mainMenu(object):
	def __init__(self, allgroup):
		pygame.init()
		pygame.mixer.init()
		self.screen = pygame.display.set_mode((960, 525))
		pygame.display.set_caption("Monopoly-Tokyo!")
		self.framerate = pygame.time.Clock()

		pygame.font.init()
		self.font = pygame.font.SysFont('kaiti', 12)
		self.font.set_bold(True)
		self.text = self.font.render("©Copyright Dum@$ Game 2019", True, (0,0,0))
		self.screen.blit(self.text,(760,510))

	def setup(self,allgroup, backgroundgroup, buttongroup, penguingroup):

		'''
		self.bg = background("Resources/graphics/title270_480.png", pygame.math.Vector2(0, -20), allgroup, backgroundgroup)

		self.button1 = Button(upImageFilename1, pygame.math.Vector2(90, 220), 2, allgroup, buttongroup)
		self.button2 = Button(upImageFilename2, pygame.math.Vector2(90, 260), 2, allgroup, buttongroup)
		self.button3 = Button(upImageFilename3, pygame.math.Vector2(90, 300), 2, allgroup, buttongroup)
		self.downButton1 = downButton(downImageFilen#L0UJ9UPCC#L0UJ9UPCC#L0UJ9UPCC#L0UJ9UPCCame1, pygame.math.Vector2(90, 220), -2, allgroup, buttongroup)
		self.downButton2 = downButton(downImageFilename2, pygame.math.Vector2(90, 260), -2, allgroup, buttongroup)
		self.downButton3 = downButton(downImageFilename3, pygame.math.Vector2(90, 300), -2, allgroup, buttongroup)

		self.dancing = penguin(self.screen, allgroup, penguingroup)
		self.dancing.load("Resources/graphics/dancingPenguin270.png", 270, 270, pygame.math.Vector2(0, 0))
'''
		
		self.button4 = Button(c.brunch, pygame.math.Vector2(90, 350), 2, allgroup, buttongroup)

		self.button1 = Button(c.play_Button_Up, pygame.math.Vector2(170, 300), 2, allgroup, buttongroup)
		self.button2 = Button(c.option_Button_Up, pygame.math.Vector2(55, 380), 2, allgroup, buttongroup)
		self.button3 = Button(c.exit_Button_Up, pygame.math.Vector2(60, 440), 2, allgroup, buttongroup)
		self.downButton1 = downButton(c.play_Button_Down, pygame.math.Vector2(170, 300), -2, allgroup, buttongroup)
		self.downButton2 = downButton(c.option_Button_Down, pygame.math.Vector2(55, 380), -2, allgroup, buttongroup)
		self.downButton3 = downButton(c.exit_Button_Down, pygame.math.Vector2(60, 440), -2, allgroup, buttongroup)
		

		self.bg = background(c.main_Menu_Logo, pygame.math.Vector2(20, 100), allgroup, backgroundgroup)

		self.JB = train(self.screen, allgroup, penguingroup)
		self.JB.load(c.train_Anime, 960, 525, pygame.math.Vector2(0, 0))

		self.dancing = penguin(self.screen, allgroup, penguingroup)
		self.dancing.load(c.dancing_Penguin, 205, 205, pygame.math.Vector2(700, 300))

		#self.dancing = penguin(self.screen, allgroup, penguingroup)
		#self.dancing.load("Resources/graphics/dancingPenguin270.png", 270, 270, pygame.math.Vector2(0, 0))

		pygame.mixer.music.load(c.main_Menu_BGM)
		pygame.mixer.music.set_volume(1)
		pygame.mixer.music.play(-1, 0)

		pygame.display.update()

		return allgroup



	def update(self,allgroup, backgroundgroup, buttongroup, penguingroup):
		self.switch = False
		while not self.switch:
			self.framerate.tick(30)
			ticks = pygame.time.get_ticks()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			
				if event.type == pygame.MOUSEBUTTONDOWN:
					if self.button3.isOver():
						sys.exit()

					elif self.button1.isOver():
						backgroundgroup.empty()
						buttongroup.empty()
						penguingroup.empty()
						allgroup.remove_sprites_of_layer(-2)
						allgroup.remove_sprites_of_layer(1)
						allgroup.remove_sprites_of_layer(2)
						self.screen = pygame.display.quit()
						self.switch = True
						break

				if event.type == pygame.MOUSEBUTTONUP:
					if self.button3.isOver():
						sys.exit()

			if self.switch:
				break


			allgroup.update(ticks,allgroup)
			allgroup.draw(self.screen)
			self.screen.blit(self.text,(760,510))
			pygame.display.update()





class Button(pygame.sprite.Sprite):
	def __init__(self, upimage, position, layer, allgroup, buttongroup):
		self.group = allgroup, buttongroup
		self._layer = layer
		pygame.sprite.Sprite.__init__(self, self.group)
		self.image = pygame.image.load(upimage).convert_alpha()
		self.pos = position
		self.rect = self.image.get_rect()
		self.rect.x = self.pos.x
		self.rect.y = self.pos.y

	def isOver(self):
		point_x, point_y = pygame.mouse.get_pos()
		x = self.pos.x
		y = self.pos.y
		w, h = self.image.get_size()

		#in_x = x - w / 2 < point_x < x + w / 2
		#in_y = y - h / 2 < point_y < y + h / 2
		in_x = x  < point_x < x + w 
		in_y = y  < point_y < y + h 
		return in_x and in_y

	def udpate(self,current_time,allgroup):
		w, h = self.image.get_size()
		x = self.pos.x
		y = self.pos.y

		if self.isOver():
			allgroup.change_layer(self, -2)
			self._layer = -2
		# self.rect.x = 1000
		# self.rect.y = 700
		else:
			allgroup.change_layer(self, 2)
			self._layer = 2
		# self.rect.x = self.pos.x
		# self.rect.y = self.pos.y


class downButton(Button):
	def __init__(self, downimage, position, layer, allgroup, buttongroup):
		Button.__init__(self, downimage, position, layer, allgroup, buttongroup)
		self._layer = layer
		self.rect.x = self.pos.x
		self.rect.y = self.pos.y

	def update(self,current_time, allgroup):
		w, h = self.image.get_size()
		x, y = self.pos

		if self.isOver():
			# self.rect.x = self.pos.x
			# self.rect.y = self.pos.y
			allgroup.change_layer(self, 2)
			self._layer = 2

		else:
			allgroup.change_layer(self, -2)
			self._layer = -2
		# self.rect.x = 1000
		# self.rect.y = 700


class background(pygame.sprite.Sprite):
	def __init__(self, image, position, allgroup, backgroundgroup):
		self.group = allgroup, backgroundgroup
		self._layer = 1
		pygame.sprite.Sprite.__init__(self, self.group)
		self.image = pygame.image.load(image).convert_alpha()
		self.pos = position
		self.rect = self.image.get_rect()
		self.rect.x = self.pos.x
		self.rect.y = self.pos.y

	def update(self, current_time, allgroup):
		# screen.fill((250,250,250))
		pass


class penguin(pygame.sprite.Sprite):
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
		self.columns = 2
		self.last_time = 0


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

	def update(self, current_time, allgroup, rate=300):
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

class train(penguin):
	def __init__(self, target, allgroup, backgroundgroup):
		penguin.__init__(self, target, allgroup, backgroundgroup)
		self.columns = 7
		self.rows = 7
		allgroup.change_layer(self, -3)
		self._layer = -3


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

	def update(self, current_time, allgroup, rate=50):
		if self.frame != self.last_frame:
			if current_time > self.last_time + rate:
				self.frame += 1
				self.last_time = current_time

			if self.frame != self.old_frame:
				frame_x = (self.frame % self.columns) * self.frame_width
				frame_y = (self.frame // self.columns) * self.frame_height
				rect = (frame_x, frame_y, self.frame_width, self.frame_height)
				self.image = self.master_image.subsurface(rect)
				self.old_frame = self.frame




#class mainPage(object):



'''
bg = background("Resources/graphics/title270_480.png", pygame.math.Vector2(0, -20))

button1 = Button(upImageFilename1, pygame.math.Vector2(90, 220), 2)
button2 = Button(upImageFilename2, pygame.math.Vector2(90, 260), 2)
button3 = Button(upImageFilename3, pygame.math.Vector2(90, 300), 2)
downButton1 = downButton(downImageFilename1, pygame.math.Vector2(90, 220), -1)
downButton2 = downButton(downImageFilename2, pygame.math.Vector2(90, 260), -1)
downButton3 = downButton(downImageFilename3, pygame.math.Vector2(90, 300), -1)

dancing = penguin(screen)
dancing.load("Resources/graphics/dancingPenguin270.png", 270, 270, pygame.math.Vector2(0, 0))

pygame.mixer.music.load("Resources/music/mainMenu.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1, 0)

pygame.display.update()

framerate = pygame.time.Clock()

while True:
	framerate.tick(6)
	ticks = pygame.time.get_ticks()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			if button3.isOver():
				sys.exit()

		if event.type == pygame.MOUSEBUTTONUP:
			if button3.isOver():
				sys.exit()

			#elif button1.isOver():




	bg.update(ticks)
	button1.render()
	button2.render()
	button3.render()
	downButton1.render()
	downButton2.render()
	downButton3.render()
	dancing.update(ticks)
	allgroup.update(ticks)
	allgroup.draw(screen)
	pygame.display.update()
'''
'''
startMenu = mainMenu()
allgroup = startMenu.setup()
startMenu.update(allgroup)

pygame.quit()
'''

#gameUI = mainPage()
