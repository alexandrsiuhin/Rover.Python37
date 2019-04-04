import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)
kernelclos = np.ones((5, 5), np.uint8)
hsv_min = np.array((32, 141, 35), np.uint8)
hsv_max = np.array((132, 255, 255), np.uint8)

'''
(32, 141, 35)
(134, 255, 255)
'''


def filterCamera(agreement):
    __hsv = cv2.cvtColor(agreement, cv2.COLOR_BGR2HSV_FULL)
    __thresh = cv2.inRange(__hsv, hsv_min, hsv_max)
    __opening = cv2.morphologyEx(__thresh, cv2.MORPH_OPEN, kernel)
    __clos = cv2.morphologyEx(__opening, cv2.MORPH_CLOSE, kernelclos)
    if np.sum(__clos) > 0:
        return __clos
    else:
        __clos = [0]
        return __clos
    # newAgreement = cv2.morphologyEx(__opening, cv2.MORPH_CLOSE, kernelclos)
    # return newAgreement
