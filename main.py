# the funtion of this file is to control the main process system. Esentially actin as a state machine.
import movement
import lights
import audio
import connection
import integration
import RPi.GPIO as GPIO
from signal import pause

# system powers up

# this is esentially the idle state.
# input 0 = no button pressed
GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# input 1 = test for movement
GPIO.setup(5, GPIO.IN)
MoveBtn = GPIO.input(5)
# input 2 = test for lights
GPIO.setup(22, GPIO.IN)
LightsBtn = GPIO.input(22)
# input 3 = test for audio
GPIO.setup(27, GPIO.IN)
AudioBtn = GPIO.input(27)
# input 4 = connect to director
GPIO.setup(17, GPIO.IN)
DirectorBtn = GPIO.input(17)
# input 5 = integration test.
GPIO.setup(6, GPIO.IN)
IntegrateBtn = GPIO.input(6)

x = False
start = True
while (start):

    # simulates pressin gone of the butttons on the User interface

    #    button_press = int(input("Press a button 0 - 5: "))

    if (DirectorBtn):
        connection.connected = True
    # if system connection it should run the fully integrated process, and then return to the idle state.
    #if (connection.connected == True and x == False):
     #   ctest = False
      #  integration.start(ctest)

    if  (MoveBtn):
        movement.start()
    elif (LightsBtn):
        lights.start()
    elif (AudioBtn):
        audio.run()
    elif (IntegrateBtn):
        integration.start()

