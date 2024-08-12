
## Changes 
- Installed Temp sensor 
- Connected Temp sensor to A3 Input, 5v and ground
- Set A3 pin to input (code)
- Created scaledTemp variable (float)
- Created rawTemp Variable (for necessary calculations)
- Created temperature Function
- Set rawTemp value to A3 and multiplied by 5/1024
- Set scaledTemp value to `(rawTemp - 0.50)*100.00;