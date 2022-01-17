import cv2

webcam = cv2.VideoCapture(0)

while 1 :
    _, img = webcam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(
        threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contourSize = []
    for contour in contours :
        contourSize.append(cv2.contourArea(contour))

    index = contourSize.index(max(contourSize))



    approx = cv2.approxPolyDP(contours[index], 0.01 * cv2.arcLength(contours[index], True), True)

    cv2.drawContours(img, [contours[index]], 0, (0, 0, 255), 5)

    contour_corner = []

    corner = approx.ravel()
    i = 0

    for j in corner:
        if (i % 2 == 0):
            x = corner[i]
            y = corner[i + 1]

            # String containing the co-ordinates.
            string = str(x) + " " + str(y)
            contour_corner.append(string)

            if (i != 0):
                # text on remaining co-ordinates.
                cv2.putText(img, string, (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
        i = i + 1
    print(contour_corner)

    cv2.imshow('Flux Camera', img)



    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()