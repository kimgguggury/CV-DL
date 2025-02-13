import cv2 as cv
import numpy as np

img = np.zeros((480, 640, 3), dtype = np.uint8)

COLOR = (0, 0, 255) #BGR : 빨간색
THICKNESS = 3 #두께

pts1 = np.array([[100, 100], [200, 100], [100, 200]])
#True면 닫힌 도형이 됨 끝점과 시작점이 연결
#False면 연결하지 않음
pts2 = np.array([[200, 100], [300, 100], [300, 200]])
cv.polylines(img, [pts1], True, COLOR, THICKNESS, cv.LINE_AA)
cv.polylines(img, [pts2], True, COLOR, THICKNESS, cv.LINE_AA)

# cv.polylines(img, [pts1, pts2], True, COLOR, THICKNESS, cv.LINE_AA) #속이 빈 다각형
# #그릴 위치, 그릴 좌표들, 닫힘 여부, 색깔, 두께, 선 종류

pts3 = np.array([[[100, 300], [200, 300], [100, 400]], [[200, 300], [300, 300], [300, 400]]])
cv.fillPoly(img, pts3, COLOR, cv.LINE_AA) #꽉 찬 다각형
# #그릴 위치, 그릴 좌표들, 색깔, 선 종류
cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()