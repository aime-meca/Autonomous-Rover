# Make Sure To Run:
#	source RC/bin/activate
# Before Testing Any PS4 Python Code
# UNINSTALL RPi.GPIO BEFORE INSTALLING lgpio
	# sudo apt remove python3-rpi.gpio
	# sudo apt install python3-rpi-lgpio


# 5V: pin 2
# Ground: pin 6
# (pin 12) GPIO 18 - PWM
# (pin 11) GPIO 17 - on/off direction ctrl

# Import lgpio Module
import lgpio
# Import time Library To Use Delays
import time
# Import evdev
from evdev import InputDevice, categorize, ecodes

lgpio.setwarnings(False)

# Variables To Hold Pin and Controller Info

	# Unsure If This Will Still Work
PSCtrl = InputDevice('/dev/input/event7')
	# 12 On The Board, GPIO 18 (PCM CLK)
pwmPin		= 12
	# 11 On The Board, GPIO 17
directionSwitch = 11

# Define That Code Is Referred To By Its Board Number
lgpio.setmode(lgpio.BOARD)

# Set PWM Pin As Output
lgpio.setup(pwmPin, lgpio.OUT)

# Initize PWM With Frequency = 1 kHz
pwm = lgpio.PWM(pwmPin, 1000)

# Set Output To 0% Duty Cycle At The Start
pwm.start(0)


#	#	#	#	#


# Duty Cycle Initial Value = 0
dc = 0


# Outputs On Button Press
for event in PSCtrl.read_loop():
	# R1 Go Faster?
	if event.code == 311:
		print('Speed')
		if (dc < 20):
			dc = dc + 1
		pwm.ChangeDutyCycle(dc)

	# R2 Go Slower
	if event.code == 310:
		print('Slow')
		if (dc > 0):
			dc = dc - 1
		pwm.ChangeDutyCycle(dc)

	# X Is Stop
	if event.code == 304:
		print('Stop')
		dc = 0
		pwm.ChangeDutyCycle(dc)
		pwm.stop
		pwm.cleanup()