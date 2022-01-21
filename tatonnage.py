"""import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


rows,cols = img.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv.warpAffine(img,M,(cols,rows))
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()

img = cv.imread('Logo.png')
rows,cols,ch = img.shape
pts1 = np.float32([[0,0],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[400,400]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
"""
"""

import cv2
import numpy as np

def find_centroids(dst):
    ret, dst = cv2.threshold(dst, 0.01 * dst.max(), 255, 0)
    dst = np.uint8(dst)

    # find centroids
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
    # define the criteria to stop and refine the corners
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100,
                0.001)
    corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),
              (-1,-1),criteria)
    return corners

image = cv2.imread("tableau.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 2, 3, 0.04)

dst = cv2.dilate(dst, None)

# Threshold for an optimal value, it may vary depending on the image.
# image[dst > 0.01*dst.max()] = [0, 0, 255]

# Get coordinates
corners= find_centroids(dst)
# To draw the corners
for corner in corners:
    image[int(corner[1]), int(corner[0])] = [0, 0, 255]
cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
import numpy as np
import cv2

img = cv2.imread('tableauBenjaminus.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,127,255,1)

contours,h = cv2.findContours(thresh,1,2)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    print(len(approx))
    if len(approx)==5:
        print("pentagon")
        cv2.drawContours(img,[cnt],0,255,-1)
    elif len(approx)==3:
        print("triangle")
        cv2.drawContours(img,[cnt],0,(0,255,0),-1)
    elif len(approx)==4:
        print("square")
        cv2.drawContours(img,[cnt],0,(0,0,255),-1)
    elif len(approx) == 9:
        print("half-circle")
        cv2.drawContours(img,[cnt],0,(255,255,0),-1)
    elif len(approx) > 15:
        print("circle")
        cv2.drawContours(img,[cnt],0,(0,255,255),-1)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""
"""
import cv2
import numpy as np
img = cv2.imread("tableauBenjaminus.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_range = np.array([0,0,0])
upper_range = np.array([255,120,120])
mask = cv2.inRange(hsv, lower_range, upper_range)

cv2.imshow("image", img)
cv2.imshow("Mask", mask)
cv2.waitKey(0)

cv2.destroyAllWindows()
"""





import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('tableau.png')
rows,cols,ch = img.shape
pts1 = np.float32([[50,50],[2000,50],[50,1200],[2000,1100]])
pts2 = np.float32([[50,50],[1870,50],[50,1030],[1870,1030]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(2100,1300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()