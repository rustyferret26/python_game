import messages
import blinkt
import time
import pygame
import os
import DS4

os.environ['SDL_VIDEODRIVER'] = "dummy"

# Initialize pygame and everything that's needed with it.
pygame.init()
pygame.joystick.init()
pad=pygame.joystick.Joystick(0)
pad.init()
clock=pygame.time.Clock()
pygame.display.set_mode((1,1))

def game():
	# Default game choice.
	game_choice=1

	x=True
	while x==True:
		for event in pygame.event.get():
			if event.type==pygame.JOYBUTTONDOWN:
				if pad.get_button(DS4.R1())==1:
					if game_choice < 4:
						game_choice +=1
				elif pad.get_button(DS4.L1())==1:
					if game_choice > 1:
						game_choice -=1
				elif pad.get_button(DS4.Cross())==1:
					print("Game choice selected = {}".format(game_choice))
					x=False
					return game_choice

		messages.game_lights(game_choice)
		clock.tick(30)

def difficulty():
	# Default difficulty choice.
	diff_choice=1

	x=True
	while x==True:
		for event in pygame.event.get():
			if event.type==pygame.JOYBUTTONDOWN:
				if pad.get_button(DS4.R1())==1:
					if diff_choice<4:
						diff_choice+=1
				elif pad.get_button(DS4.L1())==1:
					if diff_choice>1:
						diff_choice-=1
				elif pad.get_button(DS4.Cross())==1:
					print("Difficulty selected = {}".format(diff_choice))
					x=False
					return diff_choice

		messages.diff_lights(diff_choice)
		clock.tick(30)

def get_btn():
	x=False
	while x==False:
		for event in pygame.event.get():
			if event.type==pygame.JOYBUTTONDOWN:
				if pad.get_button(DS4.Square())==1:
					print("Square")
					return DS4.Square()
				if pad.get_button(DS4.Cross())==1:
					print("Cross")
					return  DS4.Cross()
				if pad.get_button(DS4.Circle())==1:
					print("Circle")
					return  DS4.Circle()
				if pad.get_button(DS4.Triangle())==1:
					print("Triangle")
					return  DS4.Triangle()
				if pad.get_button(DS4.R1())==1:
					print("R1")
					return DS4.R1()
				if pad.get_button(DS4.L1())==1:
					print("L1")
					return DS4.L1()

			#elif event.type==pygame.JOYBUTTONUP:
			#	x=True
			#	return choice
		clock.tick(30)
