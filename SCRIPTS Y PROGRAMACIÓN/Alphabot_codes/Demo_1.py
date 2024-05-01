#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
from AlphaBot2_Lib import AlphaBot2
from rpi_ws281x import Adafruit_NeoPixel, Color
from AlphaBot2_Lib import TRSensor
import time

Button = 7
DR = 16
DL = 19
IR = 17
PWM = 50
n=0
TRIG = 22
ECHO = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Button,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(DR,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(DL,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(IR,GPIO.IN)
GPIO.setup(TRIG,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ECHO,GPIO.IN)



# LED strip configuration:
LED_COUNT      = 4      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)	

maximum = 20;
j = 0
integral = 0;
last_proportional = 0


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
    
def Ruleta(pos):
#	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)
        
def getkey():
	if GPIO.input(IR) == 0:
		count = 0
		while GPIO.input(IR) == 0 and count < 200:  #9ms
			count += 1
			time.sleep(0.00006)
		if(count < 10):
			return;
		count = 0
		while GPIO.input(IR) == 1 and count < 80:  #4.5ms
			count += 1
			time.sleep(0.00006)

		idx = 0
		cnt = 0
		data = [0,0,0,0]
		for i in range(0,32):
			count = 0
			while GPIO.input(IR) == 0 and count < 15:    #0.56ms
				count += 1
				time.sleep(0.00006)
				
			count = 0
			while GPIO.input(IR) == 1 and count < 40:   #0: 0.56mx
				count += 1                               #1: 1.69ms
				time.sleep(0.00006)
				
			if count > 7:
				data[idx] |= 1<<cnt
			if cnt == 7:
				cnt = 0
				idx += 1
			else:
				cnt += 1
#		print data
		if data[0]+data[1] == 0xFF and data[2]+data[3] == 0xFF:  #check
			return data[2]
		else:
			print("repetir comando")
			return "repeatir comando"
        


# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
# Intialize the library (must be called once before other functions).
strip.begin()
strip.setPixelColor(0, Color(100, 0, 0))       #Red
strip.setPixelColor(1, Color(0, 100, 0))       #Blue
strip.setPixelColor(2, Color(0, 0, 100))       #Green
strip.setPixelColor(3, Color(100, 100, 0))     #Yellow
strip.show()


time.sleep(1)
strip.setPixelColor(0, Color(0, 0, 0))       # Se Apaga
strip.setPixelColor(1, Color(0, 0, 0))       # Se Apaga
strip.setPixelColor(2, Color(0, 0, 0))       # Se Apaga
strip.setPixelColor(3, Color(0, 0, 0))       # Se Apaga
strip.show()
time.sleep(1)


contador_LEDS = 0
j = 0

while(contador_LEDS <64*4):
    for i in range(0,strip.numPixels()):
        strip.setPixelColor(i, Ruleta(((i * 256 // strip.numPixels()) + j) & 255))
        strip.show();
        j += 1
    if(j > 256*4):
        j= 0
    time.sleep(0.005)
    contador_LEDS = contador_LEDS + 1
    
time.sleep(0.5)    
strip.setPixelColor(0, Color(0, 0, 0))       # Se Apaga
strip.setPixelColor(1, Color(0, 0, 0))       # Se Apaga
strip.setPixelColor(2, Color(0, 0, 0))       # Se Apaga
strip.setPixelColor(3, Color(0, 0, 0))       # Se Apaga
strip.show()

time.sleep(0.5)
strip.setPixelColor(0, Color(255, 0, 0))       #Rojo
strip.setPixelColor(1, Color(255, 0, 0))       #Rojo
strip.setPixelColor(2, Color(255, 0, 0))       #Rojo
strip.setPixelColor(3, Color(255, 0, 0))       #Rojo
strip.show()

time.sleep(0.5)
strip.setPixelColor(0, Color(0, 255, 0))       #Verde
strip.setPixelColor(1, Color(0, 255, 0))       #Verde
strip.setPixelColor(2, Color(0, 255, 0))       #Verde
strip.setPixelColor(3, Color(0, 255, 0))       #Verde
strip.show()

time.sleep(0.5)
strip.setPixelColor(0, Color(0, 0, 255))       #Azul
strip.setPixelColor(1, Color(0, 0, 255))       #Azul
strip.setPixelColor(2, Color(0, 0, 255))       #Azul
strip.setPixelColor(3, Color(0, 0, 255))       #Azul
strip.show()

time.sleep(0.5)
strip.setPixelColor(0, Color(255, 255, 0))     #Amarillo
strip.setPixelColor(1, Color(255, 255, 0))     #Amarillo
strip.setPixelColor(2, Color(255, 255, 0))     #Amarillo
strip.setPixelColor(3, Color(255, 255, 0))     #Amarillo
strip.show()

time.sleep(0.5)    
strip.setPixelColor(0, Color(0, 0, 0))       # Se Apaga
strip.setPixelColor(1, Color(0, 0, 0))       # Se Apaga
strip.setPixelColor(2, Color(0, 0, 0))       # Se Apaga
strip.setPixelColor(3, Color(0, 0, 0))       # Se Apaga
strip.show()
time.sleep(0.5) 
strip.setPixelColor(0, Color(128, 128, 128))       # Se Apaga
strip.setPixelColor(1, Color(128, 128, 128))       # Se Apaga
strip.setPixelColor(2, Color(128, 128, 128))       # Se Apaga
strip.setPixelColor(3, Color(128, 128, 128))       # Se Apaga
strip.show()


TR = TRSensor()
Ab = AlphaBot2()
Ab.stop()
time.sleep(0.5)

limit = 50
pwm = 15
for i in range(0,limit):
	if(i<0.33*limit or i>= limit*0.66):
		Ab.right()
		Ab.setPWMA(pwm)
		Ab.setPWMB(pwm)
	else:
		Ab.left()
		Ab.setPWMA(pwm)
		Ab.setPWMB(pwm)
	TR.calibrate()
Ab.stop()

print("Sensores Calibrados niveles máximos",TR.calibratedMin)
print("Sensores Calibrados niveles minimos",TR.calibratedMax)
Ab.forward()
seguidor_linea_IR = 0
seguidor_linea_NIR = 0

while True:
    key = getkey()
    if key == 0x18:
        print("Modo Seguidor de Línea con IR obstáculos ")
        seguidor_linea_IR = 1
        seguidor_linea_NIR = 0
        seguidor_linea_US  = 0
    if key == 0x1c:
        print("Modo Seguidor de Línea sin IR obstáculos ")
        seguidor_linea_IR = 0
        seguidor_linea_NIR = 1
        seguidor_linea_US  = 0    
    
    
    if (seguidor_linea_IR):
        DR_status = GPIO.input(DR)
        DL_status = GPIO.input(DL)
        position,Sensors = TR.readLine()
        if ((DL_status != 0) and (DR_status != 0)):
            if(Sensors[0] >900 and Sensors[1] >900 and Sensors[2] >900 and Sensors[3] >900 and Sensors[4] >900):
                Ab.setPWMA(0)
                Ab.setPWMB(0);
                # Caso en el que tenemos el robot al aire.
            else:       
                proportional = position - 2000
                derivative = proportional - last_proportional
                integral += proportional
                last_proportional = proportional
                power_difference = proportional/30 + integral/80000 + derivative*20;

                if (power_difference > maximum):
                    power_difference = maximum
                if (power_difference < - maximum):
                    power_difference = - maximum
                #print(position,power_difference)
                if (power_difference < 0):
                    Ab.setPWMA(maximum + power_difference)
                    Ab.setPWMB(maximum);
                else:
                    Ab.setPWMA(maximum);
                    Ab.setPWMB(maximum - power_difference)             
        else:
            Ab.setPWMA(0)
            Ab.setPWMB(0)
    if (seguidor_linea_NIR):
        position,Sensors = TR.readLine()      
        if(Sensors[0] >900 and Sensors[1] >900 and Sensors[2] >900 and Sensors[3] >900 and Sensors[4] >900):
            Ab.setPWMA(0)
            Ab.setPWMB(0);
            # Caso en el que tenemos el robot al aire.
        else:       
            proportional = position - 2000
            derivative = proportional - last_proportional
            integral += proportional
            last_proportional = proportional
            power_difference = proportional/30 + integral/80000 + derivative*20;

            if (power_difference > maximum):
                power_difference = maximum
            if (power_difference < - maximum):
                power_difference = - maximum
            #print(position,power_difference)
            if (power_difference < 0):
                Ab.setPWMA(maximum + power_difference)
                Ab.setPWMB(maximum);
            else:
                Ab.setPWMA(maximum);
                Ab.setPWMB(maximum - power_difference)
                