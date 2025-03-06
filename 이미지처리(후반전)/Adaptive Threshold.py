#이미지를 작은 영역으로 나누어서 임계치 적용

import cv2 as cv

def empty(pos) :
    print(pos)
    pass 

img = cv.imread('gguHa1.jpg',cv.IMREAD_GRAYSCALE)

name = 'Trackbar'
cv.namedWindow(name)

#bar 이름, 창의 이름, 초기값, 최대값, 이벤트 처리
cv.createTrackbar('block_size', name, 25, 100, empty) #홀수만 가능, 1보다는 큰 값
cv.createTrackbar('c', name, 3, 10, empty) #일반적으로 양수의 값을 사용

while True :
    block_size = cv.getTrackbarPos('block_size', name)
    c = cv.getTrackbarPos('c', name)

    if block_size <= 1 : #1이하면 3으로
        block_size = 3

    if block_size % 2 == 0 : #짝수이면 홀수로
        block_size += 1
     
    binary = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,block_size, c)
 

    cv.imshow(name, binary)
    if cv.waitKey(1) == ord('q') :
        break
cv.destroyAllWindows()

#그럼 궁금한 게 어디 부분으로 나눠지는가?