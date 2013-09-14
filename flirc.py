import RPi.GPIO as GPIO
import time
import pygame
pygame.init()
screen = pygame.display.set_mode((100, 100))
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# setup Volume UP / DOWN pins with LEDs OFF
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, GPIO.HIGH)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)
# setup Mute to be Off with LED OFF
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.LOW)
MUTED = False
def pulse(pin):
        GPIO.output(pin, GPIO.LOW)
        time.sleep(1)
        GPIO.output(pin, GPIO.HIGH)
#	time.sleep(1)
        return
while(1):
	try:
		# m
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN and event.key <= 256:
				print event.key, chr(event.key)
				if event.key == 117:
					pulse(16)
				elif event.key == 110:
					pulse(18)
				elif (event.key == 50) & MUTED:
					GPIO.output(22, GPIO.LOW)
					MUTED = False
				elif (event.key == 50) & (MUTED == False):
					GPIO.output(22, GPIO.HIGH)
					MUTED = True
				elif event.key == 27:
					raise NameError('Quit')

	except NameError:
		GPIO.cleanup()
		print "    Normal exit"
		exit(0)
 
