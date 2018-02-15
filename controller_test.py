import os
import pygame
import time

class Controller(object):

	os.environ['SDL_VIDEODRIVER']="dummy"
	controller = None

	def init(self):
		pygame.init()
		pygame.joystick.init()
		self.controller = pygame.joystick.Joystick(0)
		self.controller.init()

	def listen(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.JOYBUTTONDOWN:
					return event.button

	def game_two_listen(self,interval_time,bool):
		start_time=time.time()
		check_time=time.time()
		output=None
		button_pressed=False

		while check_time - start_time < interval_time:
			for event in pygame.event.get():
				if event.type == pygame.JOYBUTTONDOWN:
					button_pressed=True

			check_time = time.time()

			if button_pressed==True and bool==True:
				output=True
			elif button_pressed==True and bool==False:
				output=False
			elif button_pressed==False:
				output=None
		return output
