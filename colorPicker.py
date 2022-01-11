import cv2
def ColorPicker(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  # checks mouse moves
        colorsBGR = image[y, x]
        colorsRGB=tuple(reversed(colorsBGR)) #Reversing the OpenCV BGR format to RGB format
        print("RGB Value at ({},{}):{} ".format(x,y,colorsRGB))
# Read an image
image = cv2.imread("unknown.png")
# Create a window and set Mousecallback to a function for that window
cv2.namedWindow('Color Picker')
cv2.setMouseCallback('Color Picker', ColorPicker)
# Do until esc pressed
while (1):
    cv2.imshow('Color Picker', image)
    if cv2.waitKey(10) & 0xFF == 27:
        break
# if esc is pressed, close all windows.
cv2.destroyAllWindows()