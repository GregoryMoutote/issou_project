import cv2
import matplotlib.pyplot as plt
import numpy as np
from calibration import ShapeDetection


class CalibrationTool:
    def __init__(self):
        self.matrix = []
        self.webcam = None
        self.pts1 = None
        self.pts2 = None
        self.M = None
        self.isDone = False

    def initCamera(self):
        self.webcam = cv2.VideoCapture(0)
        print("CAMERA INITIALISATION...")

    def closeCamera(self):
        if self.webcam is not None:
            self.webcam.release()
            print("CAMERA CLOSED...")

    def getPoints(self):
        self.shape_util = ShapeDetection.ShapeDetection()
        self.shape_util.initCamera()
        print("RECUPERATION DES POINTS...")
        #while len(self.matrix) != 4:
            #self.matrix = self.shape_util.detectBoard()
        self.matrix = self.shape_util.detectFromPicture()
        print(self.matrix)
        self.shape_util.closeCamera()

    def calcMatrix(self):
        self.initCamera()
        #_, img = self.webcam.read()

        img = cv2.imread("calibration/table2.png")


        rows, cols, ch = img.shape



        self.pts1 = np.float32([[self.matrix[0][0], self.matrix[0][1]], [self.matrix[3][0], self.matrix[3][1]],
                                [self.matrix[1][0], self.matrix[1][1]], [self.matrix[2][0], self.matrix[2][1]]])

        print("Premiere Matrice : " + '\n' + str(self.pts1))

        self.triPoint()

        print("Seconde Matrice : " + '\n' + str(self.pts1))


        self.pts2 = np.float32([[0, 0], [cols, 0], [0, rows], [cols, rows]])

        self.M = cv2.getPerspectiveTransform(self.pts1, self.pts2)

        self.isDone = True
        self.closeCamera()

    # def triPoint(self):
    #     firstSum = self.matrix[0][0] + self.matrix[0][1]
    #     secondSum = self.matrix[1][0] + self.matrix[1][1]
    #     thirdSum = self.matrix[2][0] + self.matrix[2][1]
    #     fourthSum = self.matrix[3][0] + self.matrix[3][1]
    #     points = [self.matrix[0], self.matrix[1],
    #               self.matrix[2], self.matrix[3]]
    #
    #     print("Points = " + str(points))
    #     print("Pts1 = " + str(self.pts1))
    #
    #     if firstSum < secondSum & firstSum < thirdSum & firstSum < fourthSum:
    #         self.pts1[0] = points[0]
    #     elif secondSum < firstSum & secondSum < thirdSum & secondSum < fourthSum:
    #         self.pts1[0] = points[1]
    #     elif thirdSum < firstSum & thirdSum < secondSum & thirdSum < fourthSum:
    #         self.pts1[0] = points[2]
    #     else:
    #         self.pts1[0] = points[3]
    #
    #     if firstSum > secondSum & firstSum > thirdSum & firstSum > fourthSum:
    #         self.pts1[3] = points[0]
    #         del points[0]
    #     elif secondSum > firstSum & secondSum > thirdSum & secondSum > fourthSum:
    #         self.pts1[3] = points[1]
    #         del points[1]
    #     elif thirdSum > firstSum & thirdSum > secondSum & thirdSum > fourthSum:
    #         self.pts1[3] = points[2]
    #         del points[2]
    #     else:
    #         self.pts1[3] = points[3]
    #         del points[3]

    def triPoint(self):
        tabSum = [self.matrix[0][0] + self.matrix[0][1], self.matrix[1][0] + self.matrix[1][1],
                  self.matrix[2][0] + self.matrix[2][1], self.matrix[3][0] + self.matrix[3][1]]
        pointOrder = []
        tabIndex = [0,1,2,3]
        minIndex = tabSum.index(min(tabSum))
        maxIndex = tabSum.index(max(tabSum))
        print("Max Index " + str(maxIndex))
        print("Min Index " + str(minIndex))
        pointOrder.append(minIndex)
        tabIndex.pop(tabIndex.index(minIndex))
        tabIndex.pop(tabIndex.index(maxIndex))

        print(tabIndex)

        if self.matrix[tabIndex[0]][0]>self.matrix[tabIndex[1]][0] :
            pointOrder.append(tabIndex[0])
            pointOrder.append(tabIndex[1])

        else:
            pointOrder.append(tabIndex[1])
            pointOrder.append(tabIndex[0])


        pointOrder.append(maxIndex)
        self.pts1 = np.float32([[self.matrix[pointOrder[0]][0], self.matrix[pointOrder[0]][1]],
                            [self.matrix[pointOrder[1]][0], self.matrix[pointOrder[1]][1]],
                            [self.matrix[pointOrder[2]][0], self.matrix[pointOrder[2]][1]],
                            [self.matrix[pointOrder[3]][0], self.matrix[pointOrder[3]][1]]])

        print(pointOrder)



    def calibratePicture(self, img, preview: bool):
        rows, cols, ch = img.shape
        dst = cv2.warpPerspective(img, self.M, (cols, rows))
        if preview:
            plt.subplot(121), plt.imshow(img), plt.title('Input')
            plt.subplot(122), plt.imshow(dst), plt.title('Output')
            plt.show()
        return dst

    def calibratePoint(self, coord):
        coord_matrix = np.float32([[coord[0]], [coord[1]], [1]])
        result_matrix = np.matmul(self.M, coord_matrix)
        return result_matrix[0][0] / result_matrix[2][0], result_matrix[1][0] / result_matrix[2][0]
