import cv2
import numpy


# bottom_hsv = numpy.array([42, 30, 17])
# top_hsv = numpy.array([93, 234, 146])
def ColorConvert(__image, __bottom_hsv, __top_hsv, __kernel, __counturColor, __counturWidth):
    # Kernel
    open_kern = numpy.ones((__kernel, __kernel), numpy.uint8)

    hsv = cv2.cvtColor(__image, cv2.COLOR_BGR2HSV)

    __percolator = cv2.inRange(hsv, __bottom_hsv, __top_hsv)
    _percolator = cv2.morphologyEx(__percolator, cv2.MORPH_OPEN, open_kern, iterations=2)
    percolator = cv2.morphologyEx(_percolator, cv2.MORPH_CLOSE, open_kern)

    contours, hierarchy = cv2.findContours(percolator.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(__image, contours, -1, __counturColor, __counturWidth, cv2.LINE_AA, hierarchy, 1)

    return percolator,contours
