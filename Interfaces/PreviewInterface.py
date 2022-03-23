import pygame.font

from Interfaces.Interface import *
import cv2

class PreviewInterface(Interface):
    def __init__(self,screen_data, screen, detection):
        super().__init__(screen_data, screen)
        self.background = pygame.image.load("./Pictures/Interfaces/fond.png")
        self.detection = detection
        self.detection.close_camera()
        self.webcam = cv2.VideoCapture(0)
        self.webcam.set(3, 1280)
        self.webcam.set(4, 720)
        pygame.font.init()
        self.font = pygame.font.Font("./Fonts/Glitch.otf",70)
        self.ok_text = self.font.render("OK", True, (0, 255, 0))
        self.not_ok_text = self.font.render("NOT OK", True, (255,0, 0))
        self.displayed_text = self.ok_text
        self.show()
        self.loop()
        pygame.font.quit()


    def loop(self):
        go_on = True
        while go_on:
            self.show()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        go_on = False
                        self.detection.reopen_camera()
                        self.detection.init_hand_capture()


    def show(self):
        self.screen.blit(self.background, (0, 0))
        _, img = self.webcam.read()
        img = self.picture_draw_contour(img)
        self.screen.blit(self.convert_opencv_picture_to_pygame(img),(10,10))
        self.screen.blit(self.displayed_text,(1000,700))
        pygame.display.update()


    """
    Dessine les contours de la plus grande forme sur l'image
    """
    def picture_draw_contour(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contour_size = []

        # Detection de la plus grosse forme
        for contour in contours:
            contour_size.append(cv2.contourArea(contour))

        if len(contour_size) > 0:
            index = contour_size.index(max(contour_size))


        approx = cv2.approxPolyDP(contours[index], 0.01 * cv2.arcLength(contours[index], True), True)

        corner = approx.ravel()

        i = 0

        corners = []

        ##Detection des coordonnees du contour
        for j in corner:
            if i % 2 == 0:
                x = corner[i]
                y = corner[i + 1]

                corners.append((x, y))
            i = i+1

        if len(corners)==4:
            self.displayed_text = self.ok_text
            cv2.drawContours(img, contours[index], -1, (0, 255,0), 3)
        else:
            self.displayed_text = self.not_ok_text
            cv2.drawContours(img, contours[index], -1, (0, 0, 255), 3)


        return img

    """
    Converti une image obtenu par le biais d'OpenCV en image affichable sur Python
    """
    def convert_opencv_picture_to_pygame(self, img):
        opencv_image = img[:, :,::-1]
        shape = opencv_image.shape[1::-1]
        pygame_image = pygame.image.frombuffer(opencv_image.tostring(), shape, 'RGB')
        return pygame_image