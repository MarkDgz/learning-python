# Required libraries
#python program to check if a directory exists
import os
#Import required Image library
from PIL import Image, ImageDraw, ImageFont
from random import randint

#Parameters
path  = ["inp-img", "out-img"]
text  = "Buy this NFT on staygoldcrypto.com"
font = ImageFont.truetype('Impacted2.0.ttf', 20)
margin = 50

# Check whether the specified path exists or not
for dpath in path:
    eXist = os.path.exists(dpath)
    if not eXist :
        os.mkdir(dpath)
        #printing if the path exists or not
        print(dpath + ' Directory was created')


# Getting the list of directories
dir = os.listdir(path[0])
  
# Checking if the list is empty or not
if len(dir) == 0:
    print("Empty source image directory")
else:
    print("Processing Images...")

for filex in dir:
    #Create an Image Object from an Image
    nfile = path[0] + f'/' + filex
    im = Image.open(nfile)
    width, height = im.size
    draw = ImageDraw.Draw(im)
    textwidth, textheight = draw.textsize(text, font)
    # calculate the x,y coordinates of the text
    rndint  = (1 / randint(25, 99)) * 450
    rndint2 = (1 / randint(35, 99)) * 255
    rndint3 = randint(0, 255)
    rndint4 = randint(0, 255) 
    x = round( ((width - textwidth   - margin  ) / rndint ), 0)
    y = round( ((height - textheight - margin  ) / rndint2), 0)
    print('axis yx width height textwith textheight margin ',x,y, width, height, textwidth, textheight, margin )
    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font, fill=(255-rndint3-5,rndint3,rndint4,255-rndint4-10))

    # im.show()
    #Save watermarked image
    outFile = path[1] + f'/' + 'out-' +  filex
    print('Image processed -> ', outFile )
    im.save(outFile)

print('Done...')
