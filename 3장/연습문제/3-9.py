import cv2 as cv
import numpy as np

# 이미지 로드
img = cv.imread('rose.jpg')
if img is None:
    raise ValueError("이미지를 불러올 수 없습니다. 경로를 확인하세요.")

clone = img.copy()  # 원본 이미지 보존
ix, iy = -1, -1  # 초기 좌표값 설정
patch = None  # patch 초기화

def draw(event, x, y, flags, param):
    global ix, iy, patch, img

    if event == cv.EVENT_LBUTTONDOWN:
        ix, iy = x, y  # 시작 좌표 저장

    elif event == cv.EVENT_LBUTTONUP:
        if ix != x and iy != y:  # 좌표가 같지 않을 때만 실행
            patch = img[iy:y, ix:x, :].copy()  # ROI 선택
            cv.rectangle(img, (ix, iy), (x, y), (255, 0, 0), 3)

            if patch.size > 0:  # 선택한 영역이 유효한 경우만
                patch1 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_NEAREST)
                patch2 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_LINEAR)
                patch3 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_CUBIC)

                cv.imshow('Resize nearest', patch1)
                cv.imshow('Resize bilinear', patch2)
                cv.imshow('Resize bicubic', patch3)

    cv.imshow('Drawing', img)

cv.namedWindow('Drawing')
cv.imshow('Drawing', img)
cv.setMouseCallback('Drawing', draw)

while True:
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('r'):  # 'r' 키를 누르면 원본 이미지로 초기화
        img = clone.copy()
        cv.imshow('Drawing', img)

cv.destroyAllWindows()
