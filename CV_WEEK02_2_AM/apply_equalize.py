from PIL import Image, ImageOps

def equalize(image_path, output_path):
    image = Image.open(image_path)
    converted_image = ImageOps.equalize(image)
    converted_image.save(output_path)

if __name__ == "__main__":
    equalize("hummingbird.jpg", "hummingbird_equalize.jpg")