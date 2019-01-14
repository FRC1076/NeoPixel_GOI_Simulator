try:
    from frc1076lib.udp_channel import UDPChannel as UDPChannel
except:
    from lib1076.udp_channel import UDPChannel as UDPChannel

#Ignore error here
from NeoDisplay import NeoDisplay
import time
import json
import sys, argparse
#
#   If the user sets the terminal window to 64 wide and 12 pixels
#   high the display will fill the window.   Set the font to fixed
#   width font for it to work nicely.
#
#   For starters, just run this in one terminal, and the packet producer
#   in another.
#
#   Instead of hard-coding these values, we should extract them
#   from the command line.
#   Make Sure the ports are correct
REMOTE_IP = 'localhost'
REMOTE_PORT = 8877
LOCAL_IP = 'localhost'
LOCAL_PORT = 8876


# some VT100 terminal helpers.
def clear_screen():
    print(chr(27) + '[2J', end='')


def cursor_home():
    print(chr(27) + '[H', end='')


#Deal with arguments
arguments = len(sys.argv) - 1
parser = argparse.ArgumentParser()
parser.add_argument("-LP", "--localport", help="sets localport")
parser.add_argument("-RP", "--remoteport", help="sets remoteport")
parser.add_argument("-LI", "--localip", help="sets localip")
parser.add_argument("-RI", "--remoteip", help="sets remoteip")
# read arguments from the command line
args = parser.parse_args()

# check for --version or -V
if args.localport:
    print("set local port to %s" % args.localport)
    LOCAL_PORT = args.localport
elif args.remoteport:
    print("set remote port to %s" % args.remoteport)
    REMOTE_PORT = args.remote_port
elif args.remoteip:
    print("set remote ip to %s" % args.remoteip)
    REMOTE_IP = args.remoteip
elif args.localip:
    print("set local ip to %s" % args.localip)
    LOCAL_IP = args.local_ip

# create the udp listener/receiver to read udp packets
# from port LOCAL_PORT
receiver = UDPChannel(
    local_ip=LOCAL_IP,
    local_port=LOCAL_PORT,
    remote_ip=REMOTE_IP,
    remote_port=REMOTE_PORT)

# create the display, initialized to ' '
# just an array of characters seems fine as an implementation
# but it should probably be a class
display = NeoDisplay(256)

clear_screen()
print(display.render())

# Loop forever
while 1:
    if (receiver.receive_from() == (None, None)):
        continue
    else:
        (message, (recv_addr, recv_port)) = receiver.receive_from()

    # read the incoming udp packet
    if message is not None:

        # Test this to see what exception it generates
        # if the message is not valid json.  Then add
        # try/except so we can report a problem instead
        # of blindly trying to update the display.
        d = json.loads(message)

        # extract the values from the resulting dictionary
        clear_directive = False
        if (d['clear'] == 1):
            clear_directive = True

        # we should probably check the message to make sure that
        # it is one we know how to handle
        sender = d['sender']
        message = d['message']
        num_pixels = d['num_pixels']
        pixel_values = d['pixel_values']

        # if there is a "clear" directive, clear the display
        if clear_directive:
            display.clear()

        # if there are pixel values:
        # use those values to insert '*' or ' ' in display array
        display.set_pixels(pixel_values)

        cursor_home()
        print(
            display.render('Received ' + str(pixel_values) + ' from (' +
                           str(recv_addr) + ',' + str(recv_port) + ')'))

    #
    # wait for a second before trying to read again
    # should fix this after a bit
    #
    time.sleep(1)
