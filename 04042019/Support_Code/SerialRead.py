import serial

serailConnection = serial.Serial("COM3", 9600)  # change ACM number as found from ls /dev/tty/ACM*

while True:
     print(serailConnection.readline())
