#마우스 이벤트 등록

# import cv2 as cv
# import numpy as np

# img = cv.imread('poker.jpg')
# width, height = 257, 349 #가로 크기 257, 세로 크기 349 으로 결과물 출력

# src = np.array([[351,67], [564, 208], [360, 497], [144, 350]], dtype=np.float32)
# dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)
# #좌상, 우상, 우하, 좌하 (시계 방향으로 4 지점 정의)
# matrix = cv.getPerspectiveTransform(src, dst) #Matrix 얻어옴
# result = cv.warpPerspective(img, matrix, (width, height))

# cv.imshow('img', img)
# cv.imshow('result', result)
# cv.waitKey(0)
# cv.destroyAllWindows()

import cv2 as cv

def mouse_handler(event, x, y, flags, param) :
    if event == cv.EVENT_LBUTTONDOWN : # 마우스 왼쪽 버튼 누름
        print('왼쪽 버튼 Down')
        print(x,y)

    elif event == cv.EVENT_LBUTTONUP : #마우스 왼쪽 버튼 뗌
        print("왼쪽 버튼 Up")
        print(x,y)
    
    elif event == cv.EVENT_MOUSEMOVE : #마우스 이동
        print("마우스 이동")
    
    elif event == cv.EVENT_RBUTTONDOWN : #오른쪽 버튼 Down
        print('오른쪽 버튼 Down')

img = cv.imread('poker.jpg')
cv.namedWindow('img') #img 란 이름의 윈도우를 먼저 만들어두는 것. 여기에 무으스 이벤트를 처리하기 위한 핸들러 적용
cv.setMouseCallback('img', mouse_handler)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()