import pygame
import blinkt
import time
import user_select
import controller_test

br=0.2

def Init(speed):
	pad=controller_test.Controller()
	pad.init()
	x=True
	while x==True:
		global br
		game_brightness = br
		g = speed * 124
		b = 15
		r = 255 - speed * 124
		for i in range(blinkt.NUM_PIXELS-1):
			blinkt.set_pixel(i,r,g,b,game_brightness)
			blinkt.show()
			pad.game_two_listen((speed/blinkt.NUM_PIXELS),False)
			blinkt.clear()
			blinkt.show()
		for i in range(blinkt.NUM_PIXELS-1):
			blinkt.set_pixel(8-(i+1),r,g,b,game_brightness)
			blinkt.show()
			if i==0:
				pad.game_two_listen((speed/blinkt.NUM_PIXELS),True)
			else:
				pad.game_two_listen(speed/blinkt.NUM_PIXELS,False)
			blinkt.clear()
			blinkt.show()
		speed -= 0.05


