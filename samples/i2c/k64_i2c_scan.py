from machine import I2C

i2c = I2C("I2C_0")
print( i2c.scan() )
