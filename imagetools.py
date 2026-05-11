import sys
import colorsys
from PIL import Image, ImageEnhance



def format(path, target_format):
    img = Image.open(path)
    if target_format == "png":
        new_path = "temp.png"
    elif target_format == "jpg":
        new_path = "temp.jpg"
    img.save(new_path)
    return new_path

def pallete(path):
    img = Image.open(path)
    
    img = img.quantize(colors = 5)
    img2 = img.convert("RGB")
    colors = img2.getcolors(maxcolors = 5)

    for count, color in colors:
        print(f"Color {color} occurs {count} times")

    
    new_path = "temp.png"
    img.save(new_path)
    return new_path

def brightness(path):
    img = Image.open(path)
     
    enhancer = ImageEnhance.Brightness(img)

    bright_img = enhancer.enhance(1.5)

    new_path = "temp.png"
    bright_img.save(new_path)
    return new_path

def add_RGB(path, r_new, g_new,b_new):

    img = Image.open(path).convert("RGB")
    pixels = img.load()

    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            new_r = max(0, min(255, r + r_new))
            new_g = max(0, min(255, g + g_new))
            new_b = max(0, min(255, b + b_new))

            pixels[x, y] = (new_r, new_g, new_b)

    new_path = "temp.png"
    img.save(new_path)
    return new_path 