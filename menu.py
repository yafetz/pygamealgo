import pygame
import os

pygame.init()

#setting up Window
w = 600
h = 600
run = True
run_Level = False
win = pygame.display.set_mode((w, h))
pygame.display.set_caption('TRY')
background = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "MENU BACKGROUND.png")), (w, h))
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 50)
run = True
x = 170
y = 200
width = 260
height = 50

while (run):
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	selection_box = (x, y , width, height)


	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_DOWN]:
		x = 150
		y = 300
		width = 300
		height = 50
	elif keys[pygame.K_UP] and y == 300:
		x = 170
		y = 200
		width = 260
		height = 50
	elif keys[pygame.K_RETURN ] and y == 200:
		import astar
		run = False
	elif keys[pygame.K_RETURN] and y == 300:
		import dijkstra
		run = False

	win.blit(background, (0,0))
	text=font.render("Run astar ", True, (200,00,00))
	win.blit(text, [180, 200])
	text2=font.render("Run dijkstra", True, (200,00,00))
	win.blit(text2, [150, 300])
	pygame.draw.rect(win, (255, 255, 255), selection_box, 2 )
	pygame.display.update()

