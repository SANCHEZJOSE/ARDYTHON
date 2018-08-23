import serial 
import time

arduinoData = serial.Serial('/dev/ttyACM0',9600)
while 1==1:
	datos = arduinoData.readline()
	print(datos)
arduinoData.close()
