import RPi.GPIO as GPIO
import time
from AlphaBot2 import AlphaBot2
Ab = AlphaBot2()
try:
	while True:
		decision = str(input("Dirección"))
		if decision == "s":
			Ab.stop();
			print("Freno")
			
		elif decision == "w":
			Ab.forward();
			print("accelerando")
		
		elif decision == "a":
			Ab.right();
			print("right")
			
		elif decision== "d":
			Ab.left();
			print("left")
			
		
	

except KeyboardInterrupt:
	GPIO.cleanup()
