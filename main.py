import pygame
import user_select
import game_one
import game_two
import time
import controller_test
import os

os.environ['SDL_VIDEODRIVER']="dummy"

# Initialize all things pygame
pygame.init()
pad=pygame.joystick.Joystick(0)
pad.init()
clock=pygame.time.Clock()
pygame.display.set_mode((1,1,))
g2=game_two.init()


def Pad():
	return pad

# Get level choice from user
print("Please select a game")
game = user_select.game()

if game==1:
	print("Game one selected, please select the difficulty..")
	difficulty=user_select.difficulty()
	print("Difficulty level {}, starting game..".format(difficulty))
	if difficulty==1:
		game_one.diff_one()
	elif difficulty==2:
		game_one.diff_two()
	elif difficulty==3:
		game_one.diff_three()
	elif difficulty==4:
		game_one.diff_four()

elif game==2:
	print("starting game_two()")
	g2.init()

elif game==3:
	print("starting game_three()")
#	game_three()

elif game==4:
	print("starting game_four()")
	while True:
		test = controller_test.PS4Controller()
		test.init()
		test.listen()
