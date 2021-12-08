# name=Novation Launchkey MK3 25
# by Dencel K. Babu (@dencel007)

import patterns
import channels
import mixer
import device
import transport
import arrangement
import general
import launchMapPages
import playlist
import ui
import screen

import midi
import utils

Transport = {
    'Stop': 0x74,
    'Start':  0x73,
    'Record': 0x75,
    'Loop': 0x76
}

Pads = {
    'Pad01':0x2C,
    'Pad02':0x2D,
    'Pad03':0x2E,
    'Pad04':0x2F,
    'Pad05':0x30,
    'Pad06':0x31,
    'Pad07':0x32,
    'Pad08':0x33,
    'Pad09':0x24,
    'Pad10':0x25,
    'Pad11':0x26,
    'Pad12':0x27,
    'Pad13':0x28,
    'Pad14':0x29,   
    'Pad15':0x2A,
    'Pad16':0x2B
}

Device = {
    'DSelect':0x33,
    'DLock':0x34
}

EventNameT = ['Note Off', 'Note On ', 'Key Aftertouch', 'Control Change', 'Program Change', 'Channel Aftertouch', 'Pitch Bend', 'System Message']
              
class LKMK3():
    def __init__(self):
        return

    def OnInit(self):
        print('init ready')

    def OnDeInit(self):
        print('deinit ready')
        
    def OnMidiMsg(self, event):
        event.handled = False
        print ("{:X} {:X} {:2X} {}".format(event.status, event.data1, event.data2,  EventNameT[(event.status - 0x80) // 16] + ': '+  utils.GetNoteName(event.data1)))
            
        # Use midi.MIDI_NOTEON for note events.
        if event.midiId == midi.MIDI_CONTROLCHANGE:
            if event.data2 > 0:
                if event.data1 == Transport['Stop']:
                    transport.stop()
                    event.handled = True
                elif event.data1 == Transport['Start']:
                    transport.start()
                    event.handled = True
                elif event.data1 == Transport['Record']:
                    transport.record()
                    event.handled = True
                elif event.data1 == Transport['Loop']:
                    transport.setLoopMode()
                    event.handled = True
        
        #FL Window Stuff
        GlobalMIDIChannel = event.status // 16
        
        #Show Window
        if (GlobalMIDIChannel == 0xB) and (event.data1 == Pads['Pad01']) and (event.data2 == 0x7F):
            ui.showWindow(2)            
        if (GlobalMIDIChannel == 0xB) and (event.data1 == Pads['Pad02']) and (event.data2 == 0x7F):
            ui.showWindow(1)            
        if (GlobalMIDIChannel == 0xB) and (event.data1 == Pads['Pad03']) and (event.data2 == 0x7F):
            ui.showWindow(3)        
        if (GlobalMIDIChannel == 0xB) and (event.data1 == Pads['Pad04']) and (event.data2 == 0x7F):
            ui.showWindow(0)          
        
        #Hide Window
        if (GlobalMIDIChannel == 0xB) and (event.data1 == Pads['Pad01']) and (event.data2 == 0):
            ui.hideWindow(2)            
        if (GlobalMIDIChannel == 0xB) and (event.data1 == Pads['Pad02']) and (event.data2 == 0):
            ui.hideWindow(1)          
        if (GlobalMIDIChannel == 0xB) and (event.data1 == Pads['Pad03']) and (event.data2 == 0):
            ui.hideWindow(3)        
        if (GlobalMIDIChannel == 0xB) and (event.data1 == Pads['Pad04']) and (event.data2 == 0):
            ui.hideWindow(0)
            
        #Navigation
        if (GlobalMIDIChannel == 0xB) and (event.data1 == Pads['Pad06']) and (event.data2 == 0x7F):
            ui.escape()
        if (GlobalMIDIChannel == 0xB) and (event.data1 == Pads['Pad07']) and (event.data2 == 0x7F):
            ui.up()
        if (GlobalMIDIChannel == 0xB) and (event.data1 == Pads['Pad08']) and (event.data2 == 0x7F):
            ui.enter()
        if (GlobalMIDIChannel == 0xB) and (event.data1 == Pads['Pad14']) and (event.data2 == 0x7F):
            ui.left()
        if (GlobalMIDIChannel == 0xB) and (event.data1 == Pads['Pad15']) and (event.data2 == 0x7F):
            ui.down()
        if (GlobalMIDIChannel == 0xB) and (event.data1 == Pads['Pad16']) and (event.data2 == 0x7F):
            ui.right()
        
        #Global Transport
        if (GlobalMIDIChannel == 0xB) and (event.data1 == Pads['Pad09']) and (event.data2 == 0x7F):
            transport.globalTransport(midi.FPT_Metronome, True)
        if (GlobalMIDIChannel == 0xB) and (event.data1 == Pads['Pad10']) and (event.data2 == 0x7F):
            transport.globalTransport(midi.FPT_Overdub, True)
        if (GlobalMIDIChannel == 0xB) and (event.data1 == Pads['Pad11']) and (event.data2 == 0x7F):
            transport.globalTransport(midi.FPT_CountDown, True)        
        if (GlobalMIDIChannel == 0xB) and (event.data1 == Pads['Pad12']) and (event.data2 == 0x7F):
            transport.globalTransport(midi.FPT_TapTempo, True)
            
        #Window Focus
        #if (GlobalMIDIChannel == 0xB) and (event.data1 == Device['DSelect']) and (event.data2 == 0x7F):
            #print("Button
            #transport.globalTransport(midi.FPT_MixerWindowJog, True)

Launchkey = LKMK3()
def OnInit():
    Launchkey.OnInit()
def OnDeInit():
    Launchkey.OnDeInit()
def OnMidiMsg(event):
    Launchkey.OnMidiMsg(event)