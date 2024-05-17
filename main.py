import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption('Hello World!')

AND = pygame.transform.scale(pygame.image.load("AND gate.png").convert_alpha(),(45,45))#

contactOff = pygame.image.load("contactOff.png").convert_alpha()
contactOn  = pygame.image.load("contactOn.png").convert_alpha()

hud = pygame.image.load("HUD V1.02.png").convert_alpha()
button1 = pygame.transform.scale(pygame.image.load("SmallGrayButton.png").convert_alpha(),(30,10))
spaceButton = pygame.transform.scale(pygame.image.load("SPACEButton.png").convert_alpha(),(60,45))

gridsize = 15

def getCoords(GridTile):
	return (GridTile[0]*15 + 120 , GridTile[1]*15 + 10)

def getGridTile(coords):
	pass
# make this one be used to snap to grid^^^^^^^^^^^^^
gridDark = pygame.transform.scale(pygame.image.load("GridDark.png").convert_alpha(),(gridsize,gridsize))

gridLight = pygame.transform.scale(pygame.image.load("GridLight.png").convert_alpha(),(gridsize,gridsize))

types  ={"AND":AND
				}

def getComponentSprite(type):
	return types[type]

def move_object(object,direction):
	pass
selected_object = ""

class immovable:
	def __init__(self,x,y,sprite):
		self.coords = (x,y)
		self.sprite = sprite

class moveable:
	def __init__(self,x,y,sprite):
		self.coords = (x,y)
		self.sprite = sprite


class component (moveable):
	def __init__(self,x,y,type):
		super().__init__(x,y,0)
		self.type = type
		sprites = {contactOff:(0,0),
							 contactOff:(0,30),
							 getComponentSprite(type):(15,15)
							}
		

class GridSquare (immovable):
	def __init__(self,x,y,sprite):
		super().__init__(x,y,sprite)


class button (immovable):
	def __init__(self,x,y):
		super().__init__(self,x,y)


class smallButton (button):
	def __init__(self,x,y):
		super().__init__(x,y)
		self.sprite = button1


grid = []
t = [gridDark,gridLight]
alt=0
for i in range(71):
	for j in range(45):
		grid.append(GridSquare(15*i+120,15*j+10,t[alt]))
		alt = (j + i + 1) % 2

		print(alt)
HUDelements = [(button1,(70,20)),(button1,(20,20)),(spaceButton,(30,650))]

#components = [component()]

while True:
	for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if pygame.mouse.get_pressed(num_buttons=3)[0]:
						print("clicked")

				if event.type == pygame.KEYDOWN:
					pass
				

				if event.type == QUIT:
					pygame.quit()
					sys.exit()


	#logic
	


			
	
	#draw




	screen.blit(hud,(0,0))

	for element in HUDelements:
		screen.blit(element[0],element[1])

	for element in grid:
		screen.blit(element.sprite,element.coords)

	#print(pygame.mouse.get_rel())

	pygame.display.update()