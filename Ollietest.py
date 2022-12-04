#!/usr/bin/python
from bluepy import btle
import struct
import time
import Ollie_driver
import sys
ollie = Ollie_driver.Sphero()
ollie.connect()


ollie.start()
time.sleep(2)
ollie.set_rgb_led(255,0,0,0,False)
time.sleep(1)
ollie.set_rgb_led(0,255,0,0,False)
time.sleep(1)
ollie.set_rgb_led(0,0,255,0,False)
time.sleep(3)
ollie.join()
ollie.disconnect()
sys.exit(1)

