from PIL import Image, ImageOps

## fit() = crop()+scale()
def fit(image_path, output_path, size, centering=(0.5,0.5)):
    image = Image.open(image_path)
    converted_image = ImageOps.fit(image, size, centering=centering)
    converted_image.save(output_path)

if __name__ == "__main__":
    fit("hummingbird.jpg", "hummingbird_fitted.jpg", size=(400, 400))