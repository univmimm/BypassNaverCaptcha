'''
*****주의*****
	동작하지 않음
테서렉트로 하려 했는데 동작하지 않는 코드ㅜㅜ
'''

#C:\Program Files (x86)\Tesseract-OCR
from pytesseract import *
from PIL import Image

def OCR(imgfile, lang ='eng') :
    img = Image.open(imgfile)
    text = image_to_string(img, lang = lang)
    
    print("OCR Result")
    print(text)

    
OCR('D:\\Git\\BypassNaverCaptcha\\image\\A.jpg')
