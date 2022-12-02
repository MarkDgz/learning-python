# Program:     wm-v-1.1.3-stable.py 
# Description: Generate one image with watermark, base previous program wm.py v-1.1.3
# Changes: 
# 1. Add multiple watermarks in parts var
# 2. Rotation grades for watermark text
# 3. Font color  
# Licence: GNU General Public License v3.0
# Dev status: Latest Stable Version 1.1.3

# # Required libraries
# python programs to support file and directory functions
import os
import sys
#Import required Image library
from PIL import Image, ImageDraw, ImageFont
from random import randint

# Generate Transparent Base Image for Watermark
def gen_t_image( iimg, isize ): 

    # Open new image into object
    #iimg = Image.new('RGBA', isize)

    # Open new image objetc from parameters
    rgba = iimg.convert("RGBA")
    datas = rgba.getdata()

    newData = []
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:  # Finding black colour by its RGB value
            # Storing a transparent value when we find a black colour
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)  # Other colours remain unchanged
    
    rgba.putdata(newData)
    return rgba

# Mixing two images and return mixed one back
def mix_img(img1, img2):
    comb_image = Image.alpha_composite(img1, img2)
    return comb_image

# Generating watermarks function
def gen_wm(name, parts, rotateg, bkgcolor, fcolor, original_image, original_image_size, fontzise):

    # --- Select watermark font ---
    font = ImageFont.truetype('Impacted2.0.ttf', fontzise)

    # calculate text size in pixels (width, height)
    text_size = font.getsize(name)

    # create image for text
    text_image = Image.new('RGBA', text_size)
    ###text_image = gen_t_image( text_size )
    #text_image.putalpha(0)
    text_draw = ImageDraw.Draw(text_image)
    #text_draw.save('out-img/out-text.png', "PNG")
    # draw text on image
    text_draw.text((0, 0), name, fcolor, font=font)
    # rotate text image and fill with transparent color
    rotated_text_image = text_image.rotate(rotateg, expand=True, fillcolor=bkgcolor)
    rotated_text_image = gen_t_image( rotated_text_image, original_image_size )
    rotated_text_image.save('out-img/out-rtextimg.png', "PNG")
    rotated_text_image_size = rotated_text_image.size
    #rotated_text_image.show()
    # --- watermarks image ---
    combined_image = original_image
    # calculate top/left corner for centered text
    ##parts = 8
    offset_x = original_image_size[0]//parts
    offset_y = original_image_size[1]//parts
    start_x = original_image_size[0]//parts - rotated_text_image_size[0]//2
    start_y = original_image_size[1]//parts - rotated_text_image_size[1]//2
    for a in range(0, parts, 2):
        for b in range(0, parts, 2):
            x = start_x + a*offset_x
            y = start_y + b*offset_y
            # image with the same size and transparent color (..., ..., ..., 0)
            watermarks_image = Image.new('RGBA', original_image_size)
            ###watermarks_image = gen_t_image( original_image_size )
            #watermarks_image.putalpha(0)
            #watermarks_image
            # put text in expected place on watermarks image
            watermarks_image.paste(rotated_text_image, (x, y))
            # put watermarks image on original image
            combined_image = mix_img(combined_image, watermarks_image)

    return combined_image



#Parameters
#font = ImageFont.truetype('Impacted2.0.ttf', fontzise)
#text  = "https://staygoldcrypto/shop"
if len(sys.argv) == 2:
    text = sys.argv[1]
else:
    print("Put the Watermark Text as Parameter")
    quit()
path  = ["inp-img", "out-img"]
font = ImageFont.truetype('Impacted2.0.ttf', 25)
margin = 50

# --- Watermark Params ---
parts = 6
grades = 30
fontcolor = (255,255,255,126)
backgcolor = (0,0,0,0)
fontzise = 19

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
    ###im = Image.open(nfile)
    im = Image.open(nfile).convert("RGBA")
    width, height = im.size

    xoriginal_image = im
    xoriginal_image_size = xoriginal_image.size

    outimage = gen_wm(text, parts, grades, backgcolor, fontcolor, xoriginal_image, xoriginal_image_size, fontzise)

    # --- result ---
    outFile = path[1] + f'/' + 'out-' +  filex
    print('Image processed -> ', outFile )
    outimage.save(outFile, "PNG")

print('Done...')
