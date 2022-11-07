import lights
import servo
import audio
import RPi.GPIO as GPIO
import time

def startTest():
    servo.up()
    audio.run("BYOB")
    lights.start()
    servo.down()
    print("all done")
    
if __name__ == "__main__":
    startTest()
    