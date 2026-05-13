"""
Name: Ricardo Losoya
Course: Cst 205 Multimedia Design & Programming
Date: 05/13/2026

"""
import sys
import colorsys
import os
from PIL import Image, ImageEnhance


def make_output_path(path, filter_name):
    folder = os.path.dirname(path)
    original_name = os.path.basename(path)
    name, ext = os.path.splitext(original_name)
    return os.path.join(folder, f"{name}_{filter_name}.jpg")

"""
def format(path, target_format):
    img = Image.open(path)
    if target_format == "png":
        new_path = "temp.png"
    elif target_format == "jpg":
        new_path = "temp.jpg"
    img.save(new_path)
    return new_path
"""

#Above is a scrapped idea.

def pallete(path): #Should return the 5 colors of the image
    img = path
    
    img = img.quantize(colors = 5) #reduces amount of colors and puts image in p mode
    img2 = img.convert("RGB") #puts it back into rgb mode
    colors = img2.getcolors(maxcolors = 5) #
    color_list = []
    for count, color in colors:
        color_list.append(color)

    c1 = color_list[0]
    c2= color_list[1]
    c3 = color_list[2]
    c4 = color_list[3]
    c5 = color_list[4]

    return c1, c2, c3, c4, c5
#The colors are returns are then become strings so html can use them

def brightness(path): #Makes images brighter(Same effect can be accomplished with add_rgb)
    img = Image.open(path)
     
    enhancer = ImageEnhance.Brightness(img)

    bright_img = enhancer.enhance(1.5)

    new_path = make_output_path(path, "grayscale")
    bright_img.save(new_path)
    return new_path

def add_RGB(path, r_new, g_new, b_new): #lets you add red green or blue values to an image

    img = Image.open(path).convert("RGB")
    pixels = img.load()
    r2 = int(r_new)
    g2 = int(g_new)
    b2 = int(b_new)

    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            new_r = max(0, min(255, r + r2))
            new_g = max(0, min(255, g + g2))
            new_b = max(0, min(255, b + b2))

            pixels[x, y] = (new_r, new_g, new_b)

    new_path = make_output_path(path, "add_rgb")
    img.save(new_path)
    return new_path 