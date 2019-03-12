import gpiozero
import time

import reader

relay = gpiozero.OutputDevice("GPIO17", active_high=False, initial_value=False)
print("Relay init")
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
    relay.off()
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
        relay.on()
        print('Door locked')
        opened = False
