from PIL import Image, ImageDraw

# 타원 그리기 
def ellipse(output_path):
    image = Image.new("RGB", (400, 400), "white") #도화지 만들기
    draw = ImageDraw.Draw(image) # 도화지에 그리는 객체를 만듬

    draw.ellipse((25, 50, 175, 200), fill="green")

    draw.ellipse((100, 150, 275, 300), width = 5, fill="yellow", outline="blue")

    image.save(output_path)

if __name__ == "__main__":
    ellipse("ellipse.jpg")