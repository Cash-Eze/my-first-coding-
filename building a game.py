import pygame
screen_size = [360, 400]
pygame.display.set_mode(screen_size)
screen = pygame.display.set_mode(screen_size)
background= pygame.image.load('background.png')
keep_alive = True
while keep_alive:
	screen.blit(background,[50,500])
	pygame.display.update()
