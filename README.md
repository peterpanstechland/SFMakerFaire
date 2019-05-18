# SFMakerFaire
## Drive with RC Controller
### SOFTWARE
- STEP 1: Select the Circuit Python firmware loaded board.
- STEP 2: Plug-in the board with microUSB cable
- STEP 3: Copy the code_RC_Control.py file into CIRCUITPY USB drive
- STEP 4: Rename the code_RC_Control.py to code.py
### HARDWARE
#### Item list
- 4 x Dupont Jumper Cables or 2 x 3pin Dupont Jumper (female to female most time)
- backup LIPO battery
- RC Receiver
- RC CAR
    1. ESC
    2. Car Battery
    3. Steering Servo
#### Connection
##### Signal
- STEP 1: plug in the 5V, GND, CH1 from RC Receiver to RCH1 pin on HAT
- STEP 2: plug in the 5V, GND, CH2 from RC Receiver to RCH2 pin on HAT
- STEP 2: plug in Steering Servo to SERVO1 on hat
- STEP 3: plug in ESC Throttle to SERVO2 on hat
##### Power
- STEP 1: plug in Car Battery to Main power port 
- STEP 2: plug in ESC to ESC passthrough por
- STEP 3: plug in LIPO Back up battery
### Operation
- STEP 1: Press Power button to turn power for hat and pi
- STEP 2: login to pi through ssh or using monitor pluged in with HDMI cable
- STEP 3: ...
