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
	


	print(categorize(event))
