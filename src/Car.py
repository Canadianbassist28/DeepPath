import pygame as pg
import math

CAR_MAX_TURN_RATE = 1500
CAR_MAX_VELOCITY = 2.5

class Car(pg.sprite.Sprite):

	def  __init__(self, camera, pos):
		pg.sprite.Sprite.__init__(self)
		self.width = 50
		self.height = 50
		self.pos = pg.math.Vector2(pos)
		self.rot = 180
		self.forward = pg.math.Vector2(math.cos(math.radians(self.rot)), math.sin(math.radians(self.rot)))
		self.right = self.forward.rotate(90)

		self.img = pg.Surface((self.width, self.height), pg.SRCALPHA)
		self.img.fill((255,255,255))

		self.rect = self.img.get_rect()
		self.rect.center = self.pos
		self.mask = pg.mask.from_surface(self.img.copy())


	def update(self, walls, target, events, camera):
		img_copy = self.img.copy()
		target_x, target_y  = target
		self.forward = pg.math.Vector2(math.sin(math.radians(self.rot)),
									   math.cos(math.radians(self.rot)))
		self.right = self.forward.rotate(90)

		#--------Update speed--------
		velocity = self.__find_velocity(target)
		dist = (target - self.pos).length()

		old_pos = self.pos
		if dist > 15:
			self.pos += self.forward * velocity
			self.rect.center = self.pos

			#check collision
			if pg.sprite.spritecollideany(self, walls, pg.sprite.collide_mask) is not None:
				self.pos -= self.forward * velocity
				self.rect.center = self.pos

				# add Only X component
				self.pos[0] += (self.forward * velocity)[0]
				self.rect.center = self.pos
				#re-check collision
				if pg.sprite.spritecollideany(self, walls, pg.sprite.collide_mask) is not None:
					self.pos[0] -= (self.forward * velocity)[0]
					self.rect.center = self.pos

				# add Only Y component
				self.pos[1] += (self.forward * velocity)[1]
				self.rect.center = self.pos
				#re-check collision
				if pg.sprite.spritecollideany(self, walls, pg.sprite.collide_mask) is not None:
					self.pos[1] -= (self.forward * velocity)[1]
					self.rect.center = self.pos

		#--------Update Rotation--------
		# get angle to target
		target_rot = math.atan2(target_x - self.pos[0],
								target_y - self.pos[1]) * (180 // math.pi)
		rot_dist = ((target_rot - self.rot) + 180) % 360 - 180
		print(rot_dist)
		rot_dist = max(min(rot_dist, CAR_MAX_TURN_RATE), -CAR_MAX_TURN_RATE)

		if dist > 15:
			if velocity > 0:
				self.rot += (rot_dist / 35)
			else: # reverse rotation when moving backwards
				self.rot += -1 * (rot_dist / 70)
			self.rot = self.rot % 360

		img_copy = pg.transform.rotate(img_copy, self.rot)
		self.rect = img_copy.get_rect()
		self.rect.center = self.pos

		new_pos = self.pos
		self.mask = pg.mask.from_surface(img_copy)

		# Draw Car
		camera.scroll(new_pos - old_pos)
		camera.screen.blit(img_copy, self.rect.topleft + camera.offset)
		pg.draw.line(camera.screen, (255,0,0),self.pos + camera.offset, (self.forward * 25 + self.pos) + camera.offset)
		pg.draw.line(camera.screen, (0,0,255),self.pos + camera.offset, (self.right * 25 + self.pos) + camera.offset)

	def __find_velocity(self, target):
		heading = target - self.pos
		dist = heading.length()
		velocity = max(min(dist * .05, CAR_MAX_VELOCITY), -CAR_MAX_VELOCITY)

		#-----determine forward or reverse-----
		m = ((self.right + self.pos)[1] - self.pos[1]) / ((self.right + self.pos)[0] - self.pos[0] + .000000001)
		b = self.pos[1] - (m * self.pos[0])

		sign = True if  (self.right + self.pos)[0] < self.pos[0] else False # determine if upside-down
		if (target[1] + 20 > (m * target[0] + b)):
			if not sign:
				velocity *= -.5
		else:
			if sign:
				velocity *= -.5

		return velocity
