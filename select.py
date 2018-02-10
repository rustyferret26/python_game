import messages
import blinkt
import time
import pygame
import os

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

	in_game=True
	while in_game==True:
		for event in pygame.event.get():
			if event.type==pygame.JOYBUTTONDOWN:
				if pad.get_button(5)==1:
					if game_choice < 4:
						game_choice +=1
				elif pad.get_button(4)==1:
					if game_choice > 1:
						game_choice -=1
				elif pad.get_button(1)==1:
					print("Game choice selected = {}".format(game_choice))
					return game_choice

		messages.game_lights(game_choice)
		clock.tick(30)

def difficulty():
	diff_choice=1

	while True:
		for event in pygame.event.get():
			if event.type==pygame.JOYBUTTONDOWN:
				if pad.get_button(5)==1:
					if diff_choice<4:
						diff_choice+=1
				elif pad.get_button(5)==1:
					if diff_choice>1:
						diff_choice-=1
				elif pad.get_button(1)==1:
					print("Difficulty selected = {}".format(diff_choice))

		if diff_choice==1:
			diff_bar(0.2,0,0,0)
		elif diff_choice==2:
			diff_bar(0.2,0.2,0,0)
		elif diff_choice==3:
			diff_bar(0.2,0.2,0.2,0)
		elif diff_choice==4:
			diff_bar(0.2,0.2,0.2,0.2)



def diff_bar(br_1,br_2,br_3,br_4):
	blinkt.clear()
	blinkt.set_pixel(0,0,255,0,br_1)
	blinkt.set_pixel(1,100,255,0,br_1)
	blinkt.set_pixel(2,140,255,0,br_2)
	blinkt.set_pixel(3,210,240,0,br_2)
	blinkt.set_pixel(4,255,215,0,br_3)
	blinkt.set_pixel(5,255,150,0,br_3)
	blinkt.set_pixel(6,255,50,0,br_4)
	blinkt.set_pixel(7,255,0,0,br_4)
	blinkt.show()
