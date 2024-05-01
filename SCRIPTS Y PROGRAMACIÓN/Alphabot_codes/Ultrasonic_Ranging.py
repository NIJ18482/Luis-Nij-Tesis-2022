import RPi.GPIO as GPIO
import time

TRIG = 22
ECHO = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ECHO,GPIO.IN)

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
    distancia = dist()
    print("Distancia medida:%0.2f cm" % distancia)
    
    if (distancia < 10.00):
        strip.setPixelColor(0, Color(255, 0, 0))       #Rojo
        strip.setPixelColor(1, Color(255, 0, 0))       #Rojo
        strip.setPixelColor(2, Color(255, 0, 0))       #Rojo
        strip.setPixelColor(3, Color(255, 0, 0))       #Rojo
        strip.show()    
     
    else:
        strip.setPixelColor(0, Color(0, 255, 0))       #Verde
        strip.setPixelColor(1, Color(0, 255, 0))       #Verde
        strip.setPixelColor(2, Color(0, 255, 0))       #Verde
        strip.setPixelColor(3, Color(0, 255, 0))       #Verde
        strip.show()
    
	time.sleep(1/2)


