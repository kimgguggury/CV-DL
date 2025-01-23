import cv2 as cv
import sys

img1=cv.imread('image\gguggury.jpg')
img2=cv.imread('smaile.jpg')

if img1 is None :
    sys.exit('파일을 찾을 수 없습니다.')

if img2 is None :
    sys.exit('파일을 찾을 수 없음')

cv.imshow('Image1 Display', img1) #윈도우에 영상 표시


cv.imshow('Image2 Display', img2) #윈도우에 영상 표시


cv.waitKey()
cv.destroyAllWindows()
