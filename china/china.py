import cv2
import numpy as np
import matplotlib.pyplot as plt

class ImageModel(object):
    #чёрная маска
    lower_black = np.array([0,0,0])
    upper_black = np.array([179,255,25])

    #серая маска
    lower_gray = np.array([0,0,26])
    upper_gray = np.array([179,38,165])

    #белая маска
    lower_white = np.array([0,0,166])
    upper_white = np.array([179,38,255])

    #красная маска 1
    lower_red1 = np.array([0,45,26])
    upper_red1 = np.array([10,255,255])

    #красная маска 2
    lower_red2 = np.array([170,45,26])
    upper_red2 = np.array([179,255,255])

    #розовая маска 1
    lower_pink1 = np.array([0,39,26])
    upper_pink1 = np.array([10,44,255])

    #розовая маска 2
    lower_pink2 = np.array([170,39,26])
    upper_pink2 = np.array([179,44,255])

    #розовая маска 3
    lower_pink3 = np.array([156,39,26])
    upper_pink3 = np.array([169,255,255])

    #оранжевая маска
    lower_orange = np.array([11,39,192])
    upper_orange = np.array([22,255,255])

    #коричневая маска
    lower_brown = np.array([6,39,26])
    upper_brown = np.array([22,255,191])

    #жёлтая маска
    lower_yellow = np.array([23,39,26])
    upper_yellow = np.array([32,255,255])

    #зелёная маска
    lower_green = np.array([33,39,26])
    upper_green = np.array([75,255,255])

    #циановая маска
    lower_cyan = np.array([76,39,26])
    upper_cyan = np.array([90,255,255])

    #синяя маска
    lower_blue = np.array([91,39,26])
    upper_blue = np.array([127,255,255])

    #фиолетовая маска
    lower_purple = np.array([128,128,26])
    upper_purple = np.array([155,255,255])

    #светло-фиолетовая маска
    lower_light_purple = np.array([128,39,26])
    upper_light_purple = np.array([155,127,255])

    #ищет количество пикселей удовлетворяющих маске
    def pxls_num(self, low, up):
        num = 0
        height = np.size(self.img_hsv, 0)
        width = np.size(self.img_hsv, 1)

        mask = cv2.inRange(self.img_hsv, low, up)

        for h in range(height):
            for w in range(width):
                if mask[h][w] == 255:
                    num = num + 1

        return num

    #построение модели
    def __init__(self, img):
        self.img = img
        self.img_hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

        self.pxls = np.size(self.img_hsv, 0) * np.size(self.img_hsv, 1)

        self.black_num = 100*self.pxls_num(self.lower_black, self.upper_black)/self.pxls
        self.gray_num = 100*self.pxls_num(self.lower_gray, self.upper_gray)/self.pxls
        self.white_num = 100*self.pxls_num(self.lower_white, self.upper_white)/self.pxls
        self.red_num = 100*(self.pxls_num(self.lower_red1, self.upper_red1) + self.pxls_num(self.lower_red2, self.upper_red2))/self.pxls
        self.pink_num = 100*(self.pxls_num(self.lower_pink1, self.upper_pink1) + self.pxls_num(self.lower_pink2, self.upper_pink2) + self.pxls_num(self.lower_pink3, self.upper_pink3))/self.pxls
        self.orange_num = 100*self.pxls_num(self.lower_orange, self.upper_orange)/self.pxls
        self.brown_num = 100*self.pxls_num(self.lower_brown, self.upper_brown)/self.pxls
        self.yellow_num = 100*self.pxls_num(self.lower_yellow, self.upper_yellow)/self.pxls
        self.green_num = 100*self.pxls_num(self.lower_green, self.upper_green)/self.pxls
        self.cyan_num = 100*self.pxls_num(self.lower_cyan, self.upper_cyan)/self.pxls
        self.blue_num = 100*self.pxls_num(self.lower_blue, self.upper_blue)/self.pxls
        self.purple_num = 100*self.pxls_num(self.lower_purple, self.upper_purple)/self.pxls
        self.light_purple_num = 100*self.pxls_num(self.lower_light_purple, self.upper_light_purple)/self.pxls

    #вывод модели
    def model(self):
        #вывод процентов
        percentages = {
            "black": self.black_num,
            "gray": self.gray_num,
            "white": self.white_num,
            "red": self.red_num,
            "pink": self.pink_num,
            "orange": self.orange_num,
            "brown": self.brown_num,
            "yellow": self.yellow_num,
            "green": self.green_num,
            "cyan": self.cyan_num,
            "blue": self.blue_num,
            "purple": self.purple_num,
            "light-purple": self.light_purple_num,
        }

        for key in percentages.keys():
            if percentages.get(key) != 0:
                print(str(key) + ": " + str(percentages.get(key)) + "%")

    #оператор "равно"
    def __eq__(self, other):
        return self.black_num == other.black_num and\
               self.gray_num == other.gray_num and\
               self.white_num == other.white_num and\
               self.red_num == other.red_num and\
               self.pink_num == other.pink_num and\
               self.orange_num == other.orange_num and\
               self.brown_num == other.brown_num and\
               self.yellow_num == other.yellow_num and\
               self.green_num == other.green_num and\
               self.cyan_num == other.cyan_num and\
               self.blue_num == other.blue_num and\
               self.purple_num == other.purple_num and\
               self.light_purple_num == other.light_purple_num

if __name__ == "__main__":
    print("      Распознавание объекта по его цветовой модели      ")
    print("--------------------------------------------------------")

    print("Подготовка моделей входных изображений...")

    rKits = []
    for i in range(6):
        rKit = ImageModel(cv2.imread("rKit" + str(i+1) + ".jpg"))
        rKits.append(rKit)
        print("\nМодель входного изображения №" + str(i+1) + ":")
        rKit.model()

    print("--------------------------------------------------------")
    print("Анализ моделей...")

    for i in range(6):
        if (rKits[i].brown_num + rKits[i].red_num) >= 1 and (rKits[i].brown_num + rKits[i].red_num) <= 5:
            print("\nНа изображении №" + str(i+1) + " наблюдается серьёзное загрязнение в начальной стадии.")
            img = cv2.imread("rKit" + str(i+1) + ".jpg")
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            plt.figure(num = "Изображение №" + str(i+1))
            plt.imshow(img)
            plt.show()

    print("--------------------------------------------------------")
    print("                  (C)Artem Bulakh, 2020                 ")
