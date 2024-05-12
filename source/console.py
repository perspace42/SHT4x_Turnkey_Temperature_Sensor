'''
Author: Scott Field
Version: 1.0
Date: 05/11/2024
Purpose:
Interact with the running Adafruit SHT4x Trinkey board, displaying its output if found
'''

import serial #To read data from the board
import time #To wait

#Connect to the serial port
connection = serial.Serial('COM7',115200)

#Check if the serial port is open
if connection.is_open:
    print("Serial Port Connection Established")
else:
    print("Serial Port Connection Failed")
    

#Main Program Loop
while 1:
    #Read from serial port
    line = connection.readline().decode().strip()

    #Check if serial port line is empty
    if line:
        print(line)
    
    #Wait to prevent high CPU usage
    time.sleep(0.05)