from PIL import Image, ImageOps

# 이미지의 콘트라스트 = 명암, 대비, 
def autocontrast(image_path, output_path, cutoff=0, ignore=None):
    image = Image.open(image_path)
    converted_image = ImageOps.autocontrast(image, cutoff, ignore)
    converted_image.save(output_path)

if __name__ == "__main__":
    autocontrast("hummingbird.jpg", "autocontrast.jpg", cutoff=0.2)
