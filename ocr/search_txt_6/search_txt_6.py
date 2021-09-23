#
# use: python3 search_txt.py -i images/image3.jpg -t 'co szukam' -s 2
#

import pytesseract
from pytesseract import Output
import cv2
import argparse

def apply_brightness_contrast(input_img, brightness = 0, contrast = 0):

    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow)/255
        gamma_b = shadow

        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()

    if contrast != 0:
        f = 131*(contrast + 127)/(127*(131-contrast))
        alpha_c = f
        gamma_c = 127*(1-f)

        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    return buf

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
help="input image")
ap.add_argument("-t", "--text", type=str, default='',
help="text to search")
ap.add_argument("-s", "--size", type=int, default=0,
help="size after text")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])

txt = args["text"]
if len(txt) > 0:
    txt = txt.split(' ')
size = int(args["size"])

img = apply_brightness_contrast(img,0,64)


#custom_config = r'-l pol+eng+fra+deu --psm 6'
custom_config = r'-l pol --psm 6'
d = pytesseract.image_to_data(img, config=custom_config, output_type=Output.DICT)
#print(d)


n_boxes = len(d['level'])

for i in range(n_boxes):
    (x, y, w, h, t) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i], d['text'][i])
    #cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    words = len(txt)

    if words > 0 and t == txt[0]:
        for j in range(len(txt)):
            if i + j <= n_boxes:
                (x, y, w, h, t) = (d['left'][i+j], d['top'][i+j], d['width'][i+j], d['height'][i+j], d['text'][i+j])
                if t == txt[j]:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    print(t, x, y, w, h, sep=' ')
        for k in range(size):
            (x, y, w, h, t) = (d['left'][i+k+words], d['top'][i+k+words], d['width'][i+k+words], d['height'][i+k+words], d['text'][i+k+words])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            print(t, x, y, w, h, sep=' ')


cv2.imshow('img', img)
cv2.imwrite(args["image"].replace(".", "_t."), img)
cv2.waitKey(0)
