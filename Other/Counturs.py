import numpy
import cv2 as cv

from Variables import *
from ColorConvert import ColorConvert

# bottom_hsv = numpy.array([42, 30, 17])
# top_hsv = numpy.array([93, 234, 146])

capture = cv.VideoCapture(0)

while (True):

    # Frame Acquisition
    availability = False
    availability, frame = capture.read()

    percolator,contours = ColorConvert(frame, bottom_hsv, top_hsv, kernel, counturColor, counturWidth)


    #contours, hierarchy = cv.findContours(percolator.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    areas = [cv.contourArea(c) for c in contours]
    max_index = numpy.argmax(areas)
    cnt=contours[max_index]

    x,y,w,h = cv.boundingRect(cnt)
    cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv.imshow("Show",frame)

    #cv.drawContours( frame.copy(), contours, -1, (255,0,0), 3, cv.LINE_AA, hierarchy, 1 )
    cv.imshow('frame', frame)
    cv.imshow('percolator', percolator)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
