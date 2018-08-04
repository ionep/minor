import RPi.GPIO as GPIO;
import time;
GPIO.setmode(GPIO.BOARD);

GPIO.setup(40, GPIO.IN);
while(1):
	'''print("high");
	GPIO.output(40,GPIO.HIGH);
	time.sleep(3);
	print("low");
	GPIO.output(40,GPIO.LOW);
	time.sleep(3); '''
	a=GPIO.input(40);
	print(a);
