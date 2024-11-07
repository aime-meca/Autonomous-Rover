#import evdev
from evdev import InputDevice, categorize, ecodes

#creates object 'PSCtrl' to store the data
#you can call it ('PSCtrl'?) whatever you like
PSCtrl = InputDevice('/dev/input/event7')
#need to figure out which event is joystick and replace event3
#with actual event

# event6 = dell keyboard lol
# event7 = one of the constant input ones - axis stuff. also sees button presses


#prints out device info at start
print(PSCtrl)

#evdev takes care of polling the controller in a loop
for event in PSCtrl.read_loop():
	#filters by event type (type of button press)

# only prints if button is pressed
	if(event.value != 0):
		if ((event.value < 120) or (event.value > 130)):
#			print("Button Pressed")
			print(categorize(event))
			print(event)
#			if event.type == ecodes.EV_KEY:
#				print(categorize(event))
#				print("EV_KEY")


# event.code - checks the button's code
# event.value - checks value: 01/00 - pressed or not pressed

#	if event.type == ecodes.ABS_RX:
#		if event.value > 200:
#			print(categorize(event))

