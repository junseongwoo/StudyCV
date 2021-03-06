from PIL import Image, ImageOps

def invert(image_path, output_path):
    image = Image.open(image_path)
    converted_image = ImageOps.invert(image)
    converted_image.save(output_path)

if __name__ == "__main__":
    invert("hummingbird.jpg", "hummingbird_inverted.jpg")