import cv2

webcam = cv2.VideoCapture(0)

while 1 :
    _, img = webcam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(
        threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    i = 0

    for contour in contours:

        if i == 0:
            i = 1
            continue

        taille = cv2.arcLength(contour, True)

        approx = cv2.approxPolyDP(contour, 0.01 * taille, True)

        M = cv2.moments(contour)

        if taille > 50:

            if M['m00'] != 0.0:
                x = int(M['m10'] / M['m00'])
                y = int(M['m01'] / M['m00'])

            else:
                cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)
                cv2.putText(img, 'circle', (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)


    cv2.imshow('Flux Camera', img)



    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()