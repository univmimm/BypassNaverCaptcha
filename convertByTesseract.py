#C:\Program Files (x86)\Tesseract-OCR

from pytesseract import image_to_string

string_with_dates = image_to_string(img)
print(string_with_dates)
