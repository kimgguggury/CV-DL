# #이미지 흐림
# #외각선 검출 작업을 보다 단순하게 처리할 수 있다.

#가우시안 블러
#커널 사이즈 변화에 따른 흐림
# import cv2 as cv
# img = cv.imread('gguZam.jpg')

# #(3,3) (5,5) (7,7)
# kernel_3 = cv.GaussianBlur(img, (3, 3), 0)
# kernel_5 = cv.GaussianBlur(img, (5, 5), 0)
# kernel_7 = cv.GaussianBlur(img, (7, 7), 0)
# cv.imshow('img',img)
# cv.imshow('kernel_3',kernel_3)
# cv.imshow('kernel_5',kernel_5)
# cv.imshow('kernel_7',kernel_7)
# cv.waitKey(0)
# cv.destroyAllWindows()


#표준 편차 변화에 따른 흐림

import cv2 as cv
img = cv.imread('gguZam.jpg')


sigma_1 = cv.GaussianBlur(img, (0, 0), 1) #sigmaX - 가우시안 커널의 x 방향 표준편차 
sigma_2 = cv.GaussianBlur(img, (0, 0), 2)
sigma_3 = cv.GaussianBlur(img, (0, 0), 3)
cv.imshow('img',img)
cv.imshow('sigma_1',sigma_1)
cv.imshow('sigma_2',sigma_2)
cv.imshow('sigma_3',sigma_3)
cv.waitKey(0)
cv.destroyAllWindows()