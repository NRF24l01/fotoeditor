# импортируем библиотеку
from PIL import Image
import random

def blasck_white(img):
    # цикл по всем пикселям
    # img.width - ширина картинки
    # img.height - высота картинки
    for i in range(img.width):
        for j in range(img.height):
            # получаем цвет
            r, g, b = img.getpixel((i, j))

            in1 = r + g + b
            # in12 = in1 / 3.0
            # print(type(in1))
            in12 = int(in1 / 3)

            r = in12
            g = in12
            b = in12

            # сохраняем пиксель обратно
            img.putpixel((i, j), (r, g, b))
    return img

def gren_narko(img):

    cr = 100
    cl1r = 100
    cl1g = 123
    cl1b = 124
    cl2r = 0
    cl2g = 173
    cl2b = 1

    # цикл по всем пикселям
    # img.width - ширина картинки
    # img.height - высота картинки
    for i in range(img.width):
        for j in range(img.height):
            # получаем цвет
            r, g, b = img.getpixel((i, j))

            in1 = r + g + b
            # in12 = in1 / 3.0
            # print(type(in1))
            in12 = int(in1 / 3)

            if in12 > cr:
                img.putpixel((i, j), (cl1b, cl1g, cl1r))
            else:
                img.putpixel((i, j), (cl2b, cl2g, cl2r))

            # r = in12
            # g = in12
            # b = in12

            # сохраняем пиксель обратно
            # img.putpixel((i, j), (r, g, b))

    return img

def noise(img):

    # цикл по всем пикселям
    # img.width - ширина картинки
    # img.height - высота картинки
    for i in range(img.width):
        for j in range(img.height):
            # получаем цвет
            r, g, b = img.getpixel((i, j))

            # in1 = r + g + b
            # in12 = in1 / 3.0
            # print(type(in1))
            # in12 = int(in1 / 3)
            noize = random.randint(0, 20)
            r += noize
            g += noize
            b += noize
            if r > 255:
                r1 = r - 255
                r = r1
                if r > 255:
                    r1 = r - 255
                    r = r1
            elif g > 255:
                g1 = g - 255
                g = g1
                if g > 255:
                    g1 = g - 255
                    g = g1
            elif b > 255:
                b1 = b - 255
                b = b1
                if g > 255:
                    b1 = b - 255
                    b = g1

            # сохраняем пиксель обратно
            img.putpixel((i, j), (r, g, b))

    return img

def color_noise(img):
    # цикл по всем пикселям
    # img.width - ширина картинки
    # img.height - высота картинки
    for i in range(img.width):
        for j in range(img.height):
            # получаем цвет
            r, g, b = img.getpixel((i, j))

            # in1 = r + g + b
            # in12 = in1 / 3.0
            # print(type(in1))
            # in12 = int(in1 / 3)
            r += random.randint(0, 25)
            g += random.randint(0, 25)
            b += random.randint(0, 25)
            if r > 255:
                r1 = r - 255
                r = r1
                if r > 255:
                    r1 = r - 255
                    r = r1
            elif g > 255:
                g1 = g - 255
                g = g1
                if g > 255:
                    g1 = g - 255
                    g = g1
            elif b > 255:
                b1 = b - 255
                b = b1
                if g > 255:
                    b1 = b - 255
                    b = g1

            # сохраняем пиксель обратно
            img.putpixel((i, j), (r, g, b))
    return img

def hetvertirovanie(img):
    for i in range(img.width // 2, img.width):
        for j in range(img.height // 2):
            r, g, b = img.getpixel((i, j))
            r = r + 256
            img.putpixel((i, j), (r, g, b))
    for i in range(img.width // 2, img.width):
        for j in range(img.height // 2, img.height):
            r, g, b = img.getpixel((i, j))
            g = g + 256
            img.putpixel((i, j), (r, g, b))
    for i in range(img.width // 2):
        for j in range(img.height // 2, img.height):
            r, g, b = img.getpixel((i, j))
            b = b + 256
            img.putpixel((i, j), (r, g, b))
    return img

def kek(img):
    for i in range(img.width // 2):
        for j in range(img.height):
            r, g, b = img.getpixel((i, j))
            img.putpixel((img.width - i - 1, j), (r, g, b))
    return img

def razm(img):
    img2 = img.copy()
    for km in range(1, 10):
        for i in range(1, img.width - 1):
            for j in range(1, img.height - 1):
                r, g, b = img2.getpixel((i, j))
                r1, g1, b1 = img2.getpixel((i - 1, j - 1))
                r2, g2, b2 = img2.getpixel((i - 1, j + 1))
                r3, g3, b3 = img2.getpixel((i - 1, j))
                r4, g4, b4 = img2.getpixel((i + 1, j))
                r5, g5, b5 = img2.getpixel((i + 1, j + 1))
                r6, g6, b6 = img2.getpixel((i + 1, j - 1))
                r7, g7, b7 = img2.getpixel((i, j - 1))
                r8, g8, b8 = img2.getpixel((i, j + 1))
                r = round((r * 1 + r1 * 0.5 + r3 * 0.75 + r4 * 0.75 + r7 * 0.75 + r8 * 0.75 + r2 * 0.5 + r5 * 0.5 + r6 * 0.5) / 6)
                g = round((g * 1 + g1 * 0.5 + g3 * 0.75 + g4 * 0.75 + g7 * 0.75 + g8 * 0.75 + g2 * 0.5 + g5 * 0.5 + g6 * 0.5) / 6)
                b = round((b * 1 + b1 * 0.5 + b3 * 0.75 + b4 * 0.75 + b7 * 0.75 + b8 * 0.75 + b2 * 0.5 + b5 * 0.5 + b6 * 0.5) / 6)
                img.putpixel((i, j), (r, g, b))
    return img

def rezk(img):
    img2 = img.copy()
    for i in range(1, img.width - 1):
        for j in range(1, img.height - 1):
            r, g, b = img2.getpixel((i, j))
            r1, g1, b1 = img2.getpixel((i - 1, j - 1))
            r2, g2, b2 = img2.getpixel((i - 1, j + 1))
            r3, g3, b3 = img2.getpixel((i - 1, j))
            r4, g4, b4 = img2.getpixel((i + 1, j))
            r5, g5, b5 = img2.getpixel((i + 1, j + 1))
            r6, g6, b6 = img2.getpixel((i + 1, j - 1))
            r7, g7, b7 = img2.getpixel((i, j - 1))
            r8, g8, b8 = img2.getpixel((i, j + 1))
            r = round((r * 9 + r1 * (-1) + r3 * (-1) + r4 * (-1) + r7 * (-1) + r8 * (-1) + r2 * (-1) + r5 * (
                -1) + r6 * (-1)) / 1)
            g = round((g * 9 + g1 * (-1) + g3 * (-1) + g4 * (-1) + g7 * (-1) + g8 * (-1) + g2 * (-1) + g5 * (
                -1) + g6 * (-1)) / 1)
            b = round((b * 9 + b1 * (-1) + b3 * (-1) + b4 * (-1) + b7 * (-1) + b8 * (-1) + b2 * (-1) + b5 * (
                -1) + b6 * (-1)) / 1)
            img.putpixel((i, j), (r, g, b))
    img.show()