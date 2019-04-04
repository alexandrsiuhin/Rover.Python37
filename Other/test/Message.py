# отправка сообщения по последовательному порту
import serial
import time

def Message(__COM, __baudrate=9600, __msg = "ARDUINO"):
    __inCOM = 'COM' + str(__COM)


    port = serial.Serial(port=str(__inCOM), \
                         baudrate=__baudrate, \
                         parity=serial.PARITY_NONE, \
                         stopbits=serial.STOPBITS_ONE, \
                         bytesize=serial.EIGHTBITS, \
                         timeout=0)

    time.sleep(5)
    #__message = ((__msg) + ".").encode("utf-8")
    __message = ('ARDUINO.')
    port.write(b"ARDUINO.")
    time.sleep(5)
    port.write(b"RDUINO.")
    print("RDUINO")

Message(3)
