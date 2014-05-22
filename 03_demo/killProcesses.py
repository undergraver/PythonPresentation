#!/usr/bin/env python

# This code is under BSD 2-clause license

import psutil

list_to_kill=["excel.exe","notepad.exe"]

for proc in psutil.process_iter():
    try:
        name = proc.name()
        pid = proc.pid
        if name.lower() in list_to_kill:
            print("Killing "+name + "(" + str(pid) + ")")
            proc.kill()
    except:
        pass
