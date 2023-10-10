import board
import neopixel
from gpiozero import Button, MotionSensor

class Joystick:
	pin_left = None
	pin_right = None
	pin_top = None
	pin_down = None
	pin_center = None
	x_value = None
	y_value = None
	center_value = None
	def __init__(self, pin_left, pin_right, pin_top, pin_down, pin_center):
		self.pin_left = pin_left
		self.pin_right = pin_right
		self.pin_top = pin_top
		self.pin_down = pin_down
		self.pin_center = pin_center
		self.x_value = 0
		self.y_value = 0
		self.center_value = 0
	def update(self, len):
		if Button(self.pin_center).is_pressed:
			if self.center_value < 255:
				self.center_value += len
		else:
			if self.center_value > 0:
				self.center_value -= len
		if Button(self.pin_left).is_pressed:
			if self.x_value > 0:
				self.x_value -= len
		if Button(self.pin_right).is_pressed:
			if self.x_value < 255:
				self.x_value += len
		if Button(self.pin_top).is_pressed:
			if self.y_value < 255:
				self.y_value += len
		if Button(self.pin_down).is_pressed:
			if self.y_value > 0:
				self.y_value -= len
	def get_x(self):
		return self.x_value

	def get_y(self):
		return self.y_value

	def get_center(self):
		return self.center_value

pixels = neopixel.NeoPixel(board.D12, 30)
button_left = 17
button_right = 18
button_top = 6
button_down = 23
button_center = 22

joystick = Joystick(button_left, button_right, button_top, button_down, button_center)

while True:
	joystick.update(10)
	x_value = joystick.get_x()
	y_value = joystick.get_y()
	center_value = joystick.get_center()

	print(f"X: {x_value}, Y: {y_value}, btn: {center_value}")
#	if joystick.is_button_pressed():
#		pixels[0] = (x_value, y_value, 0)
#	else:
#		pixels[0] = (0, 0, 0) 

	pixels[0] = (x_value, y_value, center_value)
