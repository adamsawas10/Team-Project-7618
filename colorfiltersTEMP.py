import sys
import colorsys
from PIL import Image
from image_info import image_info

def grayscale(path):
    img = Image.open(path)
    gray_list = [((a[0]*299 + a[1]*587 + a[2]*114 )/1000,) * 3 for a in img.getdata()]
    img.putdata(gray_list)
    new_path = "temp_grayscale.jpg"
    img.save(new_path)
    return new_path

def negative(path):
    img = Image.open(path)
    nega_list = [(255-a[0], 255-a[1], 255-a[2]) for a in img.getdata()] 
    img.putdata(nega_list)
    new_path = "temp_negative.jpg"
    img.save(new_path)
    return new_path

def sepia(path):
    img = Image.open(path)
    sepia_list = []
    for p in img.getdata():
        if p[0] < 63:
            r,g,b = int(p[0] * 1.1), p[1], int(p[2] * 0.9)
        elif p[0] > 62 and p[0] < 192:
            r,g,b = int(p[0] * 1.15), p[1], int(p[2] * 0.85)
        else:
            r = int(p[0] * 1.08)
            g,b = p[1], int(p[2] * 0.5)
        r = min(255, r)
        g = min(255, g)
        b = min(255, b)
        sepia_list.append((r,g,b))
    img.putdata(sepia_list)
    new_path = "temp_sepia.jpg"
    img.save(new_path)
    return new_path

def saturation(path):
    img = Image.open(path)
    vibe_list = []
    for p in img.getdata():
        gray = int((p[0]*299 + p[1]*587 + p[2]*114) / 1000)
        r = int(gray + (p[0] - gray) * 1.3)
        g = int(gray + (p[1] - gray) * 1.3)
        b = int(gray + (p[2] - gray) * 1.3)

        r = min(255, max(0,r))
        g = min(255, max(0,g))
        b = min(255, max(0,b))
        vibe_list.append((r,g,b))
    img.putdata(vibe_list)
    new_path = "temp_saturation.jpg"
    img.save(new_path)
    return new_path

def selectivecolor(path, target_color):
    img = Image.open(path):
    selectcolor_list = []
    color_ranges = { "red": [(0, 15), (345, 360)], "orange": [(15, 45)], "yellow": [(45, 75)],
        "green": [(75, 165)], "blue": [(165, 255)], "purple": [(255, 345)] }

    for p in img.getdata():
        r = p[0]
        g = p[1]
        b = p[2]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        h_deg = h * 360

        matching = False
        for low, high in color_ranges[target_color]:
            if low <= h_deg <= high:
                matching = True
                break
        if matching:
            new_pixel = (r,g,b)
        else: 
            gray = int((p[0]*299 + p[1]*587 + p[2]*114) / 1000)
            new_pixel = (gray, gray, gray)
        selectcolor_list.append(new_pixel)
    img.putdata(selectcolor_list)
    new_path = "temp_selective.jpg"
    img.save(new_path)
    return new_path
    