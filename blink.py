import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.IN)

while True:
	if (GPIO.input(12)):
		GPIO.output(11, GPIO.HIGH)
	else:
		(GPIO.output(11,GPIO.HIGH))
		time.sleep(0.5)
		(GPIO.output(11,GPIO.LOW))
		time.sleep(0.5)