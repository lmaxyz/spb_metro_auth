#!/usr/bin/python

import requests


AUTH_START_URL = "https://auth.wi-fi.ru/spb/gapi/auth/start"
AUTH_INIT_URL = "https://auth.wi-fi.ru/spb/gapi/auth/init"

# Should returns json response with {status: success} and a lot of other things.
auth_start_resp = requests.get(AUTH_START_URL, params={"segment": "spbmetro_m3_4"})

print('[*] Authorization...')

auth_resp = requests.post(AUTH_INIT_URL, data={"mode": 0, "segment": "spbmetro_m3_4"})

try:
    if auth_resp.json()['auth_status'] == 'success':
        print('[*] Success!!!')
    else:
        print("[!] Can't authorize in network!!!")
        print(f"Response: {auth_resp.content}")
except KeyError:
    print('[!] Can\'t authorize in network.')

except Exception as e:
    print(f'[!] Can\'t authorize in network.\nError: {e}')
