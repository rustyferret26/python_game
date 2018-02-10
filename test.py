import os

import LED
import user
import game_one

os.environ['SDL_VIDEODRIVER'] = "dummy"

# Test the LED Lights
#LED.blink_green(4,5)
#LED.blink_blue(0.5,2)
#LED.blink_red(2,2)
#LED.blink_pink(0.2,7)

#user.get_btn()

game_one.diff_one()
