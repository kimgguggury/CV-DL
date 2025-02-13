import cv2 as cv
import numpy as np


img = np.zeros((480, 640, 3), dtype=np.uint8)
img[100:200,200:300] = (255, 255, 255)
print(img)
cv.imshow('img', img)

cv.waitKey(0)
cv.destroyAllWindows()