import pygame as pg


class Block(pg.sprite.Sprite):

	def __init__(self, pos, width = 50, height = 50):
		pg.sprite.Sprite.__init__(self)

		self.width = width
		self.height = height
		self.pos = pg.math.Vector2(pos)
		self.img = pg.Surface((self.width, self.height), pg.SRCALPHA)
		self.img.fill((0,255,0))

		self.rect = self.img.get_rect()
		self.rect.center = self.pos

	def update(self, screen):
		img_copy = self.img.copy()

		screen.blit(img_copy, self.rect)
