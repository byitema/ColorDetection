import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

img = cv2.imread('ris1.jpg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#размеры
height = np.size(img, 0)
width = np.size(img, 1)
pxls = height*width

#границы цветов в HSV

lower_white = np.array([0,0,255])
upper_white = np.array([0,0,255])
mask = cv2.inRange(img_hsv, lower_white, upper_white)
img_white = cv2.bitwise_and(img_hsv, img_hsv, mask = mask)

white_num = 0
for h in range(height):
	for w in range(width):
		if img_hsv[h][w][0] != 0 and img_hsv[h][w][1] != 0 and img_hsv[h][w][2] != 0:
			white_num = white_num + 1

lower_red = np.array([0,150,50])
upper_red = np.array([10,255,255])
mask = cv2.inRange(img_hsv, lower_red, upper_red)
img_red = cv2.bitwise_and(img_hsv, img_hsv, mask = mask)

lower_green = np.array([45,150,50])
upper_green = np.array([65,255,255])
mask = cv2.inRange(img_hsv, lower_green, upper_green)
img_green = cv2.bitwise_and(img_hsv, img_hsv, mask = mask)

lower_yellow = [25,150,50]
upper_yellow = [35,255,255]
yellow_num = 0

lower_light_blue = [95,150,0]
upper_light_blue = [110,255,255]
light_blue_num = 0

lower_orange = [15,150,0]
upper_orange = [25,255,255]
orange_num = 0

lower_dark_pink = [160,150,0]
upper_dark_pink = [170,255,255]
dark_pink_num = 0

lower_pink = [145,150,0]
upper_pink = [155,255,255]
pink_num = 0

lower_cyan = [85,150,0]
upper_cyan = [95,255,255]
cyan_num = 0

lower_dark_blue = [115,150,0]
upper_dark_blue = [125,255,255]
dark_blue_num = 0

'''
lower_black = np.array([0,0,0])
upper_black = np.array([250,255,30])
mask = cv2.inRange(img_hsv, lower_black, upper_black)
img_black = cv2.bitwise_and(img_hsv, img_hsv, mask = mask)
'''
black_num = pxls
'''
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
'''

print(white_num/pxls)

#вывод изображения
img_white = cv2.cvtColor(img_white, cv2.COLOR_HSV2BGR)
cv2.imshow('', img_white)
cv2.waitKey()