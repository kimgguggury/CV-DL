# import cv2 as cv
# img = cv.imread('gguHa1.jpg',cv.IMREAD_GRAYSCALE)

# ret, binary = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# cv.imshow('img', img)
# cv.imshow('binary', binary)
# cv.waitKey(0)
# cv.destroyAllWindows()



#기준
# Threshold (= 임계값)

#Trackbar (값 변화에 따른 변형 확인)
 
import cv2 as cv

def empty(pos) :
    print(pos)
    pass 

img = cv.imread('gguHa1.jpg',cv.IMREAD_GRAYSCALE)

name = 'Trackbar'
cv.namedWindow(name)

cv.createTrackbar('threshold', name, 127, 255, empty)

while True :
    thresh = cv.getTrackbarPos('threshold', name)
    ret, binary = cv.threshold(img, thresh, 255, cv.THRESH_BINARY)

    if not ret :
        break 

    cv.imshow(name, binary)
    if cv.waitKey(1) == ord('q') :
        break
cv.destroyAllWindows()