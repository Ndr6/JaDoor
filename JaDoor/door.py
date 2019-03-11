import time
import reader

opened = False

def open():
    global opened
    opened = True
    print('Door unlocked')

def close(tag):
    global opened
    if opened is True:
        time.sleep(3)
        print('Door locked')
        opened = False
