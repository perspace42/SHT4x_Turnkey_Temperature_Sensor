'''
Author: Scott Field
Version: 2.0
Date: 05/13/2024
Purpose:
Interact with the running Adafruit SHT4x Trinkey board, displaying its output if found
'''

import tkinter as tk            #For GUI
import serial.tools.list_ports  #To connect to port

# Function to update the labels with serial data
def update_labels():
    #Counter For Data
    max_no_data_iterations = 10
    try:
        # Read from serial port
        data = connection.readline().decode().strip()
        lines = data.split('\t')
        temperature = lines[0]
        humidity = lines[1]
    except Exception as e:
        print(f"Error reading from serial port: {e}")
        exit()

    # Update the labels (if data was received)
    if data:
        label1.config(text=temperature)
        label2.config(text=humidity)
        max_no_data_iterations = 10  # Reset the counter if data is received
    else:
        max_no_data_iterations -= 1

    
    # Schedule the next update
    if max_no_data_iterations > 0:
        root.after(50, update_labels)
    else:
        print("Program terminated due to no data received.")
        root.quit()

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
        print(f"Something Went Wrong Attempting To Connect to ({com_number})") 
        exit()

else:
    print(f"Serial Port (COM{com_number}) not found")
    exit()
    
# Create the main window
root = tk.Tk()
root.title("Serial Data")

# Create two labels to display the data
label1 = tk.Label(root, text="", font=("Arial", 14))
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = tk.Label(root, text="", font=("Arial", 14))
label2.grid(row=1, column=0, padx=10, pady=10)

#Main Loop

# Start the update loop
update_labels()

# Run the main event loop
root.mainloop()
