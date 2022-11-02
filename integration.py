import movement
import lights
import audio
import connection
import integration
from gpiozero import Button, AngularServo
from signal import pause


def start(test):
    servo = AngularServo(17, min_angle=-720, max_angle=720)
    servo.angle = -90
    print("teapot opens up")
    print("mouse moved")
    print("lights flash")
    if (test):
        print("load preset audio")
        print("play audio")
    else:
        print("interpret CSV from director")
        print("play audio")
    print("mouse lowered")
    print("teapot closed")
