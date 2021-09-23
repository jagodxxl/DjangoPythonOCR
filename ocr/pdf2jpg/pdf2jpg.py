import os
import sys

from pdf2image import convert_from_path

from pdf2image.exceptions import(
PDFInfoNotInstalledError,
PDFPageCountError,
PDFSyntaxError
)

def convert(filepdf,dir_out):
 images = convert_from_path(filepdf)

 for i, image in enumerate(images):
   fname = dir_out+'/image'+ str(i)+'.jpg'
   image.save(fname)

arg = sys.argv[1]
arg2 = sys.argv[2]
convert(arg, arg2)
output="OK"
print(output)
