import blinkt
import time
import random
import LED
import DS4
import messages
#import user_select
import controller_test

pad=controller_test.Controller()
pad.init()

## Level booleans
start=False

## Brightness
br = 0.05

## GAME STATS
round_speed = 1
player_score = 0
level=1

def diff_one():
	points = 0
	bot_array = []
	round_speed=0.7
	for x in range(0,2):
		item = random.randrange(0,4) # rand num between 0,1,2,3
		bot_array.append(item) # add sequence to array

	for r in range(1,1000):
		user_array = []
		time.sleep(1)

		## DISPLAY SEQUENCE TO USER
		for x in range(0,len(bot_array)):
			if bot_array[x]==DS4.Square():
				LED.blink_pink(round_speed,1)
			if bot_array[x]==DS4.Cross():
				LED.blink_blue(round_speed,1)
			if bot_array[x]==DS4.Triangle():
				LED.blink_green(round_speed,1)
			if bot_array[x]==DS4.Circle():
				LED.blink_red(round_speed,1)

      		## AWAIT PLAYER TO INPUT THEIR SEQUENCE
		for x in range(0,len(bot_array)):
			user_choice = pad.listen()
			user_array.append(user_choice)

		time.sleep(1) ## 1s delay for user experience

     		## ASSERT ON ARRAYS
		if bot_array==user_array:
			print("Wahoo, you got that right!")
			LED.msg(0,200,0)
			item=random.randrange(0,4)
			bot_array.append(item)
			points += 1
			round_speed -= 0.05
		else:
			print("Oh no, that wasn't quite right.. too bad!")
			LED.msg(200,0,0)
			done=True
			print("points: {}".format(points))
			break
