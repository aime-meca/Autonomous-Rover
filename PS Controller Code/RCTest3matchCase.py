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
	# shows only button presses (not constant input)
	if event.type == ecodes.EV_KEY:
		#match structure to ID buttons
		match event.code:
			case 304:
				print("X")
			case 305:
				print("Circle")
			case 307:
				print("Triangle")
			case 308:
				print("Square")
			case 311:
				print("R1")
			case 313:
				print("R2")
			case 310:
				print("L1")
			case 312:
				print("L2")

			# default case: if a button w/o ID is pressed
			case _:
				print("Other Button Pressed")




# event.code - checks the button's code
# event.value - checks value: 01/00 - pressed or not pressed



	if event.type == ecodes.ABS_RX:
		if event.value > 200:
			print(event)

#	print(categorize(event))
