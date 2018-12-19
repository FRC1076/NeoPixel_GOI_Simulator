# copy udp_channels.py to this directory for this to work for now
import udp_channels as udp
from NeoDisplay import NeoDisplay
import time
import json

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
LOCAL_PORT = 8777

# some VT100 terminal helpers.
def clear_screen():
    print(chr(27)+'[2J', end='')
 
def cursor_home():
    print(chr(27)+'[H', end='')


# create the udp listener/receiver to read udp packets
# from port 8777


receiver = udp.UDPChannel(
    local_ip=LOCAL_IP,
    local_port=LOCAL_PORT,
    remote_port=REMOTE_PORT,
    remote_ip=REMOTE_IP)


clear_screen()
display = NeoDisplay(256)

# create the display, initialized to ' '
# just an array of characters seems fine as an implementation
# but it should probably be a class


    

#Creates a test json packet
def create_test_json_packet():
    w = [71, 73, 85, 91, 99, 109, 113, 127, 127]
    #test json packet
    data = {
                "sender": 'joystick',
                "message": 'raw_display',
                "num_pixels": len(w),
                "pixel_values": w,
                "clear": 1
            }
    json_data = json.dumps(data)
    return json_data


# Loop forever
while 1:

    # read the incoming udp packet
    received = True 
    if received:    
        
        # parse the packet with json parser
        # someone figure this one out?  
        
        d = json.loads(create_test_json_packet())
        
        
        # extract the values from the resulting dictionary
        clear_directive = False
        if(d['clear'] == 1):
            clear_directive = True
        sender = d['sender']
        message = d['message']
        num_pixels = d['num_pixels']
        pixel_values = d['pixel_values']            
        # if there is a "clear" directive, clear the display 
        
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
