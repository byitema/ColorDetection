import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

img = cv2.imread('ris1.jpg')

#размеры
height = np.size(img, 0)
width = np.size(img, 1)
pxls = height*width

#стандартные цвета в rgb
blue = [0, 0, 255]
blue_num = 0
light_blue = [0, 255, 255]
light_blue_num = 0
red = [255, 0, 0]
red_num = 0
yellow = [255, 255, 0]
yellow_num = 0
green = [0, 255, 0]
green_num = 0
pink = [255, 0, 255]
pink_num = 0
black = [0, 0, 0]
black_num = 0
white = [255, 255, 255]
white_num = 0

#пофиксить совпадения, которые убираются из-за elif
#считается отклонение от какого стандартного цвета, если цвет рядом, то "приравниваем" к стандартному
def is_Standard(color, standard):
    sqr = math.sqrt(math.pow((standard[0] - color[2]), 2) + math.pow((standard[1] - color[1]), 2) + math.pow((standard[2] - color[0]), 2))
    if sqr < 1.41*255/2:
        return True
    else:
        return False


#проходим по пикселям и сравниваем со стандартными цветами, считаем количество пикселей каждого цвета
for h in range(height):
    for w in range(width):
        bgr = img[h][w]
        if is_Standard(bgr, blue):
            blue_num += 1
        elif is_Standard(bgr, light_blue):
            light_blue_num += 1
        elif is_Standard(bgr, red):
            red_num += 1
        elif is_Standard(bgr, yellow):
            yellow_num += 1
        elif is_Standard(bgr, green):
            green_num += 1
        elif is_Standard(bgr, pink):
            pink_num += 1
        elif is_Standard(bgr, white):
            white_num += 1
        elif is_Standard(bgr, black):
            black_num += 1

#подсчёт процентов
percentages = {
    "blue": blue_num/pxls,
    "light_blue": light_blue_num/pxls,
    "red": red_num/pxls,
    "yellow": yellow_num/pxls,
    "green": green_num/pxls,
    "pink": pink_num/pxls,
    "white": white_num/pxls,
    "black": black_num/pxls,
}

#вывод
for key in percentages.keys():
    print(str(key) + ": " + str(100*percentages.get(key)) + "%")

#вывод изображения
cv2.imshow('', img)
cv2.waitKey()
