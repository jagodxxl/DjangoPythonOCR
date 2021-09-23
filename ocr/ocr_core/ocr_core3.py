import os
import sys

try:
  from PIL import Image
except ImportError:
  import Image
import pytesseract

def ocr_core(filename):
  """
  This function will handle the core OCR processing of images.
  """
 
  image_rgb = Image.open(filename)
  image_gray = image_rgb.convert('LA')
  #image_gray.save('image_gray.png')
  text = pytesseract.image_to_string(image_gray, lang="pol")
  return text

arg = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]

textout = ocr_core(arg2+'/'+arg)
linie = textout.split('\n')

count = 0
max = int(arg3)
while count < max:
  print(linie[len(linie)-1-max+count+1].split(' '))
  count +=1