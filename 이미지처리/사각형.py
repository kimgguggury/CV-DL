import cv2 as cv
import numpy as np

img = np.zeros((480, 640, 3), dtype = np.uint8)

COLOR = (0, 255, 0) #BGR : 초록색
THICKNESS = 3

cv.rectangle(img, (100, 100), (200, 200), COLOR, THICKNESS) #빈 사각형
#그릴 위치, 왼쪽 위 좌표, 오른쪽 아래 좌표, 색깔, 두께

cv.rectangle(img, (300, 100), (400, 300), COLOR, -1) #꽉 찬 사각형

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()