# name=Novation Launchkey MK3 25
# by Dencel K. Babu (@dencel007)

# define variables
play_key = 0x73
stop_key = 0x74
record_key = 0x75
loop_key = 0x76

# imports
import transport

def OnMidiMsg(event):
    event.handled = False
    if event.data2 > 0:
        if event.data1 == play_key:
            transport.start()
            event.handled = True
        if event.data1 == stop_key:
            transport.stop()
            event.handled = True
        if event.data1 == record_key:
            transport.record()
            event.handled = True
        if event.data1 == loop_key:
            transport.setLoopMode()
            event.handled = True
