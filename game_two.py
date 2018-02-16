import controller_test
import LED
import os
import requests

class init(object):

	# Set game variables
	speed=None
	points=None
	level=None
	round=None
	lives=None
	round_check=None

	def set_stats(self):
		self.speed=1.7
		self.points=0
		self.level=0
		self.round=0
		self.lives=10
		round_check=True

	def show_game_data(self):
		os.system('clear')
		print("Speed: {}".format(str(round(self.speed,2))))
		print("Lives: {}".format(self.lives))
		print("Round: {}".format(self.round))
		print("Score: {}".format(self.points))

	def wrong_pixel(self):
		LED.msg(200,0,0)
		self.speed=self.speed*0.95
		self.points-=5
		self.lives-=1
		self.show_game_data()

	def right_pixel(self):
		LED.msg(0,200,0)
		self.speed=self.speed*0.95
		self.points+=5
		self.round+=1
		self.round_check=True
		self.show_game_data()

	def print_results(self):
		print(" ")
		print("Oh no, you ran out of lives")
		print("Your total score was: {}".format(self.points * self.round))
		print("This was calculated by your score multiplied by the round you finished on")
		user_choice = input("Would you like to enter your name to save your score? (Type 'yes/no'): ")
		if user_choice=="yes" or user_choice=="Yes":
			name = input("Awesome! So, what is your name?: ")
			self.post_results(name)
			print("Thanks {}! You're score has been posted to http://bondgame.twentysixstaging.com/".format(name))
		else:
			print("Thanks! Goodbye.")

	def post_results(self,name):
		response = requests.post("http://bondgame.twentysixstaging.com/score/save?playerName=" + str(name) + "&score=" + str(self.points))
		print(response)

	def init(self):
		pad=controller_test.Controller()
		pad.init()
		self.set_stats()

		x=True
		while x==True:
			# Show game stats on screen
			self.show_game_data()

			# Set colours - red,green,blue,brightness
			r,g,b,br = (255-self.speed*124),(5),(2*124),(0.2)


			# Ascend through LEDs
			for i in range(7):
				LED.set_by_pixel(i,r,g,b,br)
				if (pad.game_two_listen((self.speed/8),False))==False:
					self.wrong_pixel()
				LED.clear_all()

			# Descend through LEDs starting with correct LED.
			for i in range(7):
				LED.set_by_pixel(8-(i+1),r,g,b,br)
				if i==0:
					if (pad.game_two_listen((self.speed/8),True))==True:
						self.right_pixel()
				else:
					if (pad.game_two_listen(self.speed/8,False))==False:
						self.wrong_pixel()
				LED.clear_all()

			# Every 5 rounds, add another life.
			if self.round%5==0 and not self.round == 0 and self.round_check==True:
				self.lives+=1
				self.round_check=False

			# Quit when lives==0
			if self.lives==0:
				x=False

		self.print_results()


