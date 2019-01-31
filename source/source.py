# -------------------------------------------------------------------------------------------------------------------- #
#                                               Creator: Chu Quang Huy
#                                           Nagaoka University of Technology
#                                                Created in 2019/01/18
# -------------------------------------------------------------------------------------------------------------------- #


# ---------------------------------------------------*** BEGIN ***------------------------------------------------------

# --------------------------------------------*** IMPORT MODULES PART ***-----------------------------------------------

import re
from PIL import ImageFont, ImageDraw, Image, ImageOps
import numpy as np
import cv2
import os


# --------------------------------------------*** MAIN FUNCTION PART ***------------------------------------------------

main_directory = os.path.normpath(os.getcwd() + os.sep + os.pardir)


def main():
    text_name = input('Enter text file name:')
    print('\n')
    print('User chose: ' + text_name + '.txt')
    print('\n')
    file_text_name = text_name.strip() + '.txt'
    data_package = text_image(file_text_name)
    merge_image(data_package)


# ----------------------------------------*** TEXT TO IMAGE CONVERT PART ***--------------------------------------------


def text_image(file_text_name, font_path=None):

    text_folder = main_directory + '\Text'
    if os.path.isfile(os.path.join(text_folder, file_text_name)):
        print("Found " + file_text_name)
        print('\n')
        path = os.path.join(text_folder, file_text_name)
    else:
        print("Could not found any file name: " + file_text_name)

    # ----------------------------||| Define empty data for format and content |||-----------------------

    Font_Color = []
    Background_Color = []
    Content_Data = []
    Image_Source_Package = []
    Image_Data_Package = []
    max_height = 0

    # --------------------------------------||| Analyze function part |||---------------------------------

    def analyze(data):
        edit = re.search(r'<edit:\sc=(\w+),\sb=(\w+)>', data)
        font_color = edit.group(1)
        background_color = edit.group(2)
        content_search = re.search(r'>(.+?)<', data)
        content_data = content_search.group(1)
        return font_color, background_color, content_data

    # ----------------------------||| Open text file and split into small element |||---------------------

    with open(path, 'r+', encoding='utf-8') as tf:
        for line in tf:
            print('Raw_Data: ' + line)
            print('\n')
            splits = re.findall(r'<.+?>.+?<@.+?>', line)
            if splits:
                print('Split into separated part: ' + str(splits))
                print('\n')
            else:
                print()

    # -----------------------------||| Put every element into corresponding lists |||---------------------

    for i in range(len(splits)):
        font_color, background_color, content_data = analyze(splits[i])
        Font_Color.append(font_color)
        Background_Color.append(background_color)
        Content_Data.append(content_data)

    print('Font Color: ' + str(Font_Color))
    print('Background Color: ' + str(Background_Color))
    print('Content Data: ' + str(Content_Data))
    print('\n')

    # -------------------------------------------||| Convert part |||-------------------------------------

    font_size = 40
    font_path = font_path or 'NotoSansCJKjp-Black.otf' or 'NotoSans-Black.ttf' or 'NotoSansCJKkr-Black.otf' or 'NotoSansCJKsc-Black.otf' or 'NotoSansCJKtc-Black.otf'
    try:
        font = ImageFont.truetype(font_path, size=font_size)
    except IOError:
        font = ImageFont.load_default()
        print('Could not use current font, apply default font')

    for i in range(len(Content_Data)):
        height = font.getsize(Content_Data[i])[1]
        if max_height <= height:
            max_height = height

    for i in range(len(Content_Data)):
        width = font.getsize(Content_Data[i])[0] - 3
        vertical_position = 0
        horizontal_position = -2
        image = Image.new('RGBA', (width, max_height), Background_Color[i])
        draw = ImageDraw.Draw(image)
        draw.text((horizontal_position, vertical_position), Content_Data[i], fill=Font_Color[i], font=font)
        pic_name = file_text_name[:-4] + 'pic' + str(i) + '.bmp'
        shattered_directory = os.path.join(main_directory + '\Shattered Images', pic_name)
        image.save(shattered_directory)
        Image_Source_Package.append(shattered_directory)
        Image_Data_Package.append(cv2.imread(Image_Source_Package[i]))

    return Image_Data_Package

# ---------------------------------------------*** MERGE IMAGE PART ***-------------------------------------------------


def merge_image(data_package):
    complete_directory = main_directory + '\Complete Images'
    merge = np.concatenate(data_package, axis=1)
    file_save = input('Name for result image:')
    print('\n')
    print('Image will be saved at: ' + file_save )
    print('\n')
    image_file_save_name = file_save.strip()
    cv2.imwrite(os.path.join(complete_directory, image_file_save_name), merge)


# --------------------------------------------*** EXECUTE THIS CODE ***-------------------------------------------------


if __name__ == '__main__':
    main()
    print('IMPORT SUCCESS')
    os.system("PAUSE")


# ---------------------------------------------------*** END ***--------------------------------------------------------
