import cv2


def Trapezium(__image, __width, __height, __pointColor, __pointRadius, __lineColor, __lineWidth, __textColor,
              __textFont, __bottomAngleA, __bottomAngleD, __topAngleB, __topAngleC):
    # Point Coordinates
    Ax = int(__width * __bottomAngleA)
    Ay = int(__height)
    A = (Ax, Ay)

    Bx = int(__width * __topAngleB)
    By = int(__height / 2)
    B = (Bx, By)

    Cx = int(__width * __topAngleC)
    Cy = int(__height / 2)
    C = (Cx, Cy)

    Dx = int(__width * __bottomAngleD)
    Dy = int(__height)
    D = (Dx, Dy)

    Ex = int(Ax + (Bx - Ax) / 2)
    Ey = int(Ay - (Ay - By) / 2)
    E = (Ex, Ey)

    Fx = int(Dx - (Dx - Cx) / 2)
    Fy = int(Dy - (Dy - Cy) / 2)
    F = (Fx, Fy)

    # Draw Line
    cv2.line(__image, A, B, __lineColor, __lineWidth)
    cv2.line(__image, C, D, __lineColor, __lineWidth)
    cv2.line(__image, B, C, __lineColor, __lineWidth)
    cv2.line(__image, A, D, __lineColor, __lineWidth)
    cv2.line(__image, E, F, __lineColor, __lineWidth)

    # Draw Circle
    cv2.circle(__image, A, __pointRadius, __pointColor, -1)
    cv2.circle(__image, B, __pointRadius, __pointColor, -1)
    cv2.circle(__image, C, __pointRadius, __pointColor, -1)
    cv2.circle(__image, D, __pointRadius, __pointColor, -1)
    cv2.circle(__image, E, __pointRadius, __pointColor, -1)
    cv2.circle(__image, F, __pointRadius, __pointColor, -1)

    # Draw Text
    cv2.putText(__image, "A", A, cv2.FONT_HERSHEY_SIMPLEX, __textFont, __textColor)
    cv2.putText(__image, "B", B, cv2.FONT_HERSHEY_SIMPLEX, __textFont, __textColor)
    cv2.putText(__image, "C", C, cv2.FONT_HERSHEY_SIMPLEX, __textFont, __textColor)
    cv2.putText(__image, "D", D, cv2.FONT_HERSHEY_SIMPLEX, __textFont, __textColor)
    cv2.putText(__image, "E", E, cv2.FONT_HERSHEY_SIMPLEX, __textFont, __textColor)
    cv2.putText(__image, "F", F, cv2.FONT_HERSHEY_SIMPLEX, __textFont, __textColor)
