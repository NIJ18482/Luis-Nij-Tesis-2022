import RPi.GPIO as GPIO
import numpy
import time
from AlphaBot2 import AlphaBot2

Ab = AlphaBot2()

print("Hello")
print("Moviendo el Alphabot 1s")
Ab.forward()
time.sleep(2)
Ab.stop()
