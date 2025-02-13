import cv2 as cv

cap = cv.VideoCapture(0) #0번째 카메라 장치 (Device ID)

if not cap.isOpened() : #카메라가 잘 열리지 않은 경우
    exit() #프로그램 종료

while True :
    ret, frame = cap.read()
    if not ret :
        break

    cv.imshow('camera', frame)
    if cv.waitKey(1) == ord('q') : #사용자가 q를 입력하면
        break

cap.release()
cv.destoryAllWindows()