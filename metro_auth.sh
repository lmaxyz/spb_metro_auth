#!/bin/bash

AUTH_START_URL="https://auth.wi-fi.ru/spb/gapi/auth/start?segment=spbmetro_m3_4"
AUTH_INIT_URL="https://auth.wi-fi.ru/spb/gapi/auth/init"
AUTH_INIT_DATA='{"mode":0,"segment":"spbmetro_m3_4"}'


curl -s $AUTH_START_URL > /dev/null

echo "[*] Authorization..."
RESP=$(curl -s --data $AUTH_INIT_DATA $AUTH_INIT_URL)

if [[ $RESP == *"success"* ]]; then
    echo "[+] Success!!!"
else
    echo "[!] Error. Try again later."
fi
