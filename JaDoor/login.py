import requests

def check_blacklist(id_str):
    blacklist = {}
    if id_str in blacklist:
        print('Tag in blacklist scanned')
        return True
    return False

def check_whitelist(id_str):
    whitelist = {'049ADB0A853280'}
    if id_str in whitelist:
        return True
    return False

def check_exit_tags(id_str):
    exit_tags = {'043FE9CA333580'}
    if id_str in exit_tags:
        return True
    return False

def retrieve(id_str):
    req = requests.get('https://whatsupdoc.epitech.eu/card/' + id_str)
    if req.status_code == 200 and 'login' in req.json():
        print('Identified student card')
        return req.json()['login']
    else:
        print('Invalid response from cards API.')
        return 'UNKNOWN'