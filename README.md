# Drive with RC Controller
## ROBOHAT MM1 SETUP
### SOFTWARE
- **STEP 1**: Plug-in the board with microUSB cable.
- **STEP 2**: Flash the Circuit Python firmware onto board, if circuit python firmware is not on the board.
- **STEP 3**: Copy the [code_RC_Control.py](https://raw.githubusercontent.com/peterpanstechland/SFMakerFaire/master/code_RC_Control.py) file into CIRCUITPY USB drive
- **STEP 4**: Rename the code_RC_Control.py to code.py
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
- **STEP 1**: plug in the 5V, GND, CH1 from RC Receiver to RCH1 pin on HAT
- **STEP 2**: plug in the 5V, GND, CH2 from RC Receiver to RCH2 pin on HAT
- **STEP 2**: plug in Steering Servo to SERVO1 on hat
- **STEP 3**: plug in ESC Throttle to SERVO2 on hat
!{RC Channel connection | small}(/images/IMG_20190520_002159.jpg)
![Steering & Throttle connection | small](/images/IMG_20190520_002319.jpg)

##### Power
- **STEP 1**: plug in Car Battery to Main power port
- **STEP 2**: plug in ESC to ESC passthrough port
- **STEP 3**: plug in LIPO Back up battery
![Power connection | small](/images/IMG_20190520_002357.jpg)
![Power connection 2 | small](/images/IMG_20190520_002400.jpg)
![Power and backup battery connection | small](/images/IMG_20190520_002418.jpg)

---
### Raspberry PI Setup
*Burn image to SD card and setup network, follow the donkey car setup [link](http://docs.donkeycar.com/guide/install_software/#get-the-raspberry-pi-working)*
- **STEP 1**: Press Power button on RoboHAT MM1 to turn power for hat and pi
- **STEP 2**: login to pi through ssh or using monitor pluged in with HDMI cable
- **STEP 3**: Copy the [serial_controller.py](https://raw.githubusercontent.com/peterpanstechland/SFMakerFaire/master/serial_controller.py) to the python3 donkeycar/parts/ library ~/xx/xx/lib/python3.x/site-packages/donkeycar/parts/
- **STEP 4**: Copy the [actuator.py](https://raw.githubusercontent.com/peterpanstechland/SFMakerFaire/master/actuator.py) to the python3 donkeycar/parts/ library ~/xx/xx/lib/python3.x/site-packages/donkeycar/parts/
- **STEP 5**:
```bash
$ donkey createcar ~/mycar
```
- **STEP 6**: copy the [manage.py](https://raw.githubusercontent.com/peterpanstechland/SFMakerFaire/master/manage.py) to ~/mycar
- **STEP 7**: copy the [config.py](https://raw.githubusercontent.com/peterpanstechland/SFMakerFaire/master/config.py) to ~/mycar
- **STEP 8**: start driving
```bash
$ cd ~/mycar
$ python manage.py drive --js
```
#### AI Training and Driving
*Follow the donkey car training [link](http://docs.donkeycar.com/guide/train_autopilot/)*
- **STEP 1**: Transfer dtat from car to your computer, on your computer terminal type:
```bash
$ rsync -r pi@<your_pi_ip_address>:~/mycar/tub/  ~/mycar/tub/
```
- **STEP 2**: Train a model:
```bash
$ python ~/mycar/manage.py train --tub <tub folder names comma separated> --model ./models/mypilot
```
- **STEP 3**: move trained pilot back to car
```bash
$ rsync -r ~/mycar/models/ pi@<your_ip_address>:~/mycar/models/
```
- **STEP 4**: Use the trained pilot to drive the car
```bash
$ python manage.py drive --model models/mypilot
```
