from lcd import *
from classMode import *
from examMode import *
from keypad import *

if __name__ == '__main__':

  try:
    
    lcd_main(); #start lcd and display welcome message
    time.sleep(3);
    keypad=Keypad();
    keypad.enableKeypad();
    while True: #main loop
		#select mode
		lcd_string("Select Mode:",LCD_LINE_1);
		lcd_string("1:Class 2:Exam",LCD_LINE_2);
		
		#wait for keypad input
		while(not(keypad.isNew())):
			i=1;
		mode=keypad.read();
		#print(mode);
		
		#modes code
		if(mode==1): #class
			classes(keypad);
		elif(mode==2): #exams
			exam();
		else:
			lcd_string("Invalid Command",LCD_LINE_1);
			lcd_string("Try again",LCD_LINE_2);
			time.sleep(1);
			continue;
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)
    lcd_string("Goodbye!",LCD_LINE_1)
    time.sleep(2);
    lcd_clear();
    GPIO.cleanup()



