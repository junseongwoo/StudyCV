from PIL import Image, ImageOps

def scale(image_path, output_path, factor):
    image = Image.open(image_path)
    converted_image = ImageOps.scale(image, factor)
    converted_image.save(output_path)

if __name__ == "__main__":
    scale("hummingbird.jpg", "hummingbird_scale.jpg", factor=5)