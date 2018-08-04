import RPi.GPIO as GPIO

pin=[11,32,19,21,23,12,16,18,36,24,26,7];

class Keypad:
	value=-1;
	update=False;
	def button0(self):
	    self.value=0;
	    self.update=True;
	def button1(self):
		self.value=1;
		self.update=True;
	def button2(self):
	    self.value=2;
	    self.update=True;
	def button3(self):
		self.value=3;
		self.update=True;
	def button4(self):
	    self.value=4;
	    self.update=True;
	def button5(self):
		self.value=5;
		self.update=True;
	def button6(self):
	    self.value=6;
	    self.update=True;
	def button7(self):
		self.value=7;
		self.update=True;
	def button8(self):
	    self.value=8;
	    self.update=True;
	def button9(self):
		self.value=9;
		self.update=True;
	def buttonBack(self):
	    self.value=10;
	    self.update=True;
	def buttonEnter(self):
		self.value=11;
		self.update=True;
	
	def enableKeypad(self):
		self.value=-1;
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pin[0],GPIO.IN,pull_up_down=GPIO.PUD_DOWN);
		GPIO.setup(pin[1],GPIO.IN,pull_up_down=GPIO.PUD_DOWN);
		GPIO.setup(pin[2],GPIO.IN,pull_up_down=GPIO.PUD_DOWN);
		GPIO.setup(pin[3],GPIO.IN,pull_up_down=GPIO.PUD_DOWN);
		GPIO.setup(pin[4],GPIO.IN,pull_up_down=GPIO.PUD_DOWN);
		GPIO.setup(pin[5],GPIO.IN,pull_up_down=GPIO.PUD_DOWN);
		GPIO.setup(pin[6],GPIO.IN,pull_up_down=GPIO.PUD_DOWN);
		GPIO.setup(pin[7],GPIO.IN,pull_up_down=GPIO.PUD_DOWN);
		GPIO.setup(pin[8],GPIO.IN,pull_up_down=GPIO.PUD_DOWN);
		GPIO.setup(pin[9],GPIO.IN,pull_up_down=GPIO.PUD_DOWN);
		GPIO.setup(pin[10],GPIO.IN,pull_up_down=GPIO.PUD_DOWN);
		GPIO.setup(pin[11],GPIO.IN,pull_up_down=GPIO.PUD_DOWN);
		
		GPIO.add_event_detect(pin[0],GPIO.BOTH,callback=lambda x:self.button0(),bouncetime=200);
		GPIO.add_event_detect(pin[1],GPIO.BOTH,callback=lambda x:self.button1(),bouncetime=200);
		GPIO.add_event_detect(pin[2],GPIO.BOTH,callback=lambda x:self.button2(),bouncetime=200);
		GPIO.add_event_detect(pin[3],GPIO.BOTH,callback=lambda x:self.button3(),bouncetime=200);
		GPIO.add_event_detect(pin[4],GPIO.BOTH,callback=lambda x:self.button4(),bouncetime=200);
		GPIO.add_event_detect(pin[5],GPIO.BOTH,callback=lambda x:self.button5(),bouncetime=200);
		GPIO.add_event_detect(pin[6],GPIO.BOTH,callback=lambda x:self.button6(),bouncetime=200);
		GPIO.add_event_detect(pin[7],GPIO.BOTH,callback=lambda x:self.button7(),bouncetime=200);
		GPIO.add_event_detect(pin[8],GPIO.BOTH,callback=lambda x:self.button8(),bouncetime=200);
		GPIO.add_event_detect(pin[9],GPIO.BOTH,callback=lambda x:self.button9(),bouncetime=200);
		GPIO.add_event_detect(pin[10],GPIO.BOTH,callback=lambda x:self.buttonBack(),bouncetime=200);
		GPIO.add_event_detect(pin[11],GPIO.BOTH,callback=lambda x:self.buttonEnter(),bouncetime=200);
	
	def read(self):
		if(self.update):
			self.update=False;
			return self.value;
	def isNew(self):
		return self.update;
'''	
var=Keypad();
var.enableKeypad();

while(1):
	i=1;
	if(var.isNew()):
		print(var.read());
'''
