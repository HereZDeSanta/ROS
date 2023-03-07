#!/usr/bin/env python3
import datetime
import time

def display_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

while True:
    display_time()
    time.sleep(5)
