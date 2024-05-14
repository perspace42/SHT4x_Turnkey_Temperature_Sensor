'''
Author: Scott Field
Version: 2.0
Date: 05/13/2024
Purpose:
Interact with the running Adafruit SHT4x Trinkey board, displaying its output if found
'''

import serial.tools.list_ports  #To connect to port #To read data from the board
import time #To wait

# Function to find the port of the CircuitPython board
def find_port():
    # Get a list of all connected ports
    portData = serial.tools.list_ports.comports()
    #print ([port.device for port in portData])
    #print ([port.hwid for port in portData])
    
    com_number = None
    for port in portData:
        if 'USB VID:PID=239A:8154' in port.hwid:
            com_number = port.device
            return com_number          
    
    #if the device was not found
    return None

#Attempt Connection if Port Found
com_number = find_port()
#If the port is found
if(com_number):
    #Try connection
    try:
        connection = serial.Serial(f'{com_number}',115200)
        # Check if the serial port is open
        if connection.is_open:
            print(f"Serial Port Connection ({com_number}) Established")
        else:
            print(f"Serial Port Connection ({com_number}) Failed")
            exit()  
    except Exception as e:
        print(f"Something Went Wrong Attempting To Connect to (COM{com_number})") 
        exit()

else:
    print(f"Serial Port ({com_number}) not found")
    exit()


# Main Program Loop
max_no_data_iterations = 10
while max_no_data_iterations > 0:
    try:
        # Read from serial port
        line = connection.readline().decode().strip()
    except Exception as e:
        print(f"Error reading from serial port: {e}")
        exit()

    # Check if serial port line is empty
    if line:
        print(line.strip('\n'), end = "\r")

        max_no_data_iterations = 10  # Reset the counter if data is received
    else:
        max_no_data_iterations -= 1  # Decrement the counter if no data is received

    # Wait to prevent high CPU usage
    time.sleep(0.05)

# Print a message before exiting
print("Program terminated due to no data received.")