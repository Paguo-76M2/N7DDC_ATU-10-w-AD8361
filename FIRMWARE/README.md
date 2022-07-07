# Firmware files

The PIC16F1451_FW.hex is to be flashed into the PIC16F1454 chip - just once. The chip will serve as the gateway to upload firmwares into the PIC16F18877 chip. When connected to USB port of a computer - the ATU-10 will appear as an USB-disk with the link to the project's official GITHUB page. Copying HEX files to this disk will flash the PIC16F18877.

The ATU-10_*.hex files are the firmwares for the PIC16F18877 chip.
The file with the "AD8361" substring in the filename is intended for devices with the AD8361 TruPWR chips installed. If you still have diode detectors (as on the original N7DDC boards) - flash files with the "diodes" substring respectively.