from gpiozero import DigitalOutputDevice

import time
import reader

door = DigitalOutputDevice(11 , initial_value=False)
opened = False

'''
door.open()
--
Opens the door (or will open it, one day, prints 'door opened' for now)
--
'''
def open():
    global opened
    global door
    opened = True
    door.on()
    print('Door unlocked')

'''
door.close()
--
Closes the door after a delay, if it is opened (one day...)
--
tag argument is unused and given by nfcpy
'''
def close(tag):
    global opened
    global door
    if opened is True:
        time.sleep(3)
        door.off()
        print('Door locked')
        opened = False
