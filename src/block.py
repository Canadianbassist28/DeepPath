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
		self.mask = pg.mask.from_surface(self.img.copy())

	def update(self, camera):
		img_copy = self.img.copy()
		camera.screen.blit(img_copy, self.rect.topleft - camera.offset)
