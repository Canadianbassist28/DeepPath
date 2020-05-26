import pygame
import pygame.gfxdraw
from Car import Car
from block import Block

pygame.init()
screen = pygame.display.set_mode((500, 500),pygame.RESIZABLE)

car = Car(screen)
block = Block((100,100))

running = True

while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((0,0,0))
	car.update(screen)
	block.update(screen)
	pygame.display.flip()
	pygame.time.delay(int(1/60))
pygame.quit()
