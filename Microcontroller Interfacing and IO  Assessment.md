
## Changes \
### Temp Sensor
- Installed Temp sensor 
- Connected Temp sensor to A3 Input, 5v and ground
- Set A3 pin to input (code)\
- Created scaledTemp variable (float)
- Created rawTemp Variable (for necessary calculations)
- Created temperature Function
- Set rawTemp value to A3 and multiplied by 5/1024
- Set scaledTemp value to `(rawTemp - 0.50)*100.00;

### LCD
- Connected GND and VCC to ground and 5v respectively
- Added contrast potentiometer
- Connected 5v to terminal 1 and ground to terminal 2 of potentiometer
- Connected V0 (Contrast pin) to  wiper blade of potentiometer.
- Connected RS (register select pin) to digital pin 12 of Arduino


// initialize the library by associating any needed LCD interface pin47// with the arduino pin number it is connected to48const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;49LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
