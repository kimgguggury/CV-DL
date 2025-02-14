import numpy as np
import cv2 as cv
from PIL import ImageFont, ImageDraw, Image

def myPutText(src, text, pos, font_size, font_color) :
    img_pil = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype('fonts/gulim.ttc', font_size)
    draw.text(pos, text, font=font, fill=font_color)
    return np.array(img_pil)

img = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR = (255, 255, 255)
FONT_SIZE = 30


# cv.putText(img, "꾸꾸리",(20, 50), cv.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS)

img = myPutText(img, "꾸꾸리", (20, 50), FONT_SIZE, COLOR)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()