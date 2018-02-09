import messages
import blinkt
import time
import pygame
import os

os.environ['SDL_VIDEODRIVER'] = "dummy"

pygame.init()
pygame.joystick.init()
pad=pygame.joystick.Joystick(0)
pad.init()
clock=pygame.time.Clock()
pygame.display.set_mode((1,1))
game_choice=1

in_game=True
while in_game==True:
	for event in pygame.event.get():
		if event.type==pygame.JOYBUTTONDOWN and pad.get_button(5)==1:
			print("Game change")
			if game_choice < 8:
				game_choice += 1
				print("game_choice: {}".format(game_choice))
				print("+1")
			elif game_choice == 8:
				messages.Error()
		elif event.type==pygame.JOYBUTTONDOWN and pad.get_button(4)==1:
			print("level change")
			if game_choice > 1:
				game_choice -=1
				print("game_choice: {}".format(game_choice))
				print("-1")
			elif game_choice == 1:
				messages.Error()
	messages.game_lights(game_choice)
	clock.tick(30)
