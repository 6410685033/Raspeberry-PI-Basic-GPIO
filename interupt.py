import signal
import sys
import RPi.GPIO as GPIO
import neopixel
import board

BUTTON_GPIO = 13
pixels = neopixel.NeoPixel(board.D12, 30)
status = False

def signal_handler(sig, frame):
	GPIO.cleanup()
	sys.exit(0)

def button_callback(channel):
	global status
	if not GPIO.input(BUTTON_GPIO):
		print("Button pressed!")
		status = not status
	else:	print("Button released!")
	if status:
		pixels[0] = (255, 0 ,0)
	else:
		pixels[0] = (0, 0, 0)

if __name__ == '__main__':
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	GPIO.add_event_detect(BUTTON_GPIO, GPIO.BOTH,
			callback=button_callback, bouncetime=200)
	
	signal.signal(signal.SIGINT, signal_handler)
	signal.pause()

