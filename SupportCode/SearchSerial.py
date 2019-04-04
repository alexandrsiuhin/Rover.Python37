from ExceptionFile import *
import serial
import time

__COMlist = []

ErrorAttachment = open("SerialErrorAttachment.txt", "w")


def Search(__baudrate=9600):
    __COM = ['COM' + str(i) for i in range(1, 100)]

    for COM in __COM:
        try:
            COMport = (serial.Serial(port=COM, \
                                     baudrate=__baudrate, \
                                     parity=serial.PARITY_NONE, \
                                     stopbits=serial.STOPBITS_ONE, \
                                     bytesize=serial.EIGHTBITS, \
                                     timeout=0))

            if COMport:
                __COMlist.append(COM)
            else:
                raise COMException("COM Error")
                pass

        except Exception as e:
            #print(e, e.__class__.__name__)
            ErrorAttachment = open("SerialErrorAttachment.txt", "a")
            ErrorAttachment.write(e.__class__.__name__ + "\r")
            ErrorAttachment.close()
            continue

    time.sleep(3)
    print(__COMlist)
    return __COMlist
Search()
