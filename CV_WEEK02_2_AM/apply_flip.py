from PIL import Image, ImageOps


## 위아래 변경
def flip(image_path, output_path):
    image = Image.open(image_path)
    converted_image = ImageOps.flip(image)
    converted_image.save(output_path)

if __name__ == "__main__":
    flip("hummingbird.jpg", "hummingbird_fliped.jpg")