#
# A sample code from https://github.com/micropython/micropython/blob/master/ports/zephyr/README.md
#

from machine import I2C

i2c = I2C("I2C_0")
print( i2c.scan() )
