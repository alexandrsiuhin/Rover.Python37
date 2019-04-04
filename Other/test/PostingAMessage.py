import serial
__port = "COM3"
__message = "1."
while True:
    message = serial.Serial(__port, baudrate=115200)
    message.write(__message)
    print(__port)
    print(__message)
