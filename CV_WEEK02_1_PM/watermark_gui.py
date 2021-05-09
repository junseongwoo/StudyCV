# watermark_gui.py

import io
import os
import PySimpleGUI as sg
import shutil
import tempfile

from PIL import Image
from watermark_transparent import watermark_with_transparency

file_types = [("JPEG (*.jpg)", "*.jpg"), ("All files (*.*)", "*.*")]

## 저장하는 것은 jpg로 저장하겠다. 
tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg").name ## 

## 이미지를 가져와서 썸네일화 시켜서 띄움 
def convert_image(image_path):
    image = Image.open(image_path)
    image.thumbnail((400, 400))
    bio = io.BytesIO()             ## 메모리에 올림
    image.save(bio, format="PNG")  ## png로 저장한다.
    return bio.getvalue()          ## 값 가져옴

##
def create_row(label, key, file_types, save=False):
    if save:
        return [
        sg.Text(label),
        sg.Input(size=(25, 1), key=key),
        sg.FileSaveAs(file_types=file_types)
    ]
    return [
        sg.Text(label),
        sg.Input(size=(25, 1), key=key),
        sg.FileBrowse(file_types=file_types),
    ]



def apply_watermark(original_image, values, position, window):
    watermark_with_transparency(
        ## 원본           출력         워터마크 이미지        위치 
        original_image, tmp_file, values["-WATERMARK-"], position
    )
    photo_img = convert_image(tmp_file)
    window["-IMAGE-"].update(data=photo_img)


def check_for_errors(values):
    if not values["-FILENAME-"]:
        sg.Popup("에러", "이미지를 불러오지 않았습니다!")
        return True
    if not values["-WATERMARK-"]:
        sg.Popup("에러", "워터마크를 불러오지 않았습니다!")
        return True
    if not values["-WATERMARK-X-"] or not values["-WATERMARK-Y-"]:
        sg.Popup("에러", "워터마크 위치가 정확하지 않습니다")
        return True
    return False


def save_image(values):
    save_filename = sg.popup_get_file(
        "File", file_types=file_types, save_as=True, no_window=True
    )
    if save_filename == values["-FILENAME-"]:
        sg.popup_error(
            "원본 이미지에는 덮어쓸 수가 없습니다!")
    else:
        if save_filename:
            shutil.copy(tmp_file, save_filename)
            sg.popup(f"저장: {save_filename}")



def main():
    original_image = None

    ## 레이아웃 잡았음,
    layout = [
        [sg.Image(key="-IMAGE-", size=(400, 400))],           ## 이미지를 불러올 곳을 만듦 
        create_row("이미지 파일:", "-FILENAME-", file_types),  ## 흰 줄을 만들어줌 
        create_row("워터마크 파일:", "-WATERMARK-",
                   [("PNG (*.png)", "*.png")]),
        [sg.Button("Load Image")],
        [
            sg.Text("워터마크 위치"),
            sg.Text("X:"),
            sg.Input("0", size=(5, 1), enable_events=True,
                     key="-WATERMARK-X-"),
            sg.Text("Y:"),
            sg.Input("0", size=(5, 1), enable_events=True,
                     key="-WATERMARK-Y-"),
        ],
        [sg.Button("워터마크 적용", enable_events=True),
         sg.Button("이미지 저장", enable_events=True),
         ],
    ]

    window = sg.Window("워터마크 GUI", layout, size=(450, 500))


    while True:
        event, values = window.read() ## 윈도우에서 이벤트랑 값을 가져오게 함 

        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        watermark_x = values["-WATERMARK-X-"]
        watermark_y = values["-WATERMARK-Y-"]

        if event == "Load Image":
            filename = values["-FILENAME-"]
            if os.path.exists(filename):
                photo_img = convert_image(filename)
                window["-IMAGE-"].update(data=photo_img)
                original_image = filename
                shutil.copy(original_image, tmp_file)
        if event in ["-WATERMARK-X-", "-WATERMARK-Y-"]:
            # filter watermark position to integers
            if watermark_x and watermark_y:
                if not watermark_x[-1].isdigit():
                    window["-WATERMARK-X-"].update(watermark_x[:-1])
                if not watermark_y[-1].isdigit():
                    window["-WATERMARK-Y-"].update(watermark_y[:-1])
        if event == "워터마크 적용":
            if check_for_errors(values):
                continue
            position = (int(watermark_x),
                        int(watermark_y))
            apply_watermark(original_image, values, position, window)
        if event == "이미지 저장" and values["-FILENAME-"]:
            save_image(values)

    window.close()


if __name__ == "__main__":
    main()
