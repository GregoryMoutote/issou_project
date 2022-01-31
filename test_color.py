
# Python code for Multiple Color Detection


import numpy as np
import cv2

class color_util :
    def __init__(self):
        self.colorPoint = []

    def detect_color(self):
        # Image fixe
        #image = cv2.imread("tableau.jpg")
        #image = cv2.resize(image, (1500,675))

        #FIN IMAGE FIXE

        # Webcam
        cap = cv2.VideoCapture(0)
        while(len(self.colorPoint)!=4):
            _,image = cap.read()
        # FIN WEBCAM


            arrayPoint = []
            # Start a while loop

            # Convert the imageFrame in
            # BGR(RGB color space) to
            # HSV(hue-saturation-value)
            # color space
            hsvFrame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

            # Set range for red color and
            # define mask
            red_lower = np.array([136, 87, 111], np.uint8)
            red_upper = np.array([255, 139, 150], np.uint8)
            red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)


            # Morphological Transform, Dilation
            # for each color and bitwise_and operator
            # between imageFrame and mask determines
            # to detect only that particular color
            kernal = np.ones((5, 5), "uint8")

            # For red color
            red_mask = cv2.dilate(red_mask, kernal)
            res_red = cv2.bitwise_and(image, image,
                                        mask = red_mask)


            # Creating contour to track red color
            contours, hierarchy = cv2.findContours(red_mask,
                                                    cv2.RETR_TREE,
                                                    cv2.CHAIN_APPROX_SIMPLE)

            self.colorPoint = []
            for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area > 300):
                    x, y, w, h = cv2.boundingRect(contour)
                    self.colorPoint.append((x,y))
                    image = cv2.rectangle(image, (x, y),
                                                (x + w, y + h),
                                                (0, 0, 255), 2)

                    cv2.putText(image, "Red Colour", (x, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                                (0, 0, 255))


            #pts1 = np.float32((arrayPoint[0],arrayPoint[1],arrayPoint[2]))
            # Program Termination
            cv2.imshow("Multiple Color Detection in Real-TIme", image)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()