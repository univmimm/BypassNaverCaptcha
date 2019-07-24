#이미지파일 문자 읽어들이는 코드
import cv2
from matplotlib import pyplot as plt

from pytesseract import image_to_string
'''
모듈 없을 시
python -m pip install opencv-python
pip install matplotlib
'''

#이미지 열기
img = cv2.imread('CaptchaTest1.png')

#이미지 보기
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()



string_with_dates = image_to_string(img)
print(string_with_dates)