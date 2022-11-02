# the funtion of this file is to control the main process system. Esentially actin as a state machine.
import movement
import lights
import audio
import connection
import integration
from gpiozero import Button, AngularServo
from signal import pause

# system powers up

# this is esentially the idle state.
# input 0 = no button pressed
button_press = 0
# input 1 = test for movement
MoveBtn = Button(5)
# input 2 = test for lights
LightsBtn = Button(22)
# input 3 = test for audio
AudioBtn = Button(27)
# input 4 = connect to director
DirectorBtn = Button(17)
# input 5 = integration test.
IntegrateBtn = Button(6)

x = False
start = True
while (start):

    # simulates pressin gone of the butttons on the User interface

    #    button_press = int(input("Press a button 0 - 5: "))
    # button presses form UI
    MoveBtn.when_pressed = button_press = 1
    LightsBtn.when_pressed = button_press = 2
    AudioBtn.when_pressed = button_press = 3
    DirectorBtn.when_pressed = button_press = 4
    IntegrateBtn.when_pressed = button_press = 5

    if (button_press == 4):
        connection.connected = True
    # if system connection it should run the fully integrated process, and then return to the idle state.
    if (connection.connected == True and x == False):
        ctest = False
        integration.start(ctest)

    if (button_press == 1):
        movement.start()
    elif (button_press == 2):
        lights.start()
    elif (button_press == 3):
        audio_test = True
        audio.start(audio_test)
    elif (button_press == 5):
        test_test = True
        integration.start(test_test)
