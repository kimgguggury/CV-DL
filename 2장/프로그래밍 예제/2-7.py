import cv2 as cv
import sys

img = cv.imread('smaile.jpg')

if img is None :
    sys.exit('파일을 찾을 수 없음')

#event는 이벤트 종류, x,y는 이벤트가 일어난 순간의 커서 위치!

def draw(event, x, y, flags, param) :
    if event==cv.EVENT_LBUTTONDOWN :
        cv.rectangle(img,(x,y),(x+200,y+200),(0,0,255),2)
    elif event==cv.EVENT_RBUTTONDOWN :
        cv.rectangle(img,(x,y),(x+100, y+100), (255,0,0),2)

    cv.imshow('Drawing', img)


cv.namedWindow('Drawing') #Drawing이라는 윈도우 생성
cv.imshow('Drawing',img) #Drawing이라는 영상을 디스플레이한다.

cv.setMouseCallback('Drawing',draw) 
#Drawing이라는 윈도우에서 마우스 이벤트가 발생하면 draw라는 콜백함수를 호출

while(True) :
    if cv.waitKey(1) == ord('q') :
        cv.destroyAllWindows()
        break