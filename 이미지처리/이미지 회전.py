# #시계 방향 90도 회전

# import cv2 as cv
# img = cv.imread('gguZam.jpg')

# rotate_90 = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)

# cv.imshow('img', img)
# cv.imshow('rotate_90', rotate_90)
# cv.waitKey(0)
# cv.destroyAllWindows()

#시계 방향 180도 회전

# import cv2 as cv
# img = cv.imread('gguZam.jpg')

# rotate_180 = cv.rotate(img, cv.ROTATE_180)

# cv.imshow('img', img)
# cv.imshow('rotate_180', rotate_180)
# cv.waitKey(0)
# cv.destroyAllWindows()

#시계 반대 방향 90도 회전 (시계 방향 270도 회전)

import cv2 as cv
img = cv.imread('gguZam.jpg')

rotate_270 = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)

cv.imshow('img', img)
cv.imshow('rotate_180', rotate_270)
cv.waitKey(0)
cv.destroyAllWindows()