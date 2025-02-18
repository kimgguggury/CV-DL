#좌우 대칭

# import cv2 as cv

# img = cv.imread('gguZam.jpg')
# flip_horizontal = cv.flip(img, 1) # flipCode > 0좌우 대칭

# cv.imshow('img', img)
# cv.imshow('flip_horizontal', flip_horizontal)
# cv.waitKey(0)
# cv.destroyAllWindows()

# #상하 대칭
# import cv2 as cv

# img = cv.imread('gguZam.jpg')
# flip_vertical = cv.flip(img, 0) #flipCode == 0이면 상하 대칭

# cv.imshow('img', img)
# cv.imshow('flip_horizontal', flip_vertical)
# cv.waitKey(0)
# cv.destroyAllWindows()

#상하좌우 대칭
import cv2 as cv

img = cv.imread('gguZam.jpg')
flip_both = cv.flip(img, -1) #flipCode < 0이면 상하 대칭좌우

cv.imshow('img', img)
cv.imshow('flip_both', flip_both)
cv.waitKey(0)
cv.destroyAllWindows()