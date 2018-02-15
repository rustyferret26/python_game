
import blinkt
import time

def blink_green(s,x):
	r,g,b,br=0,205,0,0.2
	SetLights(r,g,b,br,s,x)

def blink_pink(s,x):
	r,g,b,br=255,20,147,0.2
	SetLights(r,g,b,br,s,x)

def blink_blue(s,x):
	r,g,b,br=0,0,205,0.2
	SetLights(r,g,b,br,s,x)

def blink_red(s,x):
	r,g,b,br=2015,0,0,0.2
	SetLights(r,g,b,br,s,x)

def SetLights(r,g,b,br,s,x):
	for x in range(0,x):
		blinkt.set_all(r,g,b,br)
		blinkt.show()
		time.sleep(s/2)
		blinkt.clear()
		blinkt.show()
		time.sleep(s/2)

def msg(r,g,b):
	n=4
	for i in range(0,6):
		for i in range((blinkt.NUM_PIXELS)-n):
			px_a=(i+n)
			px_b=7-(i+n)
			blinkt.set_pixel(px_a,r,g,b,0.2)
			blinkt.set_pixel(px_b,r,g,b,0.2)
			blinkt.show()
			time.sleep(0.02) # Speed
			blinkt.clear()
			blinkt.show()


def blink_right(s):
	r,g,b,br=200,200,200,0.2
	for i in range(blinkt.NUM_PIXELS):
		blinkt.clear()
		blinkt.set_pixel(i,r,g,b,br)
		blinkt.show()
		time.sleep((s/blinkt.NUM_PIXELS)/2)
	blinkt.clear()
	blinkt.show()
	time.sleep(s/2)

def blink_left(s):
	r,g,b,br=200,200,200,0.2
	for i in range(blinkt.NUM_PIXELS):
		blinkt.clear()
		blinkt.set_pixel(7-i,r,g,b,br)
		blinkt.show()
		time.sleep((s/blinkt.NUM_PIXELS)/2)
	blinkt.clear()
	blinkt.show()
	time.sleep(s/2)

def set_by_pixel(px,r,g,b,br):
	blinkt.set_pixel(px,r,g,b,br)
	blinkt.show()

def clear_all():
	blinkt.clear()
	blinkt.show()
