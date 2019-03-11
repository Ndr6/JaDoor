import time
import ndef
import datetime

'''
reader.beep(clf, nb)
--
Makes the NFC reader blink its led and beep a given number of times
--
clf : NFC backend device
nb : Number of times to blink/beep
'''
def beep(clf, nb):
    i = 0
    while i < nb:
        clf.device.turn_on_led_and_buzzer()
        time.sleep(0.05)
        clf.device.turn_off_led_and_buzzer()
        time.sleep(0.1)
        i += 1

'''
reader.get_id(tag)
--
Retrieves the tag ID string from the tag object
--
tag : Tag object
'''
def get_id(tag):
    return tag.identifier.encode("hex").upper()


'''
write_time_record(tag)
--
Writes current time info on the tag
--
tag : Tag object
'''
def write_time_record(tag):
    if tag.ndef is None:
        return
    timerecord = ndef.TextRecord(
        datetime.datetime.now().strftime("JaDoor last opened on %d/%m/%Y - %H:%M:%S"))
    second_record = ndef.TextRecord('Don\'t forget to unit test your projects -- <3 Ndr')
    print('Writing time record')
    tag.ndef.records = [timerecord, second_record]
