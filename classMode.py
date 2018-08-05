from lcd import *
from datetime import datetime
import urllib2
from urllib import urlencode

url="http://localhost/index.php";

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
			data={
				'code':code,
				'periods':periods,
				'exam':0
			}
			encoded=urlencode(data)
			website=urllib2.urlopen(url,encoded);
			result= website.read();
			if(result!="-1"):
				lcd_clear();
				lcd_string("Welcome",LCD_LINE_1);
				lcd_string(result,LCD_LINE_2);
				time.sleep(1);
				start=datetime.now();
				diff=0;
				hour=0;
				minute=0;
				while(diff<=periods*50): #need to change to seconds
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
						data={
							'roll':y,
							'mode':1,
							'code':code,
							'period':periods
						};
						encoded=urlencode(data)
						website=urllib2.urlopen(url,encoded);
						a=website.read();
						if(a=="-1"):
							lcd_clear();
							lcd_string("Student Not",LCD_LINE_1);
							lcd_string("Found",LCD_LINE_2);
						elif(a=="-2"):
							lcd_clear();
							lcd_string("Multiple ",LCD_LINE_1);						
							lcd_string("attendance",LCD_LINE_2);						
							
						elif(a=="=3"):
							lcd_clear();
							lcd_string("You are ",LCD_LINE_1);
							lcd_string("     late",LCD_LINE_2);
						else:
							lcd_clear();
							lcd_string("Welcome",LCD_LINE_1);
							lcd_string(a,LCD_LINE_2);
						time.sleep(2);
			else:
				lcd_clear();
				lcd_string("Invalid Code.",LCD_LINE_1);
				time.sleep(1);
				continue;
			
