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
	for i in range(0,6): # times to strobe
		for i in range((blinkt.NUM_PIXELS)-n):
			px_a=(i+n)
			px_b=7-(i+n)
			blinkt.set_pixel(px_a,r,g,b,br)
			blinkt.set_pixel(px_b,r,g,b,br)
			blinkt.show()
			time.sleep(t)
			blinkt.clear()
			blinkt.show()
	return
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
	n = game_choice
	blinkt.clear()
	blinkt.set_pixel((n+(n-1)-1),200,200,200,0.2)
	blinkt.set_pixel((n*2)-1,200,200,200,0.2)
	blinkt.show()

def diff_lights(diff_choice):
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
	blinkt.set_pixel(3,210,230,0,br_2)
	blinkt.set_pixel(4,255,205,0,br_3)
	blinkt.set_pixel(5,255,140,0,br_3)
	blinkt.set_pixel(6,255,50,0,br_4)
	blinkt.set_pixel(7,255,0,0,br_4)
	blinkt.show()
