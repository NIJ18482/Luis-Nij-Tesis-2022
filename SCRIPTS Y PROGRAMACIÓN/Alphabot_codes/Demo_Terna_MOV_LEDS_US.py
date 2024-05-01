#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
import RPi.GPIO as GPIO
from rpi_ws281x import Adafruit_NeoPixel, Color
from AlphaBot2 import AlphaBot2

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# Demostración de Movimiento
print("Demostración de Movimiento")

Ab = AlphaBot2()
Ab.stop()
time.sleep(0.5)
for i in range(0,100):
	if(i<25 or i>= 75):
		Ab.right()
		Ab.setPWMA(30)
		Ab.setPWMB(30)
	else:
		Ab.left()
		Ab.setPWMA(30)
		Ab.setPWMB(30)
	#TR.calibrate()
Ab.stop()
#print(TR.calibratedMin)
#print(TR.calibratedMax)



print("Demo Finalizada")


