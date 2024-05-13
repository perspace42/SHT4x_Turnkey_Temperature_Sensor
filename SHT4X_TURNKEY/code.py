'''
Author: Adafruit
Version: 1.0
Date: 05/11/2024
Purpose:
Get both the Temperature and Relative Humidity from the SHT4x_Trinkey Sensor
(Necessary libraries are in the lib folder)
'''

import time
import board
import adafruit_sht4x

convertToF = lambda celsius: (celsius * 9/5) + 32

i2c = board.I2C()  # uses board.SCL and board.SDA
sht = adafruit_sht4x.SHT4x(i2c)
print("Found SHT4x with serial number", hex(sht.serial_number))

sht.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION
print("Current mode is: ", adafruit_sht4x.Mode.string[sht.mode])
print()

while True:
    temperature, relative_humidity = sht.measurements
    print(f"Temperature: {convertToF(temperature):0.1f} F\tHumidity: {relative_humidity:0.1f} %")
    time.sleep(1)
