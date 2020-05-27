import pygame
from Car import Car
from block import Block

pygame.init()
screen = pygame.display.set_mode((500, 500),pygame.RESIZABLE)

car = Car(screen)
block = Block((100,100))

walls = pygame.sprite.Group()
walls.add(block)

running = True
Clock = pygame.time.Clock()
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((0,0,0))
	car.update(screen, walls)
	walls.update(screen)
	pygame.display.flip()
	Clock.tick(60)
pygame.quit()
