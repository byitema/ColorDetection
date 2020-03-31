import cv2
import numpy as np

#ищет количество пикселей удовлетворяющих маске
def pxls_num(mask):
    num = 0
    height = np.size(mask, 0)
    width = np.size(mask, 1)
    
    for h in range(height):
	    for w in range(width):
		    if mask[h][w] == 255:
			    num = num + 1
    
    return num

#считываем изображение
img = cv2.imread('ris1.jpg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#размеры
height = np.size(img, 0)
width = np.size(img, 1)
pxls = height*width

#чёрная маска
lower_black = np.array([0,0,0])
upper_black = np.array([250,255,30])
mask = cv2.inRange(img_hsv, lower_black, upper_black)
black_num = pxls_num(mask)

#белая маска
lower_white = np.array([0,0,255])
upper_white = np.array([0,0,255])
mask = cv2.inRange(img_hsv, lower_white, upper_white)
white_num = pxls_num(mask)

#красная маска
lower_red = np.array([0,150,50])
upper_red = np.array([10,255,255])
mask = cv2.inRange(img_hsv, lower_red, upper_red)
red_num = pxls_num(mask)

#зелёная маска
lower_green = np.array([45,150,50])
upper_green = np.array([65,255,255])
mask = cv2.inRange(img_hsv, lower_green, upper_green)
green_num = pxls_num(mask)

#жёлтая маска
lower_yellow = np.array([25,150,50])
upper_yellow = np.array([35,255,255])
mask = cv2.inRange(img_hsv, lower_yellow, upper_yellow)
yellow_num = pxls_num(mask)

#оранжевая маска
lower_orange = np.array([15,150,0])
upper_orange = np.array([25,255,255])
mask = cv2.inRange(img_hsv, lower_orange, upper_orange)
orange_num = pxls_num(mask)

#тёмно-синяя маска
lower_dark_blue = np.array([115,150,0])
upper_dark_blue = np.array([125,255,255])
mask = cv2.inRange(img_hsv, lower_dark_blue, upper_dark_blue)
dark_blue_num = pxls_num(mask)

#циановая маска
lower_cyan = np.array([85,150,0])
upper_cyan = np.array([95,255,255])
mask = cv2.inRange(img_hsv, lower_cyan, upper_cyan)
cyan_num = pxls_num(mask)

#светло-синяя маска
lower_light_blue = np.array([95,150,0])
upper_light_blue = np.array([110,255,255])
mask = cv2.inRange(img_hsv, lower_light_blue, upper_light_blue)
light_blue_num = pxls_num(mask)

#тёмно-розовая маска
lower_dark_pink = np.array([160,150,0])
upper_dark_pink = np.array([170,255,255])
mask = cv2.inRange(img_hsv, lower_dark_pink, upper_dark_pink)
dark_pink_num = pxls_num(mask)

#розовая маска
lower_pink = np.array([145,150,0])
upper_pink = np.array([155,255,255])
mask = cv2.inRange(img_hsv, lower_pink, upper_pink)
pink_num = pxls_num(mask)

#подсчёт процентов
percentages = {
    "black": black_num/pxls,
    "white": white_num/pxls,
    "red": red_num/pxls,
    "green": green_num/pxls,
    "yellow": yellow_num/pxls,
    "orange": orange_num/pxls,
    "dark-blue": dark_blue_num/pxls,
    "cyan": cyan_num/pxls,
    "light-blue": light_blue_num/pxls,
    "dark-pink": dark_pink_num/pxls,
    "pink": pink_num/pxls,
}

#вывод
for key in percentages.keys():
    print(str(key) + ": " + str(100*percentages.get(key)) + "%")

cv2.imshow('', img)
cv2.waitKey()
