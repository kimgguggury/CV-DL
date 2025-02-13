import cv2 as cv
cap = cv.VideoCapture('video.mp4')

while cap.isOpened() : #동영상 파일이 올바로 열렸는 지
    ret, frame = cap.read() # ret : 성공여부, frame : 받아온 이미지
    if not ret : 
        print("더 이상 가져올 프레임이 없어요")
        break
    cv.imshow('video', frame)

    if cv.waitKey(1) == ord('q') :
        print("사용자 입력에 의해 종료합니다.")
        break
cap.release() #자원 해제
cv.destroyAllWindows()