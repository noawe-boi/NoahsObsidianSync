
## Changes
### Temp Sensor
- Installed Temp sensor 
- Connected Temp sensor to A3 Input, 5v and ground
- Set A3 pin to input (code)\
- Created scaledTemp variable (float)
- Created rawTemp Variable (for necessary calculations)
- Created temperature Function
- Set rawTemp value
	A3 and multiplied by 5/1024

- Set scaledTemp value to 
	`(rawTemp - 0.50)*100.00;
	(*the extra 0's after the decimal point are to ensure calculations are done to this number of decimal places*)
### LCD
- Connected GND and VCC to ground and 5v respectively
- Added contrast potentiometer
- Connected 5v to terminal 1 and ground to terminal 2 of potentiometer
- Connected V0 (Contrast pin) to  wiper blade of potentiometer.
- Connected RS (register select pin) to digital pin 12 of Arduino
- Connected LCD pins D4-D7 with Arduino digital pins 5-7
- Create Constant integers to use with library:
	rs = 12, 
	en = 11, 
	d4 = 5, 
	d5 = 4, 
	d6 = 3, 
	d7 = 2;

- Initiated liquidcrystal library using these variables 
	`LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

- Initialize LCD and set number of columns and rows
	`lcd.begin(16, 2);

- Create writeLCD function
- Remove previous pin initializations from when LED's were used.
- Removed previous code that set LED pins HIGH and LOW and displayed time using them

- Set cursor to (0, 0) and printed `"Time: ", disp_hours, ":", minutes, ":", seconds` to LCD
- wrote 'if' statement to add "0" when the time segment value is less than 10 
- Corrected ampm setting to that it is only true when hours>=12, not hours>12
- Set cursor to (0, 1) and printed "Temp: ", scaledTemp, " Cel     " to LCD (extra spaces after " Cel" are to clear display spaces  without causing flickering)

added "writeLCD" and "temperatureFunction" functions to main loop