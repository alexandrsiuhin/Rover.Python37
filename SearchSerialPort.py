import serial

from ExceptionFile import *

__COMlist = []

# Document Creation
ErrorAttachment = open("SerialErrorAttachment.txt", "w")


def Search(__baudrate=9600, timeSleep=5):
    # Port Database
    __COM = ['COM' + str(i) for i in range(2, 100)]

    for _COM in __COM:
        try:
            COMport = (serial.Serial(port=_COM, \
                                     baudrate=__baudrate, \
                                     parity=serial.PARITY_NONE, \
                                     stopbits=serial.STOPBITS_ONE, \
                                     bytesize=serial.EIGHTBITS, \
                                     timeout=0))

            if COMport:
                # COMlist Creation
                __COMlist.append(_COM)
            else:
                raise COMException("COM Error")
                pass

        except Exception as e:
            ErrorAttachment = open("SerialErrorAttachment.txt", "a")
            ErrorAttachment.write(e.__class__.__name__ + "\r")
            ErrorAttachment.close()
            continue

    print("SearchSerialPort__COMlist = ", __COMlist)
    return __COMlist
