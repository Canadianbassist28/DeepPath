import pygame as pg
import math

CAR_MAX_TURN_RATE = 1500
CAR_MAX_VELOCITY = 2.5

class Car(pg.sprite.Sprite):

	def  __init__(self, screen):
		pg.sprite.Sprite.__init__(self)
		self.screen = screen
		self.width = 50
		self.height = 50
		self.pos = pg.math.Vector2((screen.get_width() // 2, screen.get_height() // 2))
		self.rot = 0
		self.forward = pg.math.Vector2(math.cos(math.radians(self.rot)), math.sin(math.radians(self.rot)))
		self.right = self.forward.rotate(90)

		self.img = pg.Surface((self.width, self.height), pg.SRCALPHA)
		self.img.fill((255,255,255))

		self.rect = self.img.get_rect()
		self.rect.center = self.pos

	def update(self, screen, walls):
		img_copy = self.img.copy()
		mouse_x, mouse_y  = pg.mouse.get_pos()
		self.forward = pg.math.Vector2(math.sin(math.radians(self.rot)), math.cos(math.radians(self.rot)))
		self.right = self.forward.rotate(90)

		#--------Update speed--------
		velocity = self.__find_velocity()
		dist = (pg.mouse.get_pos() - self.pos).length()

		if dist > 15:
			old_pos = self.pos
			self.pos += self.forward * velocity
			self.rect.center = self.pos

			#check collision
			if pg.sprite.spritecollideany(self, walls) is not None:
				self.pos = old_pos
				self.rect.center = self.pos

				# add Only X component
				self.pos[0] += (self.forward * velocity)[0]
				self.rect.center = self.pos
				#re-check collision
				if pg.sprite.spritecollideany(self, walls) is not None:
					self.pos[0] -= 2 * (self.forward * velocity)[0]
					self.rect.center = self.pos

				# add Only Y component
				self.pos[1] += (self.forward * velocity)[1]
				self.rect.center = self.pos
				#re-check collision
				if pg.sprite.spritecollideany(self, walls) is not None:
					self.pos[1] -= 2 * (self.forward * velocity)[1]
					self.rect.center = self.pos

		#--------Update Rotation--------
		target_rot = math.atan2(mouse_x - self.pos[0], mouse_y - self.pos[1]) * (180 // math.pi)
		rot_dist = ((target_rot - self.rot) + 180) % 360 - 180
		rot_dist = max(min(rot_dist, CAR_MAX_TURN_RATE), -CAR_MAX_TURN_RATE)

		if dist > 15:
			self.rot += (rot_dist / 35)
			self.rot = self.rot % 360

		img_copy = pg.transform.rotate(img_copy, self.rot)
		self.rect = img_copy.get_rect()
		self.rect.center = self.pos

		# Draw Car
		screen.blit(img_copy, self.rect)
		pg.draw.line(screen, (255,0,0),self.pos, (self.forward * 25 + self.pos))
		pg.draw.line(screen, (0,0,255),self.pos, (self.right * 25 + self.pos))

	def __find_velocity(self):
		mouse_pos = pg.mouse.get_pos()
		heading = mouse_pos - self.pos
		dist = heading.length()
		velocity = max(min(dist * .05, CAR_MAX_VELOCITY), -CAR_MAX_VELOCITY)

		#-----determine forward or reverse-----
		m = ((self.right + self.pos)[1] - self.pos[1]) / ((self.right + self.pos)[0] - self.pos[0] + .000000001)
		b = self.pos[1] - (m * self.pos[0])

		sign = True if  (self.right + self.pos)[0] < self.pos[0] else False # determine if upside-down
		if (mouse_pos[1] + 20 > (m * mouse_pos[0] + b)):
			if sign:
				velocity *= -1
		else:
			if not sign:
				velocity *= -1

		return -velocity
