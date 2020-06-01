import pygame as pg
from pygame.math import Vector2

class Camera(object):

	def __init__(self, total_width, total_height, view_width = 500, view_height = 500 ):
		self.screen = pg.display.set_mode((view_width, view_height), pg.RESIZABLE)

		self.width = total_width
		self.height = total_height

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
