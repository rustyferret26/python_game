import user_select
import game_one
import time

# Get level choice from user
print("Please select a game")
game = user_select.game()

if game==1:
	print("Game one selected, please select the difficulty..")
	difficulty=user_select.difficulty()
	print("Difficulty level {}, starting game..".format(difficulty))
	if difficulty==1:
		game_one.diff_one()
	elif difficulty==2:
		game_one.diff_two()
	elif difficulty==3:
		game_one.diff_three()
	elif difficulty==4:
		game_one.diff_four()
elif game==2:
	print("starting game_two()")
#	game_two()
elif game==3:
	print("starting game_three()")
#	game_three()
elif game==4:
	print("starting game_four()")
#	game_four()
