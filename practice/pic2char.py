# -*- coding: utf-8 -*-

from PIL import Image
import argparse

#命令行输入参数管理
parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('--width', type=int, default=80)
parser.add_argument('--height', type=int, default=80)

#获取参数
args = parser.parse_args()
Img = args.file
Width = args.width
Height = args.height
Output = args.output

ascii_char = list(r"$@B%8&WM#*oefhkahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"'^`'. ")


def get_char(r, g, b, alpha=256):
    if not alpha:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    img = Image.open(Img)
    img = img.resize((Width,Height),Image.NEAREST)

    txt = ''

    for i in range(Width):
        for j in range(Height):
            txt += get_char(*img.getpixel((j,i)))
        txt += '\n'

    print(txt)

    if not Output:
        Output = 'output.txt'

    with open(Output, 'w') as f:
        f.write(txt)

