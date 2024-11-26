import pygame, sys, paddle

def gameloop():
	screen.fill(pygame.color.Color('cornsilk4'))
	pygame.draw.rect(screen, light_grey, player)

pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

light_grey = (200,200,200)
player = paddle.Player((screen_height/2, screen_width/2, 140, 10))

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	gameloop()

	pygame.display.flip()
	clock.tick(60)