from Variables import *


import SearchSerialPort
from Other.ReadAMessage import SendinglMessgage


while (True):
    try:
        # Event Processing
        # Posting a Message
        # postingMessage(message)

        # Output Active Ports
        COMList = SearchSerialPort.Search(baudrate, timeSleep)
        print(COMList)

        # Check Active Ports
        ActivePORT = SendinglMessgage(COMList, baudrate, timeSleep)
        print("ActivePORT = ", ActivePORT)

    # End Exception
    except Exception as e:
        print(e, e.__class__.__name__)
        ErrorAttachment = open("ErrorAttachment.txt", "w")
        ErrorAttachment.write(e.__class__.__name__ + "\r")
        break
