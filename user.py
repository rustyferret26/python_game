import pygame
import DS4
import os

os.environ['SDL_VIDEODRIVER'] = "dummy"

pygame.init()
pygame.joystick.init()
pad=pygame.joystick.Joystick(0)
pad.init()
clock = pygame.time.Clock()
pygame.display.set_mode((1,1))

def get_btn():
	done=False
	while done==False:
		for event in pygame.event.get():
			if event.type==pygame.JOYBUTTONDOWN:
				if pad.get_button(DS4.Square())==1:
					print("Square")
					return DS4.Square()
				elif pad.get_button(DS4.Cross())==1:
					print("Cross")
					return DS4.Cross()
				elif pad.get_button(DS4.Circle())==1:
					print("Circle")
					return DS4.Circle()
				elif pad.get_button(DS4.Triangle())==1:
					print("Triangle")
					return DS4.Triangle()
				elif pad.get_button(DS4.R1())==1:
					print("R1")
					return DS4.R1()
				elif pad.get_button(DS4.L1())==1:
					print("L1")
					return DS4.L1()
		clock.tick(30)
