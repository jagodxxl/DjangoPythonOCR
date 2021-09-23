#
# use: python3 rotate.py -i images/image3.jpg -a 90
#

import pytesseract
import cv2
import argparse
import re
import numpy as np
import imutils

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
        help="input image")
ap.add_argument("-a", "--angle", required=True,
        help="angle image")

args = vars(ap.parse_args())

img = cv2.imread(args["image"])

angle = int(args["angle"])

if angle != 0:
    rotated = imutils.rotate_bound(img, angle)
    cv2.imshow("Rotated", rotated)
    cv2.imwrite(args["image"].replace(".", "_rotate." +str(angle)+"."), rotated)
    cv2.waitKey(0)
else:
    cv2.imshow("Oryginal", img)
    cv2.waitKey(0)

output="OK"
print(output)
