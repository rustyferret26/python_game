import pygame
import blinkt
import time
import random
import select
import user
import LED
import DS4
import messages
import user_select

pygame.init()
clock=pygame.time.Clock()

## Level booleans
start=False

## Brightness
br = 0.05

## GAME STATS
round_speed = 1
player_score = 0
level=1

#Difficulty 1 - 	Using only 4 varients, pi will start by showing you three numbers that
## 			you have to then repeat back to it. Each time the number will increment
##			by one and the game will speed up.

def diff_one():
	done=False
	while done==False:
		for r in range(1,1000):

			## Starting game with a sequence of 3
			start = r + 3

            		## Creating empty arrays to hold correct sequence and attempted sequence
			correct = []
			attempt = []

			## Wait 1 second for user experience
			time.sleep(1)

            		## DISPLAY A SEQUENCE OF COLOURS TO PLAYER
			for x in range(1,start):
				item = random.randrange(0,4) # rand num between 0,1,2,3
				correct.append(item) # add sequence to array
				if item==DS4.Square():
					LED.blink_pink(round_speed,1)
				if item==DS4.Circle():
					LED.blink_red(round_speed,1)
				if item==DS4.Cross():
					LED.blink_blue(round_speed,1)
				if item==DS4.Triangle():
					LED.blink_green(round_speed,1)

            		## AWAIT PLAYER TO INPUT THEIR SEQUENCE
			for x in range(1,start):
				attempt.append(user_select.get_btn())

			time.sleep(1) ## 1s delay for user experience

            		## ASSERT ON ARRAYS
			if correct==attempt:
				print("Wahoo, you got that right!")
				messages.Success()
			else:
				print("Oh no, that wasn't quite right.. too bad!")
				messages.Error()
				done=True
				break
		clock.tick(30)

def diff_two():
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

def diff_three():
	time.sleep(1)
	print("Difficulty not available")

def diff_four():
	time.sleep(1)
	print("Difficulty not available..")
