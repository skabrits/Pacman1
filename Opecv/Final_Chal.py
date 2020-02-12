import sys

import cv2 as cv
import numpy as np
from sympy import Point

image = cv.imread('final_challenge.png')
imager = cv.imread('final_challenge.png')
np.set_printoptions(threshold=sys.maxsize)

side_len = 30

lr = np.array([0,0,20])
hr = np.array([20,200,200])
msk = cv.inRange(image, lr, hr)
print(type(msk))
# cv.imshow('ms',msk)
a1, ct, hr = cv.findContours(msk, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
ind = 0
l0 = 0
for i in range(len(ct)):
    if l0<len(ct[i]):
        l0 = len(ct[i])
        ind = i

lrr = np.array([0,50,50])
hrr = np.array([20,255,255])
mskr = cv.inRange(image, lrr, hrr)
print(type(mskr))
# cv.imshow('ms',mskr)
a1r, ctr, hrr = cv.findContours(mskr, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
indr = 0
l0r = 0
for ir in range(len(ctr)):
    if l0r<len(ctr[ir]):
        l0r = len(ctr[ir])
        indr = ir

# cv.imshow('yc', cv.drawContours(image, ctr, indr, (0,255,0),3))

temp_red = cv.imread('final_challenge_red.png')
temp_yellow = cv.imread('final_challenge_yellow.png')

sift = cv.xfeatures2d.SIFT_create()

kp1, ds1 = sift.detectAndCompute(temp_red,None)
kp2, ds2 = sift.detectAndCompute(image, msk)

bf = cv.BFMatcher()

matches = bf.knnMatch(ds1,ds2,k=2)
good = []
poi = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
        poi.append(kp2[m.queryIdx].pt)

coolpoi = np.array(poi)
mp = np.average(coolpoi, axis=0)
deviation = np.std(coolpoi, axis=0)
print(mp)

msk1 = np.zeros(image.shape, np.uint8)
msk1[int(mp[0]-side_len):int(mp[0]+side_len), int(mp[1]-side_len):int(mp[1]+side_len)] = image[int(mp[0]-side_len):int(mp[0]+side_len), int(mp[1]-side_len):int(mp[1]+side_len)]

print(type(msk1))
ret,thresh1 = cv.threshold(cv.cvtColor(msk1.copy(), cv.COLOR_BGR2GRAY), 100, 255, cv.THRESH_BINARY)


kp1r, ds1r = sift.detectAndCompute(temp_yellow,None)
kp2r, ds2r = sift.detectAndCompute(image, mskr)

bf = cv.BFMatcher()

matchesr = bf.knnMatch(ds1r,ds2r,k=2)
goodr = []
poir = []
for mr,nr in matchesr:
    if mr.distance < 0.75*nr.distance:
    # if True:
        goodr.append([mr])
        poir.append(kp2r[mr.queryIdx].pt)

coolpoir = np.array(poir)
mpr = np.average(coolpoir, axis=0)
deviationr = np.std(coolpoir, axis=0)
print("    ",coolpoir)
for cor in poir:
    if np.math.sqrt((cor[0]-mpr[0])**2+(cor[1]-mpr[1])**2) > np.math.sqrt(deviation[0]**2+deviation[1]**2):
        poir.remove(cor)
coolpoir = np.array(poir)
print("    ",coolpoir)
mpr = np.average(coolpoir, axis=0)
print(mpr)


msk1r = np.zeros(imager.shape, np.uint8)
msk1r[int(mpr[1]-side_len):int(mpr[1]+side_len), int(mpr[0]-side_len):int(mpr[0]+side_len)] = imager[int(mpr[1]-side_len):int(mpr[1]+side_len), int(mpr[0]-side_len):int(mpr[0]+side_len)]

print(type(msk1r))
ret,thresh1r = cv.threshold(cv.cvtColor(msk1r.copy(), cv.COLOR_BGR2GRAY), 220, 255, cv.THRESH_BINARY)


cv.imshow('PreFINAL',thresh1r)

a2, ctf, hrf = cv.findContours(thresh1, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

ctf.sort(key=len)
ctf = ctf[::-1]
ctf1 = ctf.copy()
j = 0
for i in range(len(ctf1)):
    peri = cv.arcLength(ctf1[i], True)
    approx = cv.approxPolyDP(ctf1[i], 0.04 * peri, True)
    if len(approx) > 5:
        ctf = np.delete(ctf, j)
        j -= 1
    j += 1

a2, ctfr, hrf = cv.findContours(thresh1r, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

ctfr.sort(key=len)
ctfr = ctfr[::-1]
ctf1r = ctfr.copy()
j = 0
for i in range(len(ctf1r)):
    peri = cv.arcLength(ctf1r[i], True)
    approx = cv.approxPolyDP(ctf1r[i], 0.04 * peri, True)
    if len(approx) > 5:
        ctfr = np.delete(ctfr, j)
        j -= 1
    j += 1

cv.imshow('FINAL',cv.drawContours(cv.drawContours(image, ctf, 0, (0,255,0),3), ctfr, 0, (0,255,0),3))

img_match = cv.drawMatchesKnn(temp_yellow, kp1r, imager, kp2r, goodr, None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv.imshow("MyMatch", img_match)

# cv.imshow('FINAL',cv.rectangle(image,(int(mp[0]-10),int(mp[1]-20)),(int(mp[0]+30),int(mp[1]+20)),(0,255,0),3))
# img_match = cv.drawMatchesKnn(temp_red, kp1, image, kp2, matches, None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
# cv.imshow("MyMatch", img_match)

cv.waitKey(0)
cv.destroyAllWindows()