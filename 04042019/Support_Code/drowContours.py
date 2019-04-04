import cv2


def contourCoordinat(contours, hierarchy, img):
    j = 0
    font = cv2.FONT_HERSHEY_PLAIN
    maxx = []
    minx = []
    maxy = []
    miny = []
    ptxup = []
    ptyr = []
    ptxdown = []
    ptyl = []
    while j <= len(hierarchy[0]) - 1:

        resultx = []
        resulty = []

        for i in range(len(contours[j])):
            resultx.append(contours[j][i][0][0])
            resulty.append(contours[j][i][0][1])

        S = (max(resultx) - min(resultx)) * (max(resulty) - min(resulty))

        if S > 1000:

            maxx.append(max(resultx))
            minx.append(min(resultx))
            maxy.append(max(resulty))
            miny.append(min(resulty))
            
            ptxup.append(resultx[resulty.index(min(resulty))])
            ptyr.append(resulty[resultx.index(max(resultx))])
            ptxdown.append(resultx[resulty.index(max(resulty))])
            ptyl.append(resulty[resultx.index(min(resultx))])
            cv2.line(img, (max(resultx), resulty[resultx.index(max(resultx))]),
                     (resultx[resulty.index(min(resulty))], min(resulty)), (0, 0, 255), 1)
            cv2.line(img, (resultx[resulty.index(min(resulty))], min(resulty)),
                     (min(resultx), resulty[resultx.index(min(resultx))]), (0, 0, 255), 1)
            cv2.line(img, (min(resultx), resulty[resultx.index(min(resultx))]),
                     (resultx[resulty.index(max(resulty))], max(resulty)), (0, 0, 255), 1)
            cv2.line(img, (resultx[resulty.index(max(resulty))], max(resulty)),
                     (max(resultx), resulty[resultx.index(max(resultx))]), (0, 0, 255), 1)
            

        else:
            pass

        j += 1

    return maxx, minx, maxy, miny, img, ptxup, ptyr, ptxdown, ptyl