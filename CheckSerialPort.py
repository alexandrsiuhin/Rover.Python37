import serial
import time


def CheckSerialPortMessage(__activeCOM=[], __baudrate=9600, __timeSleep=5):
    try:
        for __COM in __activeCOM:

            port = serial.Serial(__COM, __baudrate)
            time.sleep(__timeSleep)
            large = len(port.readline())
            port.read(large)

            while True:

                if large > 3:
                    for a in range(__timeSleep):

                        date = port.readline().decode().split()

                        if ('MotorShield' in date):
                            return __COM
                            break
                        else:
                            continue
                    else:
                        break
                break
    except Exception as e:
        print(e)
        pass
