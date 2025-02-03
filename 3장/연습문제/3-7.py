import cv2 as cv
import numpy as np

img = cv.imread('image/gguggury.jpg')
img = cv.resize(img, dsize=(0,0), fx=0.6, fy=0.6)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

img2 = cv.imread('sortImage.jpg')
img2 = cv.resize(img2, dsize=(0,0), fx=0.4, fy=0.4)
gray1 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
cv.putText(gray,'Sort',(10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
cv.imshow('Original', gray)

#가우시안 스무딩
smooth=np.hstack((cv.GaussianBlur(gray, (5,5),0.0),cv.GaussianBlur(gray,(9,9),0.0), cv.GaussianBlur(gray,(15,15),0.0)))
smooth2 = np.hstack((cv.medianBlur(gray,5),cv.medianBlur(gray,9),cv.medianBlur(gray,15)))
smooth3 = np.hstack((cv.medianBlur(gray1,5),cv.medianBlur(gray1,9),cv.medianBlur(gray1,15)))
cv.imshow('Smooth', smooth)
cv.imshow('Smooth2',smooth2)
cv.imshow('Smooth3',smooth3)
cv.waitKey()
cv.destroyAllWindows()

