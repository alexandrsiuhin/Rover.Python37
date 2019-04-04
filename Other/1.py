import cv2

print(cv2.__version__)
capture = cv2.VideoCapture(0)

while (True):
    # Frame Acquisition
    availability = False
    availability, frame = capture.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
