import cv2
import matplotlib.pyplot as plt
import numpy as np
from calibration import ShapeDetection

class CalibrationTool :
    def __init__(self):
        self.matrix = []
        self.webcam = None

    def initCamera(self):
        self.webcam = cv2.VideoCapture(0)
        print("CAMERA INITIALISATION...")


    def closeCamera(self):
        if self.webcam is not None:
            self.webcam.release()
            print("CAMERA CLOSED...")

    def calibrate(self):
        self.shape_util = ShapeDetection.ShapeDetection()
        self.shape_util.webcam = self.webcam
        print("RECUPERATION DES POINTS...")
        while len(self.matrix) != 4:
            self.matrix = self.shape_util.detectFromPicture()
        print (self.matrix)

    def showCalibratedPic(self):
        img = cv2.imread("calibration/table.jpg")

        rows, cols, ch = img.shape


        pts1 = np.float32([[self.matrix[0][0], self.matrix[0][1]],[self.matrix[3][0], self.matrix[3][1]],
                           [self.matrix[1][0], self.matrix[1][1]],[self.matrix[2][0], self.matrix[2][1]]])
        pts2 = np.float32([[0, 0], [1280, 0], [0, 720], [1280, 720]])

        M = cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(img, M, (cols,rows))
        plt.subplot(121), plt.imshow(img), plt.title('Input')
        plt.subplot(122), plt.imshow(dst), plt.title('Output')
        plt.show()