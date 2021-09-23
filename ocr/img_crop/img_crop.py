import sys
 
from PIL import Image
import pytesseract
 
def main(filejpg, lenght):
    try:
        #Relative Path
        img = Image.open(filejpg)
        width, height = img.size
        a = int(lenght)
       
        if a < height:
            area = (0, height - a, width, height)
            img = img.crop(area)
         
        #Saved in the same relative location
        filetab1 = filejpg.split('/')
        filetab2 = filetab1[1].split('.')
        fileout = filetab1[0] + '/' + filetab2[0] + '_crop.' + filetab2[1]
       
        img.save(fileout)  
 
        image_rgb = Image.open(fileout)
        image_gray = image_rgb.convert('LA')
 
        custom_config = r'-l pol+eng+fra+deu --psm 6'
        text = pytesseract.image_to_string(image_gray, config=custom_config)
        return text
         
    except IOError:
        pass
 
arg1 = sys.argv[1]
arg2 = sys.argv[2]
 
if __name__ == "__main__":
    textout = main(arg1, arg2)
 
print(textout)