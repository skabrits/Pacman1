import cv2 as cv
import numpy as np
# print(cv.__version__)
image = cv.imread('demo_cone.png')
# im1 = cv.imread('Opecv/demo_lane.png')
# image = cv.imread('stop_template.jpg',1)


hcv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
# imH = cv.cvtColor(im1, cv.COLOR_BGR2HSV)
# cv.line(image, (0,0),(338,510),(0,0,0),5)
# cv.circle(image, (150,250), 50, (0,0,255), 11)
# image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
# r, th = cv.threshold(image, 100, 255, cv.THRESH_BINARY)
# eg = cv.Canny(image, 200,255)
# cv.imshow('conet', th)
# cv.imshow('conee', eg)

lr = np.array([0,100,100])
hr = np.array([13,255,255])
msk = cv.inRange(hcv, lr, hr)
im, ct, hr = cv.findContours(msk, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(type(ct[1]))
ind = 0
l0 = 0
for i in range(len(ct)):
    if l0<len(ct[i]):
        l0 = len(ct[i])
        ind = i
icc = cv.drawContours(image, ct, ind, (0,255,0),3)
cv.imshow('conem', icc)

# x,y,w,h = cv.boundingRect(ct[ind])
# icb = cv.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
# cv.imshow('conebx', icb)
# cv.imwrite('cone_modified.jpg', image)


# rdd = cv.Canny(imH, 50, 150)
# rho = 1
# the = np.pi / 180
# minL = 200
# lines = cv.HoughLines(rdd, rho, the, minL)
for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv.line(imH,(x1,y1),(x2,y2),(0,0,255),2)
# cv.imshow('rd', imH)


# lr1 = np.array([0,0,100])
# hr1 = np.array([100,0,255])
# msk1 = cv.inRange(imH, lr1, hr1)
# ct1, hr1 = cv.findContours(msk1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#
# lr2 = np.array([1,100,100])
# hr2 = np.array([80,255,255])
# msk2 = cv.inRange(imH, lr2, hr2)
# ct2, hr2 = cv.findContours(msk2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#
# imm = cv.drawContours(imH, ct1, -1, (0,255,0),3)
# imm1 = cv.drawContours(imm, ct2, -1, (180,200,100),3)
# # cv.imshow('conem', imm1)
#
x1,y1,w1,h1 = cv.boundingRect(ct[0])
ilb = cv.rectangle(image,(x1,y1),(x1+w1,y1+h1),(0,255,0),2)
# # cv.imshow('conebx', ilb)
# cv.imwrite('lane_modified.jpg', ilb)


cv.waitKey(0)
cv.destroyAllWindows()
print(image.shape)
