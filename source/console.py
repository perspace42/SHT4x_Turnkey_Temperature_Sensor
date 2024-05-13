'''
Author: Scott Field
Version: 1.0
Date: 05/11/2024
Purpose:
Interact with the running Adafruit SHT4x Trinkey board, displaying its output if found
'''

import serial #To read data from the board
import time #To wait

# Connect to the serial port
connection = serial.Serial('COM7', 115200)

# Check if the serial port is open
if connection.is_open:
    print("Serial Port Connection Established")
else:
    print("Serial Port Connection Failed")
    exit()  # Exit the program if connection fails

# Set a maximum number of iterations with no data before terminating
max_no_data_iterations = 10

# Main Program Loop
while max_no_data_iterations > 0:
    try:
        # Read from serial port
        line = connection.readline().decode().strip()
    except Exception as e:
        print(f"Error reading from serial port: {e}")
        exit()

    # Check if serial port line is empty
    if line:
        print(line)

        max_no_data_iterations = 10  # Reset the counter if data is received
    else:
        max_no_data_iterations -= 1  # Decrement the counter if no data is received

    # Wait to prevent high CPU usage
    time.sleep(0.05)

# Print a message before exiting
print("Program terminated due to no data received.")