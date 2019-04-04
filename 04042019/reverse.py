import cv2
import numpy as np
import serial
from Support_Code.Camera_filter import filterCamera
from Support_Code.olddrowContours import contourCoordinat

frameWeight = 640
frameHigh = 480

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frameHigh)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, frameWeight)

serialConnection = serial.Serial("COM4", 9600)  # change ACM number as found from ls /dev/tty/ACM*
cont = dict()
backcount = 0
while True:
    flag, frame = cap.read()

    CLOSE = filterCamera(frame)

    if np.array_equal(CLOSE, [0]):

##        cv2.imshow('frame', frame)
        pass

    else:

        contours, hierarchy = cv2.findContours(CLOSE, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        Return = contourCoordinat(contours, hierarchy, frame)
        maxx = Return[0]
        minx = Return[1]
        maxy = Return[2]
        miny = Return[3]
        frame = Return[4]
        ptxup = Return[5]
        ptyr = Return[6]
        ptxdown = Return[7]
        ptyl = Return[8]

        cont = dict()
        pt = dict()

        for i in range(len(maxx)):
            cont[i] = [maxx[i], minx[i], maxy[i], miny[i]]
            pt[i] = [ptxup[i], ptyr[i], ptxdown[i], ptyl[i]]
            cv2.putText(frame, str(i+1)+' tree', (ptxup[i], miny[i]+15), font, 1, (0, 255, 255))

        for j in range(len(cont)):
            # Определение положения контуров по оси х
            if (cont[j][0] > frameWeight / 2) and (cont[j][1] > frameWeight / 2):
                cont[j].append(1)  # Правый
            elif (cont[j][0] < frameWeight / 2) and (cont[j][1] < frameWeight / 2):
                cont[j].append(2)  # Левый
            else:
                cont[j].append(3)  # Центральный
            # Определение положения контуров по оси у
            if cont[j][2] < frameHigh / 3:
                cont[j].append(1)  # Дальий
            elif (cont[j][2] > frameHigh / 3) and (cont[j][2] < frameHigh*0.75):
                cont[j].append(2)  # Рабочий объект
            else:
                cont[j].append(3)  # Нарушение габарита

        FG = False      # флаг отвечающий за пересечение габаритов
        FWR = False     # флаг отвечающий за наличие объекта справа
        FWL = False     # флаг отвечающий за наличие объекта слева
        FWC = False     # флаг отвечающтй за наличие объекта посередине
        FXWL = False    # флаг отвечающий за пересечение объектом левой границы
        FXWR = False    # флаг отвечающий за пересечение объектом правой границы
        FDR = False     # флаг отвечающий за наличие объекта справа в дальней области
        FDL = False     # флаг отвечающий за наличие объекта слева в дальней области
        FDC = False     # флаг отвечающтй за наличие объекта посередине в дальней области

        for k in range(len(cont)):
            if cont[k][5] == 3:
                FG = True
                if cont[k][1] < (cont[k][2]*0.18+frameWeight-30) - (round(frameHigh * 0.18)):
                            FXWR = True
                if cont[k][0] > (cont[k][2])*(-0.18)+30 + (round(frameHigh * 0.18)):
                            FXWL = True

            if FG is True and FXWL is True and FXWR is True:
##                serialConnection.write(b'Stop./r')
                backcount = backcount + 1
                if backcount == 3:
                    print('BackwardFull')
                    serialConnection.write(b'BackwardSlow./r')
                    backcount = 0
            else:
                if cont[k][5] == 2:     # проверка объектов в рабочей области
                    if cont[k][4] == 1:
                        FWR = True
                        if cont[k][1] < (pt[k][3]*0.18+610) - (round(frameHigh * 0.18)) \
                                or pt[k][2] < (cont[k][2])*(-0.18) + 610 - (round(frameHigh * 0.18)) \
                                or pt[k][0] < (cont[k][3])*(-0.18) + 610 - (round(frameHigh * 0.18)):
                            FXWR = True
                    elif cont[k][4] == 2:
                        FWL = True
                        if cont[k][0] > (pt[k][1])*(-0.18) + 30 + (round(frameHigh * 0.18)) \
                                or pt[k][2] > (cont[k][2])*(-0.18) + 30 + (round(frameHigh * 0.18)) \
                                or pt[k][0] > (cont[k][3])*(-0.18) + 30 + (round(frameHigh * 0.18)):
                            FXWL = True
                    elif cont[k][4] == 3:
                        FWC = True
                elif cont[k][5] == 1:   # проверка объектов в дальней области
                    if cont[k][4] == 1:
                        FDR = True
                    elif cont[k][4] == 2:
                        FDL = True
                    elif cont[k][4] == 3:
                        FDC = True

        if FWR is True and FWL is True and FXWR is False and FXWL is False and FWC is False:
            print('ForwardFull')
            serialConnection.write(b'ForwardFull./r')
        if FWR is False and FWL is False and FXWR is False and FXWL is False and FWC is False:
            print('ForwardFull')
            serialConnection.write(b'ForwardFull./r')
        if FWR is True and FWL is True and FXWR is False and FXWL is False and FWC is True:
##            serialConnection.write(b'Stop./r')
            backcount = backcount + 1
            if backcount == 3:
                print('BackwardFull')
                serialConnection.write(b'BackwardSlow./r')
                backcount = 0
        if FWR is True and FWL is True and FXWR is False and FXWL is True and FWC is False:
            print('RightFull')
            serialConnection.write(b'LeftFull./r')
        if FWR is True and FWL is True and FXWR is True and FXWL is False and FWC is False:
            print('LeftFull')
            serialConnection.write(b'RightFull./r')
        if FWR is True and FWL is False and FXWR is True and FWC is False:
            print('LeftFull')
            serialConnection.write(b'RightFull./r')
        if FWR is True and FWL is False and FXWR is False and FWC is False:
            print('ForwardFull')
            serialConnection.write(b'ForwardFull./r')
        if FWR is False and FWL is True and FXWL is True and FWC is False:
            print('RightFull')
            serialConnection.write(b'LeftFull./r')
        if FWR is False and FWL is True and FXWR is False and FWC is False:
            print('ForwardFull')
            serialConnection.write(b'ForwardFull./r')
        if FDC is True or FWC is True:
            print('Stop')
            if FWR is False and FWL is False:
                print('RightFull')
                serialConnection.write(b'LeftFull./r')
            if FWR is False and FWL is True:
                print('RightFull')
                serialConnection.write(b'LeftFull./r')
            if FWR is True and FWL is False:
                print('LeftFull')
                serialConnection.write(b'RightFull./r')
            if FWR is True and FWL is True:
##                serialConnection.write(b'Stop./r')
                backcount = backcount + 1
                if backcount == 3:
                    print('BackwardFull')
                    serialConnection.write(b'BackwardSlow./r')
                    backcount = 0

    if True:
        # Оформление
        y = 0
        cv2.line(frame, (round(frameHigh * 0.18 * (2 / 3)+30), round(frameHigh / 3)),
                 (frameWeight - round(frameHigh * 0.18 * (2 / 3)+30), round(frameHigh / 3)), (0, 255, 0), 1, 4)
        cv2.line(frame, (round((frameHigh / 4) * 0.18)+30, round(frameHigh - (frameHigh / 4))),
                 (frameWeight - round((frameHigh / 4) * 0.18)-30, round(frameHigh - (frameHigh / 4))), (0, 255, 0), 1, 8)
        cv2.line(frame, (round(frameHigh * 0.18+30), 0), (30, frameHigh), (0, 255, 0), 1)
        cv2.line(frame, (round((-frameHigh * 0.18-30) + frameWeight), 0), (frameWeight-30, frameHigh), (0, 255, 0), 1)
        cv2.putText(frame, 'Working area',
                    (round(frameHigh * 0.18 * (2 / 3)+30), round(frameHigh / 3) + 12), font, 1, (0, 255, 255))
        cv2.putText(frame, 'Overall dimensions',
                    (round((frameHigh / 4) * 0.18+30), round(frameHigh - (frameHigh / 4)) + 12), font, 1, (0, 255, 255))
        
    cv2.imshow('frame', frame)
    t=0
    if cv2.waitKey(1) & 0xFF == ord('q'):
##        serialConnection.write(b'Stop./r')
        while t<1000:
            t=t+1
            serialConnection.write(b'Stop./r')
            print(t)
        break



print(cont)
cap.release()
cv2.destroyAllWindows()
serialConnection.write(b'BackwardFull./r')
