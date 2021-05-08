import io
import os
import PySimpleGUI as sg
from PIL import Image

# (튜플)소괄호 {딕셔너리}중괄호 [리스트]대괄호 : 데이터 집합들을 만듦!
file_types = [("JPEG (*.jpg)", "*.jpg"),
 ("All files (*.*)", "*.*")]

def main():
    layout = [
        [sg.Image(key="-IMAGE-", size=(400,400))],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), key= "-FILE-"),
            sg.FileBrowse(file_types = file_types),
            sg.Button("Load Image"),
        ]
    ]

    window = sg.Window("이미지 뷰어", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load Image":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])   
                image.thumbnail((400, 400))            ## 불러올 이미지 크기 
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue(), size=(400,400))
    window.close()

if __name__ == "__main__":
    main()