import sys
import socket
import selectors
import traceback
import multiprocessing
import time
import keyboard 

from Protocol import libserver
from Protocol import libclient

from Utils.robotUtils import create_request, listen_for_director, start_connection, initiate_connection

ROBOT_NAME = "Robot2"
HOST = "127.0.0.1"
PORT = 2432 # 65432

LISTEN_PORT = 2432 #4456

if __name__ == "__main__":
  print('Register with director...')

  registration_request = create_request(ROBOT_NAME, "Register", LISTEN_PORT) 
  initiate_connection(HOST, PORT, registration_request, libclient)

  print('Finished registration, booting up server to listen...')

  while True:
    msg = listen_for_director(HOST, LISTEN_PORT, libserver)

    print(msg)
    if msg['value'] == 'break':
      break

    print('Main Loop recieved ', msg, ' so will start to do corresponding task')
    
    
    # READ THE MESSAGE AND DO WHATEVER YOUR ROBOT WILL DO.
    
    servo.up()
    audio.run(str(msg))
    lights.start()
    servo.down()
