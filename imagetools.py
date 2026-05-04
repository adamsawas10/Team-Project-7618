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

