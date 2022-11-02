from gpiozero import AngularServo
# This code simulates pressing the movement UI botton on the box.
def start():
    servo = AngularServo(17, min_angle=-720, max_angle=720)
    servo.angle = -90
    print("teapot opened")
    print("mouse moved up")
    print("mouse lowered")
    print("teapot closed")
