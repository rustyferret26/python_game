import pygame
import blinkt
import time
import random
import select

pygame.init()
pygame.joystick.init()
joystick=pygame.joystick.Joystick(0)
joystick.init()
clock = pygame.time.Clock()

## Level booleans
start=False

## Brightness
br = 0.05

## GAME STATS
round_speed = 1
player_score = 0
level=1

## TRANSLATE BUTTONS
pad_square = 0 # Pink
pad_cross = 1 # Blue
pad_circle = 2 # Red
pad_triangle = 3 # Green
pad_left = () # Hat left
pad_right = (1,0) # Hat right
pad_start = 9 # Start
pad_select = 8 # Select

## FUNCTIONS
def Blink(s): # Light blinks for half the given speed value.
	blinkt.show()
	time.sleep(s / 2)
	blinkt.clear()
	blinkt.show()
	time.sleep(s / 2)

def RightLight(s): # Light blinks for half the given speed value.
	for i in range(blinkt.NUM_PIXELS):
		blinkt.set_pixel(i, 255, 255, 255, br)
		blinkt.show()
		time.sleep((s/2)/8)
		blinkt.clear()
		blinkt.show()
		time.sleep(s / 2)

def LeftLight(s): # Light blinks for half the given speed value.
	for i in range(blinkt.NUM_PIXELS):
		blinkt.set_pixel((7-i), 255, 255, 255, br)
		blinkt.show()
		time.sleep((s/2)/8)
		blinkt.clear()
		blinkt.show()
		time.sleep(s / 2)

def Const(s): # Light remains on for the given speed value
	blinkt.show()
	time.sleep(s)
	blinkt.clear()
	blinkt.show()

def Strobe(s): # Light remains on for the given speed value
	for x in range(0,4):
		blinkt.set_brightness(0)
		time.sleep(s / 2)
		blinkt.set_brightness(br)
		time.sleep(s / 2)

def Triangle(): # Sets all LED to Green
	blinkt.set_all(0, 205, 0, br)
	return "Triangle"

def Circle(): # Red
	blinkt.set_all(205, 0, 0, br)
	return "Circle"

def Cross(): # Blue
	blinkt.set_all(0, 0, 205, br)
	return "Cross"

def Square(): # Pink
	blinkt.set_all(225, 20, 147, br)
	return "Square"

def WINNER(points, speed):
	print("Well Done!")
	global round_speed
	global player_score
	round_speed -= speed
	player_score += points # Add points to players total score
	for x in range(0,5): # Strobe green
		blinkt.set_all(0, 255, 0, 0.5)
		Blink(0.2)
	time.sleep(0.5)

def LOSER():
	global player_score
	print("Bad luck")
	print("Your score was: {}".format(player_score)) # Print score to console
	for x in range(0,5): # Strobe red
		blinkt.set_all(255, 0, 0, 0.5)
		Blink(0.2)

def GetUserInput():
	done = False
	while done==False:
		for event in pygame.event.get(): # User did something
			if event.type==pygame.JOYBUTTONDOWN and joystick.get_button(pad_square)==1:
				choice = pad_square
			if event.type==pygame.JOYBUTTONDOWN and joystick.get_button(pad_cross)==1:
				choice = pad_cross
			if event.type==pygame.JOYBUTTONDOWN and joystick.get_button(pad_circle)==1:
				choice = pad_circle
			if event.type==pygame.JOYBUTTONDOWN and joystick.get_button(pad_triangle)==1:
				choice = pad_triangle
			if event.type==pygame.JOYBUTTONDOWN and joystick.get_button(4)==1:
				choice = 4
			if event.type==pygame.JOYBUTTONDOWN and joystick.get_button(5)==1:
				choice = 5
			if event.type==pygame.JOYBUTTONUP:
				done==True
				print("Your choice: {}".format(str(choice)))
				return choice
				clock.tick(20)

## Dificulty 1 - 	Using only 4 varients, pi will start by showing you three numbers that
## 			you have to then repeat back to it. Each time the number will increment
##			by one and the game will speed up.

def Level_One_Game():
	done=False
	while done==False:
		for r in range(1,1000):
			print("Starting Game"

			## Starting 
			start = r + 3 

            		## Results arrays for comparison
			correct = []
			attempt = []

            		## DISPLAY A SEQUENCE OF COLOURS TO PLAYER
			for x in range(1,start):
				sq = random.randrange(0,4) # rand num between 0,1,2,3
				correct.append(sq) # add sequence to array
				if sq==0:
					result = Square()
					Blink(round_speed)
				if sq==1:
					result = Cross()
					Blink(round_speed)
				if sq==2:
					result = Circle()
					Blink(round_speed)
				if sq==3:
					result = Triangle()
					Blink(round_speed)

            		## AWAIT PLAYER TO INPUT THEIR SEQUENCE
			for x in range(1,start):
				attempt.append(GetUserInput())

			time.sleep(1) ## 1s delay for user experience

            		## ASSERT ON ARRAYS
			if correct==attempt:
				WINNER(1, 0.05) # (points|Speed Increase)
			else:
				LOSER()
				done=True
				break
		clock.tick(20)

def Level_Two_Game():
	time.sleep(1)
	print("Difficulty not available")
#    time.sleep(3)
#    done=False
#    while done==False:
#        for r in range(1,1000):
#            print("ROUND: {} LETS GO!".format(r))
#            start = r + 3 # Start at 3
#
#            ## Results arrays for comparison
#            correct = []
#            attempt = []
#
#            ## DISPLAY A SEQUENCE OF COLOURS TO PLAYER
#            for x in range(1,start):
#                sq = random.randrange(0,6) # rand num between 0,1,2,3
#                correct.append(sq) # add sequence to array
#                if sq==0:
#                    result = Square()
#                    Blink(round_speed)
#                if sq==1:
#                    result = Cross()
#                    Blink(round_speed)
#                if sq==2:
#                    result = Circle()
#                    Blink(round_speed)
#                if sq==3:
#                    result = Triangle()
#                    Blink(round_speed)
#                if sq==4:
#                    result = LeftLight(round_speed)
#                if sq==5:
#                    result = RightLight(round_speed)
#
#            ## AWAIT PLAYER TO INPUT THEIR SEQUENCE
#            for x in range(1,start):
#                attempt.append(GetUserInput())
#
#            time.sleep(1) ## 1s delay for user experience
#
#            ## ASSERT ON ARRAYS
#            if correct==attempt:
#                WINNER(2, 0.1) # (points|Speed Increase)
#            else:
#                LOSER()
#                done=True
#                break
#        clock.tick(20)

def Level_Three_Game():
	time.sleep(1)
	print("Difficulty not available")

def Level_Four_Game():
	time.sleep(1)
	print("Difficulty not available..")

inGame=True
while inGame==True:
	level_one=False
	level_two=False
	level_three=False
	level_four=False
#
#   	## SET VISUAL LEVEL
#	if level==1:
#		Diff_Bar(br,0,0,0) # Level 1
#	elif level==2:
#		Diff_Bar(br,br,0,0) # Level 2
#	elif level==3:
#		Diff_Bar(br,br,br,0) # Level 3
#	elif level==4:
#		Diff_Bar(br,br,br,br) # Level 4
#
#	level = NavigateDifficulty(level)

	level=level_select.difficulty()


	if leve==1:
		Level_One_Game()
	elif level==2:
		Level_Two_Game()
	elif level==3:
		Level_Three_Game()
	elif level==4:
		Level_Four_Game()

	clock.tick(30)
