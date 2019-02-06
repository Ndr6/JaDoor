import time
import ndef
import datetime

def beep(clf, nb):
    i = 0
    while i < nb:
        clf.device.turn_on_led_and_buzzer()
        time.sleep(0.05)
        clf.device.turn_off_led_and_buzzer()
        time.sleep(0.1)
        i += 1

def get_id(tag):
    return tag.identifier.encode("hex").upper()


def write_time_record(tag):
    if tag.ndef is None:
        return
    timerecord = ndef.TextRecord(
        datetime.datetime.now().strftime("JaDoor last opened on %d/%m/%Y - %H:%M:%S"))
    second_record = ndef.TextRecord('Don\'t forget to make unit tests -- <3 Ndr')
    print('Writing time record')
    tag.ndef.records = [timerecord, second_record]
