# This code is largely adapted from: https://github.com/DexterInd/BrickPi/blob/master/Software/BrickPi_Python/

from __future__ import print_function
from __future__ import division
from builtins import input

import time
import utils as utils

# the above lines are meant for Python3 compatibility.
# they force the use of Python3 functionality for print(),
# the integer division and input()
# mind your parentheses!

from BrickPi import *   #import BrickPi.py file to use BrickPi operations

BrickPiSetup()  # setup the serial port for communication

BrickPi.MotorEnable[PORT_A] = 1 #Enable the Motor A
BrickPi.MotorEnable[PORT_B] = 1 #Enable the Motor B

BrickPiSetupSensors() #Send the properties of sensors to BrickPi


#Communication timeout in ms (how long since last valid communication before floating the motors).
#0 disables the timeout so the motor would keep running even if it is not communicating with the RaspberryPi
BrickPi.Timeout=3000
print("BrickPiSetTimeout Status :",BrickPiSetTimeout())



def control_motor_with_keys(port_input, speed=50):

    # get the port using getPort in utils


    # get user input to start motor
start_motor = None
    while(start_motor == 'g' or start_motor == 'G'):
        start_motor = input("please press the key G. Please.")

    # start motor at speed 'speed'
print("big vroom vroom at port", port, "with the speed of")
    BrickPi.MotorSpeed[port] = speed
    stop_motor = None

    # get user input to start motor
while (not (stop_motor == 's' or stop_motor == 'S')):
        stop_motor = input("press the s key to stop the motor please!")
        BrickPiUpdateValues()

    #stop motor
    BrickPi.MotorSpeed[PORT_A] = 0



if __name__ == "__main__":
