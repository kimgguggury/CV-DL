# import cv2 as cv
# #고정 크기로 설정 여기서는 물체의 모형이 변할 수 있음(예를 들면 찌그러짐)
# img = cv.imread('gguHa2.jpg')
# dst = cv.resize(img, (300, 600)) #width, height 고정 크기

# cv.imshow('img', img)
# cv.imshow('resize',dst)

# cv.waitKey(0)
# cv.destroyAllWindows()


#비율로 설정
# import cv2 as cv
# img = cv.imread('gguHa2.jpg')
# dst = cv.resize(img, None, fx=0.5, fy=0.5) #0.5배로 축소

# cv.imshow('img', img)
# cv.imshow('resize',dst)

# cv.waitKey(0)
# cv.destroyAllWindows()

# 보간법 적용하여 축소

# import cv2 as cv

# img = cv.imread('gguHa2.jpg')
# dst = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA) #0.5배로 축소

# cv.imshow('img', img)
# cv.imshow('resize',dst)

# cv.waitKey(0)
# cv.destroyAllWindows()

# 보간법 적용하여 확대

# import cv2 as cv

# img = cv.imread('gguHa2.jpg')
# dst = cv.resize(img, None, fx=1.5, fy=1.5, interpolation=cv.INTER_CUBIC) #1.5배로 확대

# cv.imshow('img', img)
# cv.imshow('resize',dst)

# cv.waitKey(0)
# cv.destroyAllWindows()

#동영상

# # 고정  크기로 설정
# import cv2 as cv
# cap = cv.VideoCapture('video.mp4')

# while cap.isOpened() :
#     ret, frame = cap.read()
#     if not ret :
#         break

#     frame_resized = cv.resize(frame, (600, 500))
#     cv.imshow('video', frame_resized)
#     if cv.waitKey(1) == ord('q') :
#         break

# cap.release()
# cv.destroyAllWindows()


#비율로 설정

import cv2 as cv
cap = cv.VideoCapture('video.mp4')

while cap.isOpened() :
    ret, frame = cap.read()
    if not ret :
        break

    frame_resized = cv.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv.INTER_CUBIC)
    cv.imshow('video', frame_resized)
    if cv.waitKey(1) == ord('q') :
        break

cap.release()
cv.destroyAllWindows()