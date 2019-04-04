import numpy

''' COLOR CONVERT FILTER '''

# Filter
bottom_hsv = numpy.array([14, 91, 16])
top_hsv = numpy.array([220, 255, 97])
kernel = 4

# Countur
counturColor = (0, 255, 0)
counturWidth = 2

# TRAPEZIUM COLOR
# Point
pointColor = (0, 0, 255)
pointRadius = 3

# Line
lineColor = (255, 0, 0)
lineWidth = 4

# Text
textColor = (0, 255, 0)
textFont = 0.5

# Angle

# Bottom
bottomAngleA = 0.1
bottomAngleD = 0.9

# Top
topAngleB = 0.2
topAngleC = 0.8

''' SERIAL PORT '''
baudrate = 9600
timeSleep = 3

''' CAMERA FRAME RATE'''
fps = 30
