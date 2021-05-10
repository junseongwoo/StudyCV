from PIL import Image, ImageOps

def autocontrast(image_path, output_path, black, white):
    image = Image.open(image_path)
    converted_image = ImageOps.autocontrast(image, black, white)
    converted_image.save(output_path)

if __name__ == "__main__":
    autocontrast("hummingbird.jpg", "colorize.jpg", black="green", white="white")
