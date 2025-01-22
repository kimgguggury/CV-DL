import cv2 as cv
import sys
import numpy as np

cap = cv.VideoCapture(0, cv.CAP_DSHOW) #카메라와 연결 시도

if not cap.isOpened() :
    sys.exit('카메라 연결 실패')

frames = []
while True :
    ret, frame = cap.read() #ret은 성공여부, frame은 호출한 순간의 영상 한 장


    if not ret : #frame 획득 여부
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break
    
    cv.imshow('Video display', frame)

    key = cv.waitKey(1)
    if key ==ord('c') :
        frames.append(frame)
    elif key==ord('q') :
        break

cap.release()
cv.destroyAllWindows()

if len(frames) > 0 :
    imgs = frames[0]
    for i in range(1, min(3, len(frames))):
        imgs = np.hstack((imgs, frames[i]))
    
    cv.imshow('collected images', imgs)

    cv.waitKey()
    cv.destroyAllWindows()


print(len(frames)) #frames 리스트 요소 개수 
print(frames[0].shape) #frames의 리스트의 0번 째 요소의 모양
print(type(imgs))
print(imgs.shape)