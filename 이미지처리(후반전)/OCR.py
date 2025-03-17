from PIL import Image
import pytesseract

# 이미지 파일로부터 텍스트 추출
image = Image.open('gguHa1.jpg')
text = pytesseract.image_to_string(image, lang='eng')  # 'eng'는 영어를 의미합니다. 다른 언어를 사용할 경우 해당 언어 코드를 입력하세요.

print(text)