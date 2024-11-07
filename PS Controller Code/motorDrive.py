# Make Sure To Run:
#	source RC/bin/activate
# Before Testing Any PS4 Python Code


# 5V: pin 2
# Ground: pin 6
# (pin 12) GPIO 18 - PWM
# (pin 11) GPIO 17 - on/off direction ctrl

# Import RPi.GPIO Module
import RPi.GPIO as GPIO
# Import time Library To Use Delays
import time
# Import evdev
from evdev import InputDevice, categorize, ecodes


GPIO.setwarnings(False)
# Initialize Pins And Controller
PSCtrl = InputDevice('/dev/input/event7')
	# 12 On The Board, GPIO 18 (PCM CLK)
pwmPin		= 12
	# 11 On The Board, GPIO 17
directionSwitch = 11


# Define If Code Will Refer To Pins By Board Or By BCM
	# Here, We Will Refer To Them By Board
GPIO.setmode(GPIO.BOARD)

# Set PWM Pin (12, GPIO 18) As Output
GPIO.setup(12, GPIO.OUT)

# Initize PWM With Frequency = 1 kHz
pwm = GPIO.PWM(pwmPin, 1000)
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



# To Turn Off, Use pwn.stop
# To Change DutyCycle, Use pwm.ChangeDutyCycle( new value )

# End With GPIO.cleanup()

# while running
	# while stop button is not pressed
# if [this] pressed, stop all? and do this
# if [that] pressed, stop all? and do that

# R2 move right motor
# L2 move left motor
# shape button switch direction (neg/pos 5 V)
# d pad (4 cross buttons) inc decr speed


# using abs values (joysticks, L3, R3)
# for slower/faster?
# do this after we have a basic one-speed go

# increment Driver Cycle (?) by 1% or .1% with (d pad)
