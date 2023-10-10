import board
import neopixel
from gpiozero import Button

# set up
pixel = neopixel.NeoPixel(board.D12, 1)
button = Button(13)

# run
while True:
	if button.is_pressed:
		pixel[0] = (30, 0, 20)
	else:
		pixel[0] = (0,0,0)
