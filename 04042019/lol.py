import cv2
import numpy as np
#import serial
from Support_Code.Camera_filter import filterCamera
from Support_Code.drowContours import contourCoordinat

frameWeight = 640
frameHigh = 480

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

#serialConnection = serial.Serial("/dev/ttyUSB0", 115200)  # change ACM number as found from ls /dev/tty/ACM*
cont = dict()

while True:
    flag, frame = cap.read()
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
