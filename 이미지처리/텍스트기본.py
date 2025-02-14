import numpy as np
import cv2 as cv

img = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR = (255, 255, 255)
THICKNESS = 1 #두께
SCALE = 1 #크기

cv.putText(img, "꾸꾸리",(20, 50), cv.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS)


cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()