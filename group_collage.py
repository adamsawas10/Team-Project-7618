from PIL import Image
import random
from image_processing import resize_images

# Will work asssuming a list of images is passed in
def collage(images):
    # Making sure that the function will only work with the 
    # correct amount of images.
    if not(len(images) >= 3 and len(images) <= 10):
        raise ValueError("Number of images must be in betweeen 3 and 10.")
    opened_images = []
    for img in images:
        # If the images are not open
        # will open them for proper use
        if type(img) == str:
            opened = Image.open(img).convert("RGB")
            opened_images.append(opened)
        else:
            opened_images.append(img.convert("RGB"))

    opened_images = resize_images(opened_images)
    
    #Width and height of collage image
    col_w, col_h = opened_images[0].width, opened_images[0].height

    canvas = Image.new('RGB', (col_w, col_h), "white")
    #chunk_width, chunk_height = col_w // 50, col_h // 50

    x = 0 
    while  x < col_w:
        rand_chunk_width = random.randint(1,35) # Can change the range once size determined
        y = 0
        while y < col_h:
            rand_chunk_height = random.randint(1,35)
            img_select = random.randint(0, len(opened_images) - 1)
            corner = x + rand_chunk_width
            b_corner = y + rand_chunk_height

            if x + rand_chunk_width > col_w:
                corner = col_w
            if y + rand_chunk_height > col_h:
                b_corner = col_h

            orig_img_chunck = (x, y, corner, b_corner)

            orig_pic = opened_images[img_select].crop(orig_img_chunck)
            
            canvas.paste(orig_pic, (x, y))

            y = b_corner
        x = corner

    #canvas.save("Spliced_Image")
    return canvas