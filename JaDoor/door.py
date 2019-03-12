from gpiozero import OutputDevice

import time
import reader

from time import sleep
door = OutputDevice("GPIO17", active_high=False, initial_value=False)
opened = False

door.on()
sleep(3)
door.off()
sleep(3)
door.on()

'''
door.open()
--
Opens the door (or will open it, one day, prints 'door opened' for now)
--
'''
def open():
    global opened
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
    if opened is True:
        time.sleep(3)
        door.off()
        print('Door locked')
        opened = False
