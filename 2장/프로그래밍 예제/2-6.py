import cv2 as cv
import sys

img = cv.imread('smaile.jpg')

if img is None :
    sys.exit('파일을 찾을 수 없음')


#(830, 30)은 직사각형의 왼쪽 위 구석점 좌표
#(1000,200)은 오른쪽 아래 구석의 좌표
#그다음 인수는 색깔을 나타낸다
#마지막은 선 두께를 나타낸다
cv.rectangle(img,(830,30),(1000,200),(0,0,255),2)

#영상에 문자를 쓰는 함수
#첫 번째 인수는 영상, 두 번째 인수는 써넣을 문자열
#세 번째는 문자열의 왼쪽 아래 구석점의 위치를 지정한다.
# 네 번째는 폰트 종류, 그다음은 글자 크기, 그다음은색깔, 마지막은 글자 두께
 
cv.putText(img,'laugh',(830,24),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

cv.imshow('Draw', img)

cv.waitKey()
cv.destroyAllWindows()