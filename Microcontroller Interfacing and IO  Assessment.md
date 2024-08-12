
## Changes \
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

- Wrote "Time: ", disp_hours, 
- Corrected ampm setting to that it is only true when

added functions to main loop