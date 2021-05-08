from PIL import Image, ImageDraw

## 시작과 끝을 연결해 채워주는 것 chord 
def chord(output_path):
    image = Image.new("RGB", (400, 400), "white") #도화지 만들기
    draw = ImageDraw.Draw(image) # 도화지에 그리는 객체를 만듬

    draw.chord((25, 50, 175, 200), start=30, end=250, fill="green")

    draw.chord((100, 150, 275, 300), start=20, end=100, width = 5, fill="yellow", outline="blue")

    image.save(output_path)

if __name__ == "__main__":
    chord("chord.jpg")


