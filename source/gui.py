import tkinter as tk
import serial
import time



# Function to update the labels with serial data
def update_labels():
    #Counter For Data
    global max_no_data_iterations
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