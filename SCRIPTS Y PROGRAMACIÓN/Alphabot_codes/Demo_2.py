import RPi.GPIO as GPIO
import time
from rpi_ws281x import Adafruit_NeoPixel, Color
TRIG = 22
ECHO = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ECHO,GPIO.IN)

# LED strip configuration:
LED_COUNT      = 4      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)


def dist():
	#print("Config trig_high")
	GPIO.output(TRIG,GPIO.HIGH)
	time.sleep(0.000015)
	#print("Config Trig_low")
	GPIO.output(TRIG,GPIO.LOW)
	while not GPIO.input(ECHO):
		pass
	#print("Primer Time")
	t1 = time.time()
	while GPIO.input(ECHO):
		pass
	#print("Segundo Time")
	t2 = time.time()
	return (t2-t1)*34000/2

while True:
    distancia = 0.00
    distancia = dist()
    print("Distancia medida: %0.2f cm" % distancia)
    time.sleep(1)
