from gpiozero import OutputDevice

import time
import reader

from time import sleep
relay = OutputDevice(18, active_high=False, initial_value=False)
opened = False

'''
door.open()
--
Opens the door (or will open it, one day, prints 'door opened' for now)
--
'''
def open():
    global opened
    opened = True
    relay.on()
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
    if opened is True:
        time.sleep(3)
        relay.off()
        print('Door locked')
        opened = False
