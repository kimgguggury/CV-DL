#사다리꼴 이미지 펼치기
# import cv2 as cv
# import numpy as np

# img = cv.imread('newspaper.jpg')
# width, height = 640, 240 #가로 크기 640, 세로 크기 240 으로 결과물 출력

# src = np.array([[511, 359], [1005,347], [1115, 567], [461, 575]], dtype=np.float32)
# dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

# matrix = cv.getPerspectiveTransform(src, dst) #Matrix 얻어옴
# result = cv.warpPerspective(img, matrix, (width, height))

# cv.imshow('img', img)
# cv.imshow('result', result)
# cv.waitKey(0)
# cv.destroyAllWindows()

#회전된 이미지 올바로 세우기 

import cv2 as cv
import numpy as np

img = cv.imread('poker.jpg')
width, height = 257, 349 #가로 크기 257, 세로 크기 349 으로 결과물 출력

src = np.array([[351,67], [564, 208], [360, 497], [144, 350]], dtype=np.float32)
dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)
#좌상, 우상, 우하, 좌하 (시계 방향으로 4 지점 정의)
matrix = cv.getPerspectiveTransform(src, dst) #Matrix 얻어옴
result = cv.warpPerspective(img, matrix, (width, height))

cv.imshow('img', img)
cv.imshow('result', result)
cv.waitKey(0)
cv.destroyAllWindows()