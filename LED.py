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


