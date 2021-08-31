import RPi.GPIO as GPIO
import time
import picamera
from time import sleep
import autoCap as au
#from PIL import ImageGrab
#from StringIO import StringIO
TRIG=21
ECHO=20
GPIO.setmode(GPIO.BCM)
def func():
        while True:
            camera = picamera.PiCamera()
            print("distance measurement in progress")
            GPIO.setup(TRIG,GPIO.OUT)
            GPIO.setup(ECHO,GPIO.IN)
            GPIO.output(TRIG,False)
            print("waiting for sensor to settle")
            time.sleep(0.2)
            GPIO.output(TRIG,True)
            time.sleep(0.00001)
            GPIO.output(TRIG,False)
            while GPIO.input(ECHO)==0:
                pulse_start=time.time()
            while GPIO.input(ECHO)==1:
                pulse_end=time.time()
            pulse_duration=pulse_end-pulse_start
            distance=pulse_duration*17150
            distance=round(distance,2)
            
            print(distance)
            time.sleep(2)  

            if(distance>50 and distance < 150):
                
             au.Capture()
                

func()

