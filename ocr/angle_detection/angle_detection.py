#
# use: python3 angle_detection.py -i images/image3.jpg
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

args = vars(ap.parse_args())

img = cv2.imread(args["image"])

newdata = pytesseract.image_to_osd(img)
angle = int(re.search('(?<=Rotate: )\d+', newdata).group(0))
print("Kat:", angle)

if angle >= 0 and angle <=45:
   print("Vertical")
elif angle > 45 and angle <=135:
   print("Horizontal")
elif angle > 135 and angle <=225:
   print("Vertical")
elif angle > 225 and angle <=315:
   print("Horizontal")
elif angle > 315 and angle <=360:
   print("Vertical")