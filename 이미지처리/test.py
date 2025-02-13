import cv2 as cv
import numpy as np

img = np.zeros((480, 640, 3), dtype = np.uint8)

COLOR = (0, 0, 255) #BGR : 빨간색
THICKNESS = 3 #두께

pts1 = np.array([[100, 100], [200, 100], [100, 200]])


cv.polylines(img, [pts1], False, COLOR, THICKNESS, cv.LINE_AA)


cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()