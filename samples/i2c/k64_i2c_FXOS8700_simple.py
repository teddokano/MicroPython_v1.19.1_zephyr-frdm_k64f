from machine import I2C
from utime import sleep

def main():
	i2c = I2C("I2C_0")
	print( i2c.scan() )

	i2c.writeto( 29, bytearray( [0x2A, 0x01] ) )

	while True:
		i2c.writeto( 29, bytearray( [ 0 ] ) )
		r	= list( i2c.readfrom( 29, 7 ) )
		
		x, y, z = byte2g( r[ 1: ] ), byte2g( r[ 3: ] ), byte2g( r[ 5: ] )
		print( x, y, z )
		sleep( 1 )
		
def byte2int16( v ):
	i	= v[ 0 ] << 8 | v[ 1 ]
	if i & 0x8000:
		i	= (i ^ 0xFFFF) * -1 - 1
	
	return i

def byte2g( v ):
	i	= v[ 0 ] << 8 | v[ 1 ]
	if i & 0x8000:
		i	= (i ^ 0xFFFF) * -1 - 1
	
	return i / 4096

main()
