# the funtion of this file is to control the main process system. Esentially actin as a state machine.
import movement
import lights
import audio
import connection
import integration

# system powers up

# this is esentially the idle state.
# input 0 = no button pressed
# input 1 = test for movement
# input 2 = test for lights
# input 3 = test for audio
# input 4 = connect to director
# input 5 = integration test.

x = False
start = True
while (start):

    # simulates pressin gone of the butttons on the User interface

    button_press = int(input("Press a button 1 - 5: "))
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
