from PIL import Image, ImageDraw


def arc(output_path):
    image = Image.new("RGB", (400, 400), "white") #도화지 만들기
    draw = ImageDraw.Draw(image) # 도화지에 그리는 객체를 만듬

    draw.arc((25, 50, 175, 200), start=30, end=250, fill="green")

    draw.arc((100, 150, 275, 300), start=20, end=100, width = 5, fill="yellow")

    image.save(output_path)

if __name__ == "__main__":
    arc("arc.jpg")


