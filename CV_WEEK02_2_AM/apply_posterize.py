from PIL import Image, ImageOps

def posterize(image_path, output_path, bits):
    image = Image.open(image_path)
    converted_image = ImageOps.posterize(image, bits=bits)
    converted_image.save(output_path)

if __name__ == "__main__":
    posterize("hummingbird.jpg", "hummingbird_posterizeed.jpg", bits=2)