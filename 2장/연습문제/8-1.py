import cv2 as cv
import sys

img = cv.imread('smaile.jpg')
if img is None :
    sys.exit("파일을 찾을 수 없음")

def mouseCallback(event, x, y, flags, param) : 

    if event == cv.EVENT_RBUTTONDOWN :
        cv.rectangle(img,(x,y),(x+200,y+200),(0,0,255))

    cv.imshow('drawing', img) 
cv.namedWindow('drawing')
cv.imshow('drawing', img)
cv.setMouseCallback("drawing",mouseCallback, img)

while(True) :
    if cv.waitKey(1) == ord('q') :
        cv.destroyAllWindows()
        break