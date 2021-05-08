import io
import os
import PySimpleGUI as sg
import shutil
import tempfile

from blur_image import blur
from contour_image import contour
from detail_image import detail
from edge_enhance_image import edge_enhance
from emboss_image import emboss
from find_edges_image import find_edges
from PIL import Image

file_types = [("(JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

def apply_effect(values, window):
    pass  # 여기에 내용 넣기

def save_image(values):
    pass  # 여기에 내용 넣기

def main():
    effect_names = list(effects.keys())
    layout = [
        [sg.Image(key="-IMAGE-", size=(400, 400))],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), key="-FILENAME-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load Image")
        ],
        [
            sg.Text("Effect"),
            sg.Combo(
                effect_names, default_value="Normal", key="-EFFECTS-",
                enable_events=True, readonly=True
            ),
        ],
        [sg.Button("Save")],
    ]

    window = sg.Window("Image Filter App", layout, size=(450, 500))

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event in ["Load Image", "-EFFECTS-"]:
            apply_effect(values, window)
        if event == "Save" and values["-FILENAME-"]:
            save_image(values)

    window.close()


if __name__ == "__main__":
    main()
