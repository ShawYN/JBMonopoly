

totalstep += step

while totalstep > 35:
	totalstep-=36


if totalstep > 0 and totalstep < 9:
	if self.rect.x > (self.last_rect.x - step * 60):
			#if current_time > self.last_time + rate:
			self.rect.x -= 1

			print(self.rect.x)
			print(self.last_rect.x)
			print()

			#print(self.rect.y)
				#self.last_time = current_time
		else:
			self.last_rect.x = self.rect.x
			print(1)
			global move
			move = False
			player.changeImg(self)
			global change
			change = False

elif totalstep == 9:
	if self.rect.x > (block[9]. center.x):
			#if current_time > self.last_time + rate:
			self.rect.x -= 1

			print(self.rect.x)
			print(self.last_rect.x)
			print()

			#print(self.rect.y)
				#self.last_time = current_time
		else:
			self.last_rect.x = self.rect.x
			print(1)
			global move
			move = False
			player.changeImg(self)
			global change
			change = False

elif totalstep > 9 and totalstep < 18:
	if self.rect.x > (block[9]. center.x):
			#if current_time > self.last_time + rate:
			self.rect.x -= 1

			print(self.rect.x)
			print(self.last_rect.x)
			print()

	else:
		self.last_rect.x = self.rect.x

		if self.rect.y > (self.last_rect.y - (totalstep-9) * 60):
			#if current_time > self.last_time + rate:
			self.rect.y -= 1

			print(self.rect.y)
			print(self.last_rect.y)
			print()
		else:
			self.last_rect.y = self.rect.y
			print(1)
			global move
			move = False
			player.changeImg(self)
			global change
			change = False

elif totalstep == 18:
	if self.rect.y > (block[18]. center.y):
			#if current_time > self.last_time + rate:
			self.rect.y -= 1

			print(self.rect.y)
			print(self.last_rect.y)
			print()

			#print(self.rect.y)
				#self.last_time = current_time
		else:
			self.last_rect.x = self.rect.x
			print(1)
			global move
			move = False
			player.changeImg(self)
			global change
			change = False

elif totalstep > 18 and totalstep < 27:
	if self.rect.y > (block[18]. center.y):
			#if current_time > self.last_time + rate:
			self.rect.y -= 1

			print(self.rect.y)
			print(self.last_rect.y)
			print()

	else:
		self.last_rect.y = self.rect.y

		if self.rect.x < (self.last_rect.x - (totalstep-18) * 60):
			#if current_time > self.last_time + rate:
			self.rect.x += 1

			print(self.rect.x)
			print(self.last_rect.x)
			print()
		else:
			self.last_rect.x = self.rect.x
			print(1)
			global move
			move = False
			player.changeImg(self)
			global change
			change = False

elif totalstep == 27:
	if self.rect.x < (block[27]. center.x):
			#if current_time > self.last_time + rate:
			self.rect.x += 1

			print(self.rect.x)
			print(self.last_rect.x)
			print()

			#print(self.rect.y)
				#self.last_time = current_time
		else:
			self.last_rect.x = self.rect.x
			print(1)
			global move
			move = False
			player.changeImg(self)
			global change
			change = False

elif totalstep > 27 and totalstep < 36:
	if self.rect.x < (block[27]. center.x):
			#if current_time > self.last_time + rate:
			self.rect.x += 1

			print(self.rect.x)
			print(self.last_rect.x)
			print()

	else:
		self.last_rect.x = self.rect.x

		if self.rect.y < (self.last_rect.x - (totalstep-27) * 60):
			#if current_time > self.last_time + rate:
			self.rect.y += 1

			print(self.rect.y)
			print(self.last_rect.y)
			print()
		else:
			self.last_rect.y = self.rect.y
			print(1)
			global move
			move = False
			player.changeImg(self)
			global change
			change = False

elif totalstep == 0:
	if self.rect.y < (block[0]. center.y):
			#if current_time > self.last_time + rate:
			self.rect.y += 1

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