import os
import colorsys
from PIL import Image


def make_output_path(path, filter_name):
    folder = os.path.dirname(path)
    original_name = os.path.basename(path)
    name, ext = os.path.splitext(original_name)
    return os.path.join(folder, f"{name}_{filter_name}.jpg")


def grayscale(path):
    img = Image.open(path).convert("RGB")
    gray_list = []

    for p in img.getdata():
        gray = int((p[0] * 299 + p[1] * 587 + p[2] * 114) / 1000)
        gray_list.append((gray, gray, gray))

    img.putdata(gray_list)

    new_path = make_output_path(path, "grayscale")
    img.save(new_path)

    return new_path


def negative(path):
    img = Image.open(path).convert("RGB")
    nega_list = []

    for p in img.getdata():
        nega_list.append((255 - p[0], 255 - p[1], 255 - p[2]))

    img.putdata(nega_list)

    new_path = make_output_path(path, "negative")
    img.save(new_path)

    return new_path


def sepia(path):
    img = Image.open(path).convert("RGB")
    sepia_list = []

    for p in img.getdata():
        if p[0] < 63:
            r, g, b = int(p[0] * 1.1), p[1], int(p[2] * 0.9)
        elif p[0] < 192:
            r, g, b = int(p[0] * 1.15), p[1], int(p[2] * 0.85)
        else:
            r, g, b = int(p[0] * 1.08), p[1], int(p[2] * 0.5)

        sepia_list.append((min(255, r), min(255, g), min(255, b)))

    img.putdata(sepia_list)

    new_path = make_output_path(path, "sepia")
    img.save(new_path)

    return new_path


def saturation(path):
    img = Image.open(path).convert("RGB")
    vibe_list = []

    for p in img.getdata():
        gray = int((p[0] * 299 + p[1] * 587 + p[2] * 114) / 1000)

        r = int(gray + (p[0] - gray) * 1.3)
        g = int(gray + (p[1] - gray) * 1.3)
        b = int(gray + (p[2] - gray) * 1.3)

        vibe_list.append((
            min(255, max(0, r)),
            min(255, max(0, g)),
            min(255, max(0, b))
        ))

    img.putdata(vibe_list)

    new_path = make_output_path(path, "saturation")
    img.save(new_path)

    return new_path


def selectivecolor(path, target_color):
    img = Image.open(path).convert("RGB")
    selectcolor_list = []

    color_ranges = {
        "red": [(0, 15), (345, 360)],
        "orange": [(15, 45)],
        "yellow": [(45, 75)],
        "green": [(75, 165)],
        "blue": [(165, 255)],
        "purple": [(255, 345)]
    }

    for p in img.getdata():
        r, g, b = p
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        h_deg = h * 360

        matching = False
        for low, high in color_ranges[target_color]:
            if low <= h_deg <= high:
                matching = True
                break

        if matching:
            new_pixel = (r, g, b)
        else:
            gray = int((r * 299 + g * 587 + b * 114) / 1000)
            new_pixel = (gray, gray, gray)

        selectcolor_list.append(new_pixel)

    img.putdata(selectcolor_list)

    new_path = make_output_path(path, f"selective_{target_color}")
    img.save(new_path)

    return new_path
