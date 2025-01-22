import cv2 as cv
import sys

cap = cv.VideoCapture(0, cv.CAP_DSHOW) #카메라와 연결 시도

if not cap.isOpened() :
    sys.exit('카메라 연결 실패')

while True :
    ret, frame = cap.read() #ret은 성공여부, frame은 호출한 순간의 영상 한 장


    if not ret : #frame 획득 여부
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break
    
    cv.imshow('Video display', frame)

    key = cv.waitKey(1)
    if key==ord('q') :
        break

cap.release()
cv.destroyAllWindows()