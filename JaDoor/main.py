import nfc
import time

clf = False
exit_global = False

import login
import door
import reader

def on_tag_connect(tag):
    id_str = reader.get_id(tag)
    print(tag)
    print('ID: ' + id_str)
    print('Product: ' + tag.product)

    if tag.product not in {'NXP NTAG203', 'NXP NTAG213'}:
        print('Invalid tag type')
        #reader.beep(clf, 7)
        time.sleep(5)
        return True

    if login.check_exit_tags(id_str) is True:
        print('Exit tag scanned, closing...')
        global exit_global
        exit_global = True
        return True

    if login.check_uid_whitelist(id_str) is True:
        print('Tag in whitelist authenticated')
        #reader.beep(clf, 1)
        door.open()
        return True

    if login.check_blacklist(id_str) is True:
        print('Blacklisted card tried to open')
        #reader.beep(clf, 3)
        return True

    login_str = login.retrieve(id_str)
    if login_str == 'UNKNOWN':
        print('Unknown card scanned')
        #reader.beep(clf, 3)
        return True
    print('Authentified ' + login_str)

    try:
        reader.write_time_record(tag)
    except nfc.tag.tt2.Type2TagCommandError:
        print('Error when writing tag')
        reader.beep(clf, 1)
        time.sleep(1)
    #reader.beep(clf, 1)
    door.open()
    return True

def read_tag_loop(clf):
    while exit_global is False:
        clf.connect(rdwr={'on-connect': on_tag_connect,
                          'beep-on-connect': False, 'targets': ['106A']})

def main():
    global clf
    try:
        clf = nfc.ContactlessFrontend('usb')
    except IOError:
        print("Device error")
        exit()
    print(clf)
    read_tag_loop(clf)
    clf.close()

main()
