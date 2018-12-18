#from UDPChannels import udp
from NeoDisplay import NeoDisplay
import time

#
#   If the user sets the terminal window to 64 wide and 8 pixels
#   high the display will fill the window.   Set the font to fixed
#   width font for it to work nicely.
#
#   For starters, just run this in one terminal, and the packet producer
#   in another.
#
REMOTE_IP = 'localhost'
REMOTE_PORT = 8776
LOCAL_IP = 'localhost'
LOCAL_IP = 8777

# some terminal helpers.
def clear_screen():
    print(chr(27)+'[2J', end='')
 
def cursor_home():
    print(chr(27)+'[H', end='')


# create the udp listener/receiver to read udp packets
# from port 8777

clear_screen()
display = NeoDisplay(256)

# create the display, initialized to ' '
# just an array of characters seems fine as an implementation
# but it should probably be a class

# Loop forever
while 1:

    # read the incoming udp packet
    received = True 
    if received:

	# parse the packet with json parser
	# someone figure this one out?

	# extract the values from the resulting dictionary

        
	# if there is a "clear" directive, clear the display 
        clear_directive = True
        if clear_directive:
            display.clear()

        # if there are pixel values:
	# use those values to insert '*' or ' ' in display array

        cursor_home()
        print(display.render())

    #
    # wait for a second before trying to read again
    # should fix this after a bit
    #
    time.sleep(1)
