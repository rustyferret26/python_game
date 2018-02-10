import select
import game_one
#import game_two
#import game_three
#import game_four
import time

# Get level choice from user
game = select.game()
print("level variable set as {}".format(level))

if game==1:
	print("starting game_one()")
	game_one()
elif game==2:
	print("starting game_two()")
#	game_two()
elif game==3:
	print("starting game_three()")
#	game_three()
elif game==4:
	print("starting game_four()")
#	game_four()
