import cv2
import matplotlib.pyplot as plt
import numpy as np
from Calibration import ShapeDetection
import ctypes
from datetime import datetime
from Model.ScreenData import ScreenData


class CalibrationTool:
    def __init__(self):
        self.matrix = []
        self.image = None
        self.pts1 = None
        self.pts2 = None
        self.M = None
        self.is_done = False
        self.screen_width = 0

    """
    Met en place la matrice de transformation avec le calibrage
    """
    def setup(self, img: np.ndarray):
        screen = ScreenData()
        self.screen_width = screen.width
        self.image = img
        #print("TENTATIVE DE RECUPERATION DES POINTS...")
        is_done = self.get_points()
        if is_done:
            self.calc_matrix()
        return is_done

    """
    Initialise la caméra
    """
    def init_camera(self):
        self.webcam = cv2.VideoCapture(0)

    """
    Ferme la caméra s'il y en a une ouverte
    """
    def close_camera(self):
        if self.webcam is not None:
            self.webcam.release()

    """
    Insère les coins de l'image obtenue avec la caméra dans une matrice
    """ 
    def get_points(self):
        self.shape_util = ShapeDetection.ShapeDetection()
        self.matrix = self.shape_util.detect_from_picture(self.image)
        if self.matrix is not None and len(self.matrix)==4:
            return True
        else:
            return False

    """
    Calcule la matrice de transformation
    """
    def calc_matrix(self):
        if self.matrix is not None and len(self.matrix)>=4:
            rows, cols, ch = self.image.shape

            self.sort_points()

            self.pts2 = np.float32([[0, 0], [cols, 0], [0, rows], [cols, rows]])

            self.M = cv2.getPerspectiveTransform(self.pts1, self.pts2)

            self.is_done = True

    """
    Permet d'ordonner les points dans la matrice dans dans l'ordre coin haut gauche, coin haut droit,
    coin bas gauche et coin bas droit 
    """
    def sort_points(self):
        tab_sum = [self.matrix[0][0] + self.matrix[0][1], self.matrix[1][0] + self.matrix[1][1],
                  self.matrix[2][0] + self.matrix[2][1], self.matrix[3][0] + self.matrix[3][1]]
        point_order = []
        tab_index = [0, 1, 2, 3]
        min_index = tab_sum.index(min(tab_sum))
        max_index = tab_sum.index(max(tab_sum))
        point_order.append(min_index)
        tab_index.pop(tab_index.index(min_index))
        tab_index.pop(tab_index.index(max_index))

        if self.matrix[tab_index[0]][0] > self.matrix[tab_index[1]][0]:
            point_order.append(tab_index[0])
            point_order.append(tab_index[1])
        else:
            point_order.append(tab_index[1])
            point_order.append(tab_index[0])

        point_order.append(max_index)
        self.pts1 = np.float32([[self.matrix[point_order[0]][0], self.matrix[point_order[0]][1]],
                                [self.matrix[point_order[1]][0], self.matrix[point_order[1]][1]],
                                [self.matrix[point_order[2]][0], self.matrix[point_order[2]][1]],
                                [self.matrix[point_order[3]][0], self.matrix[point_order[3]][1]]])

    """
    Calibre une image selon la zone de jeu détectée
    """
    def calibrate_picture(self, img, preview: bool):
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

    """
    Calibre les coordonnées d'un point pour correspondre au coordonnées en jeu
    """
    def calibrate_point(self, coord):

        if self.M is not None:
            result_matrix = np.matmul(self.M, np.float32([coord[0],coord[1],1]))
            return self.screen_width - (result_matrix[0]/result_matrix[2]),result_matrix[1]/result_matrix[2]
        else:
            return coord[0], coord[1]

