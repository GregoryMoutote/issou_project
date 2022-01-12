from color_thread import colorThread
import keyboard

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


detection = colorThread()
detection.start()
while 1:
    if len(detection.colorClass.colorPoint) != 0:
        print(detection.colorClass.colorPoint)
    if keyboard.is_pressed("q"):
        break
    if len(detection.colorClass.colorPoint) >= 4:
        break
if len(detection.colorClass.colorPoint) >= 4:

    #img = cv.imread('tableau.png')
    #rows, cols, ch = img.shape
    pts1 = np.float32([[0, 0], [0, 0], [0, 0], [0, 0]])
    firstSum = detection.colorClass.colorPoint[0][0] + detection.colorClass.colorPoint[0][1]
    secondSum = detection.colorClass.colorPoint[1][0] + detection.colorClass.colorPoint[1][1]
    thirdSum = detection.colorClass.colorPoint[2][0] + detection.colorClass.colorPoint[2][1]
    fourthSum = detection.colorClass.colorPoint[3][0] + detection.colorClass.colorPoint[3][1]

    points = [detection.colorClass.colorPoint[0],detection.colorClass.colorPoint[1],
              detection.colorClass.colorPoint[2],detection.colorClass.colorPoint[3]]

    if firstSum < secondSum & firstSum < thirdSum & firstSum < fourthSum:
        pts1[0] = points[0]
        del points[0]
    elif secondSum < firstSum & secondSum < thirdSum & secondSum < fourthSum:
        pts1[0] = points[1]
        del points[1]
    elif thirdSum < firstSum & thirdSum < secondSum & thirdSum < fourthSum:
        pts1[0] = points[2]
        del points[2]
    else:
        pts1[0] = points[3]
        del points[3]

    if firstSum > secondSum & firstSum > thirdSum & firstSum > fourthSum:
        pts1[3] = points[0]
        del points[0]
    elif secondSum > firstSum & secondSum > thirdSum & secondSum > fourthSum:
        pts1[3] = points[1]
        del points[1]
    elif thirdSum > firstSum & thirdSum > secondSum & thirdSum > fourthSum:
        pts1[3] = points[2]
        del points[2]
    else:
        pts1[3] = points[3]
        del points[3]

    if points[0][0] < points[1][0]:
        pts1[1] = points[1][0]
        pts1[2] = points[0][0]
    else:
        pts1[2] = points[1][0]
        pts1[1] = points[0][0]

    print(pts1)

    pts2 = np.float32([[50, 50], [1870, 50], [50, 1030], [1870, 1030]])
    M = cv.getPerspectiveTransform(pts1, pts2)
    dst = cv.warpPerspective(img, M, (1870, 1030))
    plt.subplot(121), plt.imshow(img), plt.title('Input')
    plt.subplot(122), plt.imshow(dst), plt.title('Output')
    plt.show()