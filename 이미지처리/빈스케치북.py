import cv2 as cv
import numpy as np

#세로 480 x 가로 640, 3 Channel 에 해당하는 스케치북 만들기
img = np.zeros((480, 640, 3), dtype=np.uint8)
img[:] = (255,255,255) #전체 공간을 흰 색으로 채우기
#OpenCV는 BGR임
print(img)

cv.imshow('img', img)

cv.waitKey(0)
cv.destroyAllWindows()