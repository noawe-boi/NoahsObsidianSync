
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
- Connected RS (register select pin) to digital pin 12 of arduino