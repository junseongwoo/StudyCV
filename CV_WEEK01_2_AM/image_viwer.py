import io                 ## 시스템 및 운영체제 
import os                 ## 파이썬 스탠다드 라이브러리
import PySimpleGUI as sg  ## gui 만들기 위한 라이브러리
from PIL import Image     ## 이미지 처리하기 위해 

# (튜플)소괄호 {딕셔너리}중괄호 [리스트]대괄호 : 데이터 집합들을 만듦!
file_types = [("JPEG (*.jpg)", "*.jpg"),
 ("All files (*.*)", "*.*")]

def main():
    layout = [
        #[sg.Image(key="-IMAGE-", size=(400,400))],
        #[
        [sg.Text("Image File")],
        [sg.Input(size=(25, 1), key= "-FILE-")],
        [sg.FileBrowse(file_types = file_types), sg.Button("Load Image")],
        #]
    ]

    window = sg.Window("이미지 뷰어", layout)

    while True:                                        ## 이벤트 루프
        event, values = window.read()                  ## 이미지를 보여준다.

        if event == "Exit" or event == sg.WIN_CLOSED: 
            break

        if event == "Load Image":
            filename = values["-FILE-"]                ## 위에서 key 값을 불러옴 
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])   
                image.thumbnail((400, 400))            ## 불러올 이미지 크기 
                bio = io.BytesIO()                     ## 메모리에 올려서 읽는 방법 
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue(), size=(400,400))
    window.close()

if __name__ == "__main__":    ## dunder = double underscore     _ = single underscore,  __ double underscore 
    main()

