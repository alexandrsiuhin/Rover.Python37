import serial
import time

import SearchSerialPort
import CheckSerialPort

from Variables import *

# Intro
while (True):
    try:
        # Output Active Ports
        COMList = SearchSerialPort.Search(baudrate, timeSleep)
        print("main COMList = ", COMList)

        # Check Active Ports
        ActivePORT = CheckSerialPort.CheckSerialPortMessage(COMList, baudrate, timeSleep)
        print("ActivePORT = ", ActivePORT)
        break

    except Exception as EX:
        print(EX)
        break

# Connection Creation
port = serial.Serial(port=str(ActivePORT), \
                     baudrate=baudrate, \
                     parity=serial.PARITY_NONE, \
                     stopbits=serial.STOPBITS_ONE, \
                     bytesize=serial.EIGHTBITS, \
                     timeout=0)
time.sleep(5)

# Main Code
import cv2
import Trapezium

from ColorConvert import ColorConvert
from ExceptionFile import *

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FPS, fps)

while (True):

    try:
        # Frame Acquisition
        availability = False
        availability, frame = capture.read()

        # Frame Parameters
        height, width, c = frame.shape

        # No Frame Error
        if availability is False or frame is None:
            raise CV2Exception("no frame")

        # trapezium Pinting
        Trapezium.Trapezium(frame, width, height, pointColor, pointRadius, lineColor, lineWidth, textColor,
                            textFont, bottomAngleA, bottomAngleD, topAngleB, topAngleC)

        # Color Filter
        percolator = ColorConvert(frame, bottom_hsv, top_hsv, kernel, counturColor, counturWidth)

        # Rectangular Contour Selection
        # Rect = cv2.getStructuringElement()

        # Event Processing

        # Posting a Message
        port.write(b"ARDUINO.")

        # Imshow
        cv2.imshow('frame', frame)
        cv2.imshow('percolator', percolator)
        # cv2.imshow('Rect', Rect)

    # End Exception
    except Exception as e:
        print(e, e.__class__.__name__)
        ErrorAttachment = open("MainErrorAttachment.txt", "w")
        ErrorAttachment.write(e.__class__.__name__ + "\r")
        break

    # End work
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
