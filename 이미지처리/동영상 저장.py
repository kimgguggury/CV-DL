import cv2 as cv

cap = cv.VideoCapture('video.mp4')

#코덱 정의 #어떤 형태로 저장할 지 
fourcc = cv.VideoWriter_fourcc(*'DIVX') #*를 붙이면 D I V X가 됨

#프레임 크기, FPS
width = round(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv.CAP_PROP_FPS) * 2 #영상 재생 속도가 2배

out = cv.VideoWriter('output.avi', fourcc, fps, (width, height))
#저장 파일명, 코덱, FPS, 크기 (width, height)

while cap.isOpened() :
    ret, frame = cap.read()
    
    if not ret :
        break
    
    out.write(frame) #영상 데이터만 저장 (소리 x)
    
    cv.imshow('video', frame)
    if cv.waitKey(1) == ord('q') :
        break

out.release() #자원 해제
cap.release()
cv.destroyAllWindows()