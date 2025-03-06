# 색깔이 달라지는 부분을 경계선으로 인식한다.
# Canny Edge Detection

import cv2 as cv


img =cv.imread('gguZam.jpg')
canny = cv.Canny(img, 150, 200)
# 대상 이미지, minVal(하위 임계값), maxVal(상위임계값)


cv.imshow('img', img)
cv.imshow('Canny', canny)
cv.waitKey(0)
cv.destroyAllWindows()

# import cv2 as cv

# def empty(pos) :
#     pass

# img =cv.imread('gguZam.jpg')

# name = "Trackbar"
# cv.namedWindow(name)
# cv.createTrackbar("threshold1", name, 0, 255, empty) #minVal
# cv.createTrackbar("threshold2", name, 0, 255, empty) #maxVal

# while True :
#     threshold1 = cv.getTrackbarPos('threshold1', name)
#     threshold2 = cv.getTrackbarPos('threshold2', name)

#     canny = cv.Canny(img, threshold1, threshold2)
#     # 대상 이미지, minVal(하위 임계값), maxVal(상위임계값)


#     cv.imshow('img', img)
#     cv.imshow(name, canny)

#     if cv.waitKey(1) == ord('q') :
#         break 

# cv.destroyAllWindows()