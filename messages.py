import blinkt
import time
import random

def Error():
	n=4 # nth place starts lights from middle
	r=180 # red
	g=0 # green
	b=0 # blue
	br=0.2 # brightness from 0.05 - 1
	t=0.02 # time in seconds between pixel change
	print("Error!")
	for i in range(0,10): # times to strobe
		for i in range((blinkt.NUM_PIXELS)-n):
			px_a=(i+n)
			px_b=7-(i+n)
			blinkt.set_pixel(px_a,r,g,b,br)
			blinkt.set_pixel(px_b,r,g,b,br)
			blinkt.show()
			time.sleep(t)
			blinkt.clear()
			blinkt.show()
def Wait(s):
	done=False
	start=time.time()
	print("Waiting for {}".format(waiting_for))
	while done==False:
		for i in range(blinkt.NUM_PIXELS):
			x=random.randint(0,4)
			b=50+(50*x)
			y = random.randint(1,5)
			br=y/10
			blinkt.set_pixel(i,10,10,b,br)
			blinkt.show()
			end=time.time()
			elapsed=end-start
			if elapsed>s:
				blinkt.clear()
				blinkt.show()
				done=True

def Success():
	for x in range(0,2):
		for i in range(100):
			br=(i-100)
			blinkt.set_all(0,120,0,br)
			blinkt.show()


def game_lights(game_choice):
	game_choice = game_choice -1
	blinkt.clear()
	blinkt.set_pixel(game_choice,200,200,200,0.2)
	blinkt.show()