import pygame as pg
import math

CAR_MAX_TURN_RATE = 25
CAR_MAX_VELOCITY = .25

class Car(pg.sprite.Sprite):

	def  __init__(self, screen):
		pg.sprite.Sprite.__init__(self)
		self.screen = screen
		self.width = 50
		self.height = 50
		self.pos = pg.math.Vector2((screen.get_width() // 2, screen.get_height() // 2))
		self.rot = 0
		self.forward = pg.math.Vector2(math.cos(math.radians(self.rot)), math.sin(math.radians(self.rot)))

		self.img = pg.Surface((self.width, self.height), pg.SRCALPHA)
		self.img.fill((255,255,255))

		self.rect = self.img.get_rect()
		self.rect.center = self.pos

	def update(self, screen):
		img_copy = self.img.copy()
		mouse_x, mouse_y  = pg.mouse.get_pos()
		self.forward = pg.math.Vector2(math.sin(math.radians(self.rot)), math.cos(math.radians(self.rot)))

		#--------Update speed--------
		heading = pg.mouse.get_pos() - self.pos
		dist = heading.length()
		velocity = max(min(dist * .005, CAR_MAX_VELOCITY), -CAR_MAX_VELOCITY)

		if dist > 10:
			self.pos += self.forward * velocity
			self.rect.center = self.pos

		#--------Update Rotation--------
		target_rot = math.atan2(mouse_x - self.pos[0], mouse_y - self.pos[1]) * (180 // math.pi)
		rot_dist = ((target_rot - self.rot) + 180) % 360 - 180
		rot_dist = max(min(rot_dist, CAR_MAX_TURN_RATE), -CAR_MAX_TURN_RATE)

		if dist > 10:
			self.rot += (rot_dist / 100)
			self.rot = self.rot % 360

		img_copy = pg.transform.rotate(img_copy, self.rot)
		self.rect = img_copy.get_rect()
		self.rect.center = self.pos

		# Draw Car
		screen.blit(img_copy, self.rect)
		pg.draw.line(screen, (255,0,0),self.pos, (self.forward * 25 + self.pos))
