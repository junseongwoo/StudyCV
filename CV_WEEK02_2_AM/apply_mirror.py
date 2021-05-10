from PIL import Image, ImageOps


## 좌우 변경 
def mirror(image_path, output_path):
    image = Image.open(image_path)
    converted_image = ImageOps.mirror(image)
    converted_image.save(output_path)

if __name__ == "__main__":
    mirror("hummingbird.jpg", "hummingbird_mirror.jpg")