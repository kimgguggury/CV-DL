import cv2 as cv

img = cv.imread('gguHa2.jpg', cv.IMREAD_GRAYSCALE) #흑백으로 이미지 불러오기
cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()

#png로 하고 싶으면 확장자만 png로 바꾸면 됨
result = cv.imwrite('img_save.jpg', img)
print(result)