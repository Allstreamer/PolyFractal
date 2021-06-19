import time
import pygame
from vertex import Vertex
import random

# Initilize Pygame !Necesary!
pygame.init()
pygame.display.set_caption("Poly Fractals")

# Pygame / Game Values
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((1280,720))
running = True

font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()

vertices = []

for i in range(3):
	vertices.append(Vertex(random.randint(0, WIDTH),
											random.randint(0, HEIGHT),
											10,
											(255,255,255)))

picked_up = None

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
            
		if event.type == pygame.MOUSEBUTTONUP:
			picked_up = None
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			for i, v in enumerate(vertices):
				if (v.detect_Touch(pos)):
					picked_up = i
					break
   
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
				vertices.append(Vertex(random.randint(0, WIDTH),
										random.randint(0, HEIGHT),
										10,
										(255,255,255)))
    
    # Clear Screen
	screen.fill((0, 0, 0))

	if picked_up != None:
		vertices[picked_up].set_pos(pygame.mouse.get_pos())
    
	for v in vertices:
		v.draw(screen)
     
	for i in range(len(vertices)-1):
		pygame.draw.line(screen,
						(255,255,255),
						vertices[i].get_center_pos(),
						vertices[i+1].get_center_pos())

	# Draw Last connection Line
	if len(vertices) > 0:
		pygame.draw.line(screen,
						(255,255,255),
						vertices[0].get_center_pos(),
						vertices[-1].get_center_pos())
  
  
	if len(vertices) >= 3:
		random.seed(1)
		pos = [WIDTH/2, HEIGHT/2]
		last = None
		for i in range(10000):
			while True:
				vert = random.randint(0, len(vertices)-1)
				if vert != last:
					break
				last = vert
			pos[0] = (int)((pos[0] + vertices[vert].x) / 2)
			pos[1] = (int)((pos[1] + vertices[vert].y) / 2)
			screen.set_at((pos[0], pos[1]), (255,255,255))


	fps = font.render(str(int(clock.get_fps())), True, (255,255,255))
	screen.blit(fps, (0, 0))
 
	help_text = font.render("Press + To add vertices", True, (255,255,255))
	screen.blit(help_text, (0, 50))
	help_text = font.render("Click and drag to move Vertices", True, (255,255,255))
	screen.blit(help_text, (0, 70))
    
	clock.tick(75)
	pygame.display.update()