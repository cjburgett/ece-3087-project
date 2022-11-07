import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

servoPIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWM with 50Hz
p.start(2.5)  # Initialization
p.ChangeDutyCycle(0)


def up():
#     p.start(2.5)
    p.ChangeDutyCycle(2)
    print("ok cool")
    time.sleep(.7)
    p.ChangeDutyCycle(2)
    time.sleep(.7)
    
    p.ChangeDutyCycle(0)
    time.sleep(2)

    

def down():
    p.ChangeDutyCycle(11)
    print("ok cool")
    time.sleep(.7)
    p.ChangeDutyCycle(10)
    time.sleep(.4)
    
    p.ChangeDutyCycle(0)
    time.sleep(2)
    

