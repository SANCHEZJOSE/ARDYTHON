import serial 
import time
from datetime import datetime
i=0
arduinoData = serial.Serial('/dev/ttyACM0',2000000)
archivo=open("test.csv","w+")
while 1==1:
	datos = arduinoData.readline()
	archivo.write(datos)
	i=i+1
	if i==10:
		break
archivo.close()
arduinoData.close()


