import cv2 as cv
import numpy as np
image = cv.imread('demo_stop.jpg')

temp = cv.imread('stop_template.jpg')

sift = cv.xfeatures2d.SIFT_create()

kp1, ds1 = sift.detectAndCompute(temp,None)
kp2, ds2 = sift.detectAndCompute(image,None)

bf = cv.BFMatcher()

matches = bf.knnMatch(ds1,ds2,k=2)
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
img_match = cv.drawMatchesKnn(temp, kp1, image, kp2, good, None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv.imshow("MyMatch", img_match)

cv.waitKey(0)
cv.destroyAllWindows()