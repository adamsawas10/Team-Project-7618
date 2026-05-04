from PIL import Image
import glob
import statistics

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
            pixels = [img.getpixel((x, y)) for img in images]
            avg_r = sum(p[0] for p in pixels) // len(pixels)
            avg_g = sum(p[1] for p in pixels) // len(pixels)
            avg_b = sum(p[2] for p in pixels) // len(pixels)
            result.putpixel((x, y), (avg_r, avg_g, avg_b))
    return result

def median_images(image_list):
    images = resize_images(image_list)
    width, height = images[0].size
    result = Image.new("RGB", (width, height))
    for x in range(width):
        for y in range(height):
            pixels = [img.getpixel((x, y)) for img in images]
            med_r = int(statistics.median(p[0] for p in pixels))
            med_g = int(statistics.median(p[1] for p in pixels))
            med_b = int(statistics.median(p[2] for p in pixels))
            result.putpixel((x, y), (med_r, med_g, med_b))
    return result

if __name__ == "__main__":
    image_paths = glob.glob("test*.jpg")
    if len(image_paths) < 3 or len(image_paths) > 10:
        print("Please provide between 3 and 10 images!")
    else:
        images = [Image.open(path) for path in image_paths]
        average_output = average_images(images)
        average_output.save("output_average.jpg")
        median_output = median_images(images)
        median_output.save("output_median.jpg")
        print("Done! Check output_average.jpg and output_median.jpg")