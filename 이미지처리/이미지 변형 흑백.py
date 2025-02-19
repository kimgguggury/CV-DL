# #이미지를 흑백으로 읽음

# import cv2 as cv
# img = cv.imread('gguZam.jpg', cv.IMREAD_GRAYSCALE)
# cv.imshow('img', img)
# cv.waitKey(0)
# cv.destroyAllWindows()


#불러온 이미지를 흑백으로 변경

import cv2 as cv

img = cv.imread('gguZam.jpg')

dst = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('img', img)
cv.imshow('gray', dst)
cv.waitKey(0)
cv.destroyAllWindows()
