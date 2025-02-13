import cv2 as cv
import numpy as np

img = np.zeros((480, 640, 3), dtype = np.uint8)

COLOR = (0, 255, 255) #BGR : Yellow
THICKNESS = 3

cv.line(img, (50, 100),(400, 50),COLOR, THICKNESS, cv.LINE_8)
#그릴 위치 시작 점, 끝 점, 색깔, 두께, 선 종류

cv.line(img, (50, 200),(400, 150),COLOR, THICKNESS, cv.LINE_4)
cv.line(img, (50, 300),(400, 250),COLOR, THICKNESS, cv.LINE_AA)
cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()