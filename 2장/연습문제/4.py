import cv2 as cv
import sys

img = cv.imread('image/gguggury.jpg')

if img is None :
    sys.exit('이미지를 찾을 수 없음')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #컬러 영상을 명암으로 변환!

gray_small = []

size = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

for element in size :
    gray_small.append(cv.resize(gray, dsize=(0,0), fx=element, fy=element)) 

for i in range(10) :
   cv.imshow('Color image'+str(i), gray_small[i]) 

cv.waitKey()
cv.destroyAllWindows()
