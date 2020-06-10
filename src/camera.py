import pygame as pg
from pygame.math import Vector2

class Camera(object):

	def __init__(self, total_width, total_height, view_width = 500, view_height = 500 ):
		self.screen = pg.display.set_mode((view_width, view_height), pg.RESIZABLE)

		self.width = total_width
		self.height = total_height
		self.view_width = view_width
		self.view_height = view_height

		self.offset = Vector2(0,0)

		self.player = None
		self.walls = None

	def update(self, target, events):
		self.screen.fill((0,0,0))

		self.walls.update(self)
		self.player.update(self.walls, target, events, self)


	def scroll(self, offset):
		offset = Vector2(offset)

		self.offset += offset

		if self.player.pos[1] + (self.view_height / 2) > self.height or self.player.pos[1] - (self.view_height / 2) < 0:
			self.offset -= Vector2(0, offset[1])

		if self.player.pos[1] + (self.view_width / 2) > self.width or self.player.pos[1] - (self.view_width / 2) < 0:
			self.offset -= Vector2(offset[0], 0)
