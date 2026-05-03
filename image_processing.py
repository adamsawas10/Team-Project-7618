from PIL import Image

def resize_images(image_list):

    min_width = min(img.size[0] for img in image_list)
    min_height = min(img.size[1] for img in image_list)


    resized = [img.resize((min_width, min_height)) for img in image_list]
    return resized


def average_images(image_list):

    images = resize_images(image_list)
    width, height = images[0].size


    result = Image.new("RGB", (width, height))


    for x in range(width):
        for y in range(height):
            # Grab that pixel from every image
            pixels = [img.getpixel((x, y)) for img in images]


            avg_r = sum(p[0] for p in pixels) // len(pixels)
            avg_g = sum(p[1] for p in pixels) // len(pixels)
            avg_b = sum(p[2] for p in pixels) // len(pixels)

            result.putpixel((x, y), (avg_r, avg_g, avg_b))

    return result



if __name__ == "__main__":
    img1 = Image.open("test1.jpg")
    img2 = Image.open("test2.jpg")

    output = average_images([img1, img2])
    output.save("output.jpg")
    print("Done! Check output.jpg")