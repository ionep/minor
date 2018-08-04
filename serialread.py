import time
import serial

ser=serial.Serial(
port='/dev/ttyAMA0',
baudrate=9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1	
);
while 1:
	y="";
	x=ser.read();
	if(x=='~'):
		while True:
			x=ser.read();
			if(x=='`'):
				break;
			y=y+str(x);	
		print y;
