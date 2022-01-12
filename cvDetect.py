import cv2

webcam = cv2.VideoCapture(0)

while 1 :
    _, img = webcam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



    # setting threshold of gray image
    threshold, _ = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)



    cv2.imshow('Flux Camera', threshold)

    i = 0


    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()