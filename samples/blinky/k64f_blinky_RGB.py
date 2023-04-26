#
# A sample code to blink on-board RGB LEDs
#

import time
from machine import Pin

LED_R = Pin(("GPIO_1", 22), Pin.OUT)
LED_G = Pin(("GPIO_4", 26), Pin.OUT)
LED_B = Pin(("GPIO_1", 21), Pin.OUT)

while True:
    LED_R.value(0)
    LED_G.value(1)
    LED_B.value(1)
    time.sleep(0.5)
    
    LED_R.value(1)
    LED_G.value(0)
    LED_B.value(1)
    time.sleep(0.5)
    
    LED_R.value(1)
    LED_G.value(1)
    LED_B.value(0)
    time.sleep(0.5)
