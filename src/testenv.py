import pygame
from car import Car
from block import Block
from camera import Camera

pygame.init()

camera = Camera(1000, 500)

car = Car(camera, (250,250))

block = Block((100,100))
walls = pygame.sprite.Group()
walls.add(block)

camera.player = car
camera.walls = walls

running = True
Clock = pygame.time.Clock()
while running:

	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			running = False

	camera.update(pygame.mouse.get_pos(), events)
	# car.update(pygame.mouse.get_pos(), screen, walls)
	# walls.update(screen)
	pygame.display.flip()
	Clock.tick(60)
pygame.quit()
