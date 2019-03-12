import nfc
import time

clf = False

import login
import door
import reader
import db

'''
on_tag_connect(tag)
--
Checks sequentially for the tag :
- Tag type : Deny access if not NTAG203/213
- Exit tags : Exit program if tag ID in exit list
- Whitelist : Allow access if tag ID in whitelist
- Blacklist : Deny access if tag ID is blacklist
- Login : Sends tag ID to cards API, allow access if tag is linked to a login

If tag is a valid student tag, a time record is written on the tag
--
tag : NFC tag object, given by the NFC backend
'''
def on_tag_connect(tag):
    id_str = reader.get_id(tag)
    print('ID: ' + id_str)
    print('Product: ' + tag.product)

    if tag.product not in {'NXP NTAG203', 'NXP NTAG213'}:
        print('Invalid tag type')
        reader.beep(clf, 3)
        time.sleep(5)
        return True

    if db.check_exit_tags(id_str) is True:
        print('Exit tag scanned, closing...')
        clf.close()
        return True

    if db.check_whitelist(id_str) is True:
        print('Tag in whitelist authenticated')
        reader.beep(clf, 2)
        door.open()
        return True

    if db.check_blacklist(id_str) is True:
        print('Blacklisted card tried to open')
        reader.beep(clf, 5)
        return True

    login_str = login.retrieve(id_str)
    if login_str == 'UNKNOWN':
        print('Unknown card scanned')
        reader.beep(clf, 3)
        return True
    print('Authentified ' + login_str)

    try:
        reader.write_time_record(tag)
    except nfc.tag.tt2.Type2TagCommandError:
        print('Error when writing tag')
        reader.beep(clf, 1)
        time.sleep(1)
    reader.beep(clf, 1)
    door.open()
    return True

'''
read_tag_loop(clf)
--
Scans for a tag, until the nfc device backend is closed
--
clf : NFC backend device
'''
def read_tag_loop(clf):
    clf.connect(rdwr={'on-connect': on_tag_connect,
                      'on-release': door.close,
                      'beep-on-connect': False, 'targets': ['106A']})

'''
main()
--
Launches the nfc device backend, then launching the read tag loop
'''
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
