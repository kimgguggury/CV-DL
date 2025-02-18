# #영역을 잘라서 새로운 윈도우(창)에 표시

# import cv2 as cv

# img = cv.imread('gguHa1.jpg')
# #현재 이미지는 (667, 500, 3)의 크기다.

# crop = img[200:300, 100:400] #세로 기준 200 : 300 까지, 가로 기준 100 : 400 까지 자름

# cv.imshow('img', img) #원본 이미지
# cv.imshow('crop', crop) #잘린 이미지
# cv.waitKey(0)
# cv.destroyAllWindows()

#영역을 잘라서 기존 윈도우에 표시

import cv2 as cv

img = cv.imread('gguHa1.jpg')
#현재 이미지는 (667, 500, 3)의 크기다.

crop = img[200:300, 100:400] #세로 기준 200 : 300 까지, 가로 기준 100 : 400 까지 자름
img[200:300, 200:500] = crop
cv.imshow('img', img) #원본 이미지

cv.waitKey(0)
cv.destroyAllWindows()