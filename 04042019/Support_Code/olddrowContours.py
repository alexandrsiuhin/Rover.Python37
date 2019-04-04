import cv2


def contourCoordinat(contours, hierarchy, img):
    j = 0

    maxx = []
    minx = []
    maxy = []
    miny = []
    while j <= len(hierarchy[0]) - 1:

        resultx = []
        resulty = []

        for i in range(len(contours[j])):
            resultx.append(contours[j][i][0][0])
            resulty.append(contours[j][i][0][1])

        S = (max(resultx) - min(resultx)) * (max(resulty) - min(resulty))
        if S > 1000:
            cv2.rectangle(img, (max(resultx), max(resulty)), (min(resultx), min(resulty)), (0, 0, 255), 1)
            maxx.append(max(resultx))
            minx.append(min(resultx))
            maxy.append(max(resulty))
            miny.append(min(resulty))
        else:
            pass

        j += 1

    return maxx, minx, maxy, miny, img, 1, 2, 3, 4
