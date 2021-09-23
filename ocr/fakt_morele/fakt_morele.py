import sys
 
from PIL import Image
import pytesseract
 
def main(filejpg, txt, a, b, c, d):
    try:
        img = Image.open(filejpg)
        area = (a, b, c, d)
        img = img.crop(area)

        #Saved in the same relative location
        filetab1 = filejpg.split('/')
        filetab2 = filetab1[1].split('.')
        fileout = filetab1[0] + '/' + filetab2[0] + '_frag' + txt + '.' + filetab2[1]

        img.save(fileout)

        image_rgb = Image.open(fileout)
        image_gray = image_rgb.convert('LA')
        custom_config = r'-l pol+eng+fra+deu --psm 6'
        text = pytesseract.image_to_string(image_gray, config=custom_config)
        return text

    except IOError:
        pass

arg1 = sys.argv[1]
image = Image.open(arg1)
w, h = image.size

text1 = main(arg1, '1', 93 / 1600 * w, 66 / 2288 * h, 692 / 1600 * w, 371 / 2288 *h)
#text2 = main(arg1, '2', 1006 / 1600 * w, 110 / 2288 * h, 1332 / 1600 * w, 150 / 2288 *h)
#text3 = main(arg1, '3', 1394 / 1600 * w, 154 / 2288 * h, 1544 / 1600 * w, 246/ 2288 * h)
#text4 = main(arg1, '4', 80 / 1600 * w, 418 / 2288 * h, 780 / 1600 * w, 621 / 2288 * h)
#text5 = main(arg1, '5', 749 / 1600 * w, 380 / 2288 * h, 1532 / 1600 * w, 678 / 2288 * h)
#text6 = main(arg1, '6', 1002 / 1600 * w, 1900 / 2288 * h, 1538 / 1600 * w, 1934 / 2288 *h)

print(text1)
#print(text2)
#print(text3)
#print(text4)
#print(text5)
#print(text6)