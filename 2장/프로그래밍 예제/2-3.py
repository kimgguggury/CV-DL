import cv2 as cv
import sys

img = cv.imread('image/gguggury.jpg')

if img is None :
    sys.exit('이미지를 찾을 수 없음')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #컬러 영상을 명암으로 변환!
#첫 번째 인수는 컬러 영상을 가진 객체, 
#두 번째 인수는 cv.COLOR_BGR2GRAY 컬러 영상을 명암으로 변환하라고 지시한다.
gray_small = cv.resize(gray, dsize=(0,0), fx=0.5, fy=0.5) 
#resize함수로 사이즈를 변환한다.
#dsize는 절대크기를 나타낸다. (0, 0)이면 fx와 fy에 따른다는 뜻
# fx, fy는 상대크기를 나타낸다.

# imwrite는 지정한 영상을 지정한 파일에 저장한다. 
cv.imwrite('gguggury_gray.jpg', gray)
cv.imwrite('gguggury_gray_small.jpg', gray_small)

# cv.imshow('Color image', img)
# cv.imshow('Gray image', gray)
# cv.imshow('Color image', gray_small)

# cv.waitKey()
# cv.destroyAllWindows()

#명암 영상으로 만드는 방법은
# I = round(0.299*R + 0.587*G +0.114*B)로 구한다.
#실제로 계산을 해보면 
RGBToGray = round(0.299*237 + 0.587*233 + 0.114*232)
print(RGBToGray) #234가 나옴
print(gray[0, 0]) #234나옴 저 공식을 확인 해봄