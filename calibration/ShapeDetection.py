import cv2

class ShapeDetection():


    def __init__(self):
        self.corners = []
        self.isDisplaying = False
        self.webcam = None

    def initCamera(self):
        self.webcam = cv2.VideoCapture(0)
        print("CAMERA INITIALISATION...")


    def closeCamera(self):
        if self.webcam is not None:
            self.webcam.release()
            print("CAMERA CLOSED...")

    def detectBoard(self):
        self.corners = []
        if self.webcam is not None:

            _, img = self.webcam.read()

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

            contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            contourSize = []

            #Detection de la plus grosse forme
            for contour in contours:
                contourSize.append(cv2.contourArea(contour))
            if len(contourSize)>0:
                index = contourSize.index(max(contourSize))


                approx = cv2.approxPolyDP(contours[index], 0.01 * cv2.arcLength(contours[index], True), True)

                cv2.drawContours(img, [contours[index]], 0, (0, 0, 255), 5)

                corner = approx.ravel()

                i = 0

                ##Detection des coordonnees du contour
                for j in corner:
                    if (i % 2 == 0):
                        x = corner[i]
                        y = corner[i + 1]

                        self.corners.append((x,y))

                        if (self.isDisplaying):
                            string = str(x) + " " + str(y)

                            if (i != 0):
                                cv2.putText(img, string, (x, y),
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
                    i = i + 1


                if (self.isDisplaying):
                    while 1:
                        cv2.imshow('Flux Camera', img)

                        if cv2.waitKey(10) & 0xFF == ord('q'):
                            break
                return self.corners
        else:
            print("FLUX CAMERA NON INITIALISE, AUCUN POINT RETOURNE...")

    def detectFromPicture(self,):
        img = cv2.imread("calibration/table.jpg")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        contourSize = []

        # Detection de la plus grosse forme
        for contour in contours:
            contourSize.append(cv2.contourArea(contour))

        if len(contourSize)>0:
            index = contourSize.index(max(contourSize))

            approx = cv2.approxPolyDP(contours[index], 0.01 * cv2.arcLength(contours[index], True), True)

            cv2.drawContours(img, [contours[index]], 0, (0, 0, 255), 5)

            corner = approx.ravel()

            i = 0

            ##Detection des coordonnees du contour
            for j in corner:
                if (i % 2 == 0):
                    x = corner[i]
                    y = corner[i + 1]

                    self.corners.append((x, y))

                    if (self.isDisplaying):
                        string = str(x) + " " + str(y)

                        if (i != 0):
                            cv2.putText(img, string, (x, y),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
                i = i + 1

            if (self.isDisplaying):
                while 1:
                    cv2.imshow('Flux Camera', img)

                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break
            return self.corners
