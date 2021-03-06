from PIL import Image, ImageOps

def crop(image_path, output_path, border):
    image = Image.open(image_path)
    converted_image = ImageOps.crop(image, border)
    converted_image.save(output_path)

if __name__ == "__main__":
    crop("hummingbird.jpg", "hummingbird_croped.jpg", border=200)