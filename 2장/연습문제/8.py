import cv2 as cv
import sys

img = cv.imread('smaile.jpg')

if img is None :
    sys.exit('파일을 찾을 수 없음')

BrushSize = 50
LColor, RColor = (255,0,0), (0,0,255)


def painting(event, x, y, flags, param) :
    global ix, iy 

    if event==cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img, (x,y,x+50,y+50),LColor)
    elif event==cv.EVENT_RBUTTONUP :
        cv.circle(img, (x,y), BrushSize,RColor,-1)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        cv.rectangle(img, (x,y,x+50,y+50),LColor)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_RBUTTON:
        cv.circle(img, (x,y), BrushSize,RColor,-1)

    cv.imshow('Painting', img)


cv.namedWindow('Painting') 
cv.imshow('Painting',img) 
cv.setMouseCallback('Painting',painting) 

while(True) :
    if cv.waitKey(1) == ord('q') :
        cv.destroyAllWindows()
        break