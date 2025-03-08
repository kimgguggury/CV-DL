#윤곽선 (Contour): 경계선을 연결한 선

import cv2 as cv

img = cv.imread('card2.png')
target_img = img.copy() #사본 이미지

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, otsu = cv.threshold(gray, -1, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  

contours, hierarchy = cv.findContours(otsu, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# 윤곽선 정보, 구조 
# 이미지, 윤곽선 찾는 모드 (mode), 윤곽선 찾을 때 사용하는 근사치 방법 (method) :CHAIN_APPROX_SIMPLE, cv.CHAIN_APPROX_NONE
# 만약 사각형이면 심플로하면 꼭짓점 좌표만!!! => 메모리를 줄일 수 있음 
COLOR = (0, 200, 0) # 녹색
for cnt in contours :
    if cv.contourArea(cnt) > 25000 :
        x, y, width, height = cv.boundingRect(cnt)
        cv.rectangle(target_img,(x, y), (x + width, y + height), COLOR, 2)

cv.imshow('img', img)
cv.imshow('contour', target_img)

cv.waitKey(0)
cv.destroyAllWindows()