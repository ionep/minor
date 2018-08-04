from lcd import *
from datetime import datetime

def classes(keypad,serial):
	lcd_clear();
	lcd_string("Class Selected",LCD_LINE_1);
	time.sleep(2);
	while True:
		lcd_clear();
		lcd_string("No of Periods:",LCD_LINE_1);
		while(not(keypad.isNew())):
			i=1;
		periods=keypad.read();
		if(periods==10):
			break;
		#print(periods);
		if(periods<1 or periods>8):
			lcd_string("Invalid Periods",LCD_LINE_1);
			time.sleep(1);
			continue;
		lcd_string(str(periods)+" Periods",LCD_LINE_1);
		lcd_string("       Selected",LCD_LINE_2);
		time.sleep(1);
		while(periods>=1 and periods<=8):
			lcd_clear();
			lcd_string("Insert Code:",LCD_LINE_1);
			code="";
			block="";
			while(True):
				while(not(keypad.isNew())):
					i=1;
				data=keypad.read();
				if(data==10 and len(code)>0):
					code=code[:-1];
					block=block[:-1];
				elif(data==11):
					break;
				else:
					code=code+str(data);
					block=block+"*";
				lcd_string(block,LCD_LINE_2);
			#code=raw_input();
			if(code=="0000"):
				lcd_clear();
				lcd_string("Correct Code",LCD_LINE_1);
				time.sleep(1);
				start=datetime.now();
				diff=0;
				hour=0;
				minute=0;
				while(diff<=100): #seconds
					diff=(datetime.now()-start).total_seconds();
					minute=int(diff)-hour*60;
					#minute=int(diff/60)-hour*60;
					if(minute>=60):
						hour=hour+1;
						minute=minute-60;
					
					#format display
					displayTime="";
					if(hour<10):
						displayTime="0";
					displayTime=displayTime+str(hour);
					displayTime=displayTime+":";
					if(minute<10):
						displayTime=displayTime+"0";
					displayTime=displayTime+str(minute);
					lcd_string(displayTime,LCD_LINE_2);
					lcd_string("Scan Card:",LCD_LINE_1);
					y="";
					x=serial.read();
					if(x=='~'):
						while True:
							x=serial.read();
							if(x=='`'):
								break;
							y=y+str(x);	
						print y;
			else:
				lcd_clear();
				lcd_string("Invalid Code.",LCD_LINE_1);
				time.sleep(1);
				continue;
			
