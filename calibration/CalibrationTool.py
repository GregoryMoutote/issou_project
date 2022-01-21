import cv2
import matplotlib.pyplot as plt
import numpy as np
from calibration import ShapeDetection
import ctypes



class CalibrationTool:
    def __init__(self):
        self.matrix = []
        self.image = None
        self.pts1 = None
        self.pts2 = None
        self.M = None
        self.isDone = False
        self.screenWidth = 0

    def setup(self, img:np.ndarray):
        screen = ctypes.windll.user32
        self.screenWidth = screen.GetSystemMetrics(0)
        self.image = img
        #print("TENTATIVE DE RECUPERATION DES POINTS...")
        isDone = self.getPoints()
        if isDone:
            self.calcMatrix()
        return isDone


    def initCamera(self):
        self.webcam = cv2.VideoCapture(0)
        #print("CAMERA INITIALISATION...")



    def closeCamera(self):
        if self.webcam is not None:
            self.webcam.release()
            #print("CAMERA CLOSED...")

    def getPoints(self):
        self.shape_util = ShapeDetection.ShapeDetection()
        #print("ANALYSE DE L'IMAGE...")
        self.matrix = self.shape_util.detectFromPicture(self.image)
        if self.matrix is not None and len(self.matrix)==4:
            return True
        else:
            #print("ECHEC DE RECUPERATION...")
            return False


    def calcMatrix(self):
        #print("CALCUL DE LA MATRICE...")
        if self.matrix is not None and len(self.matrix)>=4:
            rows, cols, ch = self.image.shape


            self.triPoint()

            self.pts2 = np.float32([[0, 0], [cols, 0], [0, rows], [cols, rows]])

            self.M = cv2.getPerspectiveTransform(self.pts1, self.pts2)

            self.isDone = True
            #print("MATRICE CALCULEE...")
        else:
            #print("MATRICE PAS DEFINI CORRECTEMENT")
            pass

    def triPoint(self):
        #print("TRI DES POINTS...")
        tabSum = [self.matrix[0][0] + self.matrix[0][1], self.matrix[1][0] + self.matrix[1][1],
                  self.matrix[2][0] + self.matrix[2][1], self.matrix[3][0] + self.matrix[3][1]]
        pointOrder = []
        tabIndex = [0, 1, 2, 3]
        minIndex = tabSum.index(min(tabSum))
        maxIndex = tabSum.index(max(tabSum))
        pointOrder.append(minIndex)
        tabIndex.pop(tabIndex.index(minIndex))
        tabIndex.pop(tabIndex.index(maxIndex))

        if self.matrix[tabIndex[0]][0] > self.matrix[tabIndex[1]][0]:
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

    def calibratePicture(self, img,  preview: bool):
        if self.M is not None:
            rows, cols, ch = img.shape
            dst = cv2.warpPerspective(img, self.M, (cols, rows))
            if preview:
                plt.subplot(121), plt.imshow(img), plt.title('Input')
                plt.subplot(122), plt.imshow(dst), plt.title('Output')
                plt.show()
            return dst
        else:
            return img

    def calibratePoint(self, coord):
        if self.M is not None:
            result_matrix = np.matmul(self.M, np.float32([[coord[0]], [coord[1]], [1]]))
            return (self.screenWidth-result_matrix[0][0]) / result_matrix[2][0], \
                   result_matrix[1][0] / result_matrix[2][0]
        else:
            return (coord[0],coord[1])

