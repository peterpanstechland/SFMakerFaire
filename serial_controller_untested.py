#!/usr/bin/env python3
"""
Scrits to read signals from Arduino and convert into steering and throttle outputs
Arduino input signal range: 0 to 200
Output range: -1.00 to 1.00
"""

import serial
import time

class SerialController:
    def __init__(self):
        print("Starting Serial Controller")

        self.angle = 0.0
        self.throttle = 0.0
        self.mode = 'user'
        self.recording = False
        self.serial = serial.Serial('/dev/ttyS0', 115200, timeout=1) #Serial port - laptop: 'COM3', Arduino: '/dev/ttyACM0'


    def update(self):
        while True:
            line = str(self.serial.readline())[2:-5]
            output = line.split(",")
            if len(output) == 2:
                if output[0].isnumeric() and output[1].isnumeric():
                    channel = int(output[0])
                    if channel == 1:
                        self.throttle = (float(output[1])-1500)/500 #TODO: Update to output -1 to 1 for 1000
                    if channel == 2:
                        self.angle = (float(output[1])-1500)/500 #TODO: Update to output -1 to 1 for 1000to 2000.

                    if self.throttle > 0.01:
                        self.recording = True
                        print("Recording")
                    else:
                        self.recording = False
                    time.sleep(0.01)

    def run(self):
        return self.run_threaded()

    def run_threaded(self):
        #print("Signal:", self.angle, self.throttle)
        return self.angle, self.throttle, self.mode, self.recording
