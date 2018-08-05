from lcd import *
from datetime import datetime
import urllib2
from urllib import urlencode

url="http://localhost/index.php";

def exam(keypad,serial):
	lcd_clear();
	lcd_string("Exam Selected",LCD_LINE_1);
	time.sleep(2);
	while True:
		lcd_clear();
		lcd_string("No of teachers:",LCD_LINE_1);
		lcd_string("1 or 2",LCD_LINE_2);
		while(not(keypad.isNew())):
			i=1;
		number=keypad.read();
		if(number==10):
			break;
		#print(periods);
		if(number<1 or number>2):
			lcd_clear();
			lcd_string("Invalid Number",LCD_LINE_1);
			time.sleep(1);
			continue;
		lcd_string(str(number)+" Teachers",LCD_LINE_1);
		lcd_string("       Selected",LCD_LINE_2);
		time.sleep(1);
		while(number==1 or number==2):
			lcd_clear();
			lcd_string("Insert Code1:",LCD_LINE_1);
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
			code1=code;
			data={
				'code':code,
				'periods':0,
				'exam':0
			}
			encoded=urlencode(data)
			website=urllib2.urlopen(url,encoded);
			result= website.read();
			if(result=="-1"):
				lcd_clear();
				lcd_string("Invalid Code.",LCD_LINE_1);
				time.sleep(1);
				continue;
			else:
				lcd_clear();
				lcd_string("Welcome",LCD_LINE_1);
				lcd_string(result,LCD_LINE_2);
				time.sleep(1);
				code2=[];
				while(number==2):
					lcd_clear();
					lcd_string("Insert Code2:",LCD_LINE_1);
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
					code2=code;
					data={
						'code':code,
						'periods':0,
						'exam':0
					}
					encoded=urlencode(data)
					website=urllib2.urlopen(url,encoded);
					result= website.read();
					if(result=="-1"):
						lcd_clear();
						lcd_string("Invalid Code.",LCD_LINE_1);
						time.sleep(1);
						continue;
					else:
						lcd_clear();
						lcd_string("Welcome",LCD_LINE_1);
						lcd_string(result,LCD_LINE_2);
						time.sleep(1);
						break;
				start=datetime.now();
				diff=0;
				hour=0;
				minute=0;
				while(diff<=90): #need to change to seconds
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
							'mode':2,
							'code':code1,
							'code2':code2,
							'number':number,
							'period':0,
							'time':int(diff)
						};
						encoded=urlencode(data)
						website=urllib2.urlopen(url,encoded);
						a=website.read();
						#print a;
						if(a=="-1"):
							lcd_clear();
							lcd_string("Student Not",LCD_LINE_1);
							lcd_string("Found",LCD_LINE_2);
						elif(a=="-2"):
							lcd_clear();
							lcd_string("Multiple ",LCD_LINE_1);						
							lcd_string("attendance",LCD_LINE_2);						
							
						elif(a=="0"):
							lcd_clear();
							lcd_string("Going Out",LCD_LINE_1);
						
						elif(a=="1"):
							lcd_clear();
							lcd_string("Welcome Back",LCD_LINE_1);
						
						elif(a=="-3"):
							lcd_clear();
							lcd_string("You are",LCD_LINE_1);
							lcd_string("   late",LCD_LINE_2);
							
						elif(a=="-4"):
							lcd_clear();
							lcd_string("You cant go",LCD_LINE_1);
							lcd_string("out now",LCD_LINE_2);
							
						elif(a=="-5"):
							lcd_clear();
							lcd_string("You are",LCD_LINE_1);
							lcd_string("already out",LCD_LINE_2);
						else:
							lcd_clear();
							lcd_string("Welcome",LCD_LINE_1);
							lcd_string(a,LCD_LINE_2);
						time.sleep(2);
	
	
