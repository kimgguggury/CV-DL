import cv2 as cv
import numpy as np

img = cv.imread('newspaper.jpg')
width, height = 640, 240 #가로 크기 640, 세로 크기 240 으로 결과물 출력

src = np.array([[511, 359], [1005,347], [1115, 567], [461, 575]], dtype=np.float32)
dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

matrix = cv.getPerspectiveTransform(src, dst) #Matrix 얻어옴
result = cv.warpPerspective(img, matrix, (width, height))

cv.imshow('img', img)
cv.imshow('result', result)
cv.waitKey(0)
cv.destroyAllWindows()