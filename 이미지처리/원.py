import cv2 as cv
import numpy as np

img = np.zeros((480, 640, 3), dtype = np.uint8)

COLOR = (255, 255, 0) #BGR : 옥색
RADIUS = 50
THICKNESS = 10

cv.circle(img, (200, 100), RADIUS, COLOR, THICKNESS, cv.LINE_AA) # 속이 빈 원
#그릴 위치, 원의 중심점, 반지름, 색깔, 두께, 선 종류
cv.circle(img, (400, 100), RADIUS, COLOR, -1, cv.LINE_AA) #속이 꽉 찬 원


cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()