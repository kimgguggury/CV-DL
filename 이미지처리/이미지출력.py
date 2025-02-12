import cv2 as cv

# img = cv.imread('gguHa1.jpg') #해당 경로의 파일 읽어오기
# cv.imshow('gguha', img) # gguha라는 이름의 창에 img를 표시
# key = cv.waitKey(0) #지정된 시간 동안 사용자 키 입력 대기
#               #0이라는 것은 무한적으로 대기하라는 뜻
# print(key)
# cv.destroyAllWindows() #모든 창 닫기

img_color = cv.imread("gguHa1.jpg", cv.IMREAD_COLOR)
img_gray = cv.imread("gguHa1.jpg", cv.IMREAD_GRAYSCALE)
img_unchanged = cv.imread("gguHa1.jpg", cv.IMREAD_UNCHANGED)
cv.imshow('gguHa',img_color)
cv.imshow('img_gray', img_gray)
cv.imshow('img_unchanged', img_unchanged)

print(img_color.shape)
cv.waitKey(0)
cv.destoryAllWindows()

