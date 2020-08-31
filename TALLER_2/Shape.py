''' Ruler 1         2         3         4         5         6         7        '
/*******************************************************************************
*                                                                              *
*             /$$                                                              *
*            |__/                                                              *
*             /$$  /$$$$$$/$$$$    /$$$$$$    /$$$$$$    /$$$$$$               *
*            | $$ | $$_  $$_  $$  |____  $$  /$$__  $$  /$$__  $$              *
*            | $$ | $$ \ $$ \ $$   /$$$$$$$ | $$  \ $$ | $$$$$$$$              *
*            | $$ | $$ | $$ | $$  /$$__  $$ | $$  | $$ | $$_____/              *
*            | $$ | $$ | $$ | $$ |  $$$$$$$ |  $$$$$$$ |  $$$$$$$              *
*            |__/ |__/ |__/ |__/  \_______/  \____  $$  \_______/              *
*                                            /$$  \ $$                         *
*                                           |  $$$$$$/                         *
*                                            \______/                          *
*              /$$$$$$   /$$                                                   *
*             /$$__  $$ | $$                                                   *
*            | $$  \__/ | $$$$$$$    /$$$$$$    /$$$$$$    /$$$$$$             *
*            |  $$$$$$  | $$__  $$  |____  $$  /$$__  $$  /$$__  $$            *
*             \____  $$ | $$  \ $$   /$$$$$$$ | $$  \ $$ | $$$$$$$$            *
*             /$$  \ $$ | $$  | $$  /$$__  $$ | $$  | $$ | $$_____/            *
*            |  $$$$$$/ | $$  | $$ |  $$$$$$$ | $$$$$$$/ |  $$$$$$$            *
*             \______/  |__/  |__/  \_______/ | $$____/   \_______/            *
*                                             | $$                             *
*                                             | $$                             *
*                                             |__/                             *
*                                                                              *
*                  Developed by:                                               *
*                                                                              *
*                            Jhon Hader Fernandez                              *
*                     - jhon_fernandez@javeriana.edu.co                        *
*                                                                              *
*                       Pontificia Universidad Javeriana                       *
*                            Bogota DC - Colombia                              *
*                                  Aug - 2020                                  *
*                                                                              *
*****************************************************************************'''

#------------------------------------------------------------------------------#
#                          IMPORT MODULES AND LIBRARIES                        #
#------------------------------------------------------------------------------#

import math
import numpy as np
import cv2

#------------------------------------------------------------------------------#
#                                imageShape CLASS                              #
#------------------------------------------------------------------------------#

class imageShape():

    width = 0
    height = 0

    #Miembros privados
    __shape = []
    __color = (0, 0, 0)
    __name = ''

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__color = (255, 255, 0)

    def generateShape(self):
        figure = np.random.randint(0, 4)
        zeros = np.zeros((self.width, self.height, 3), np.uint8)
        if figure == 0:
            self.__shape = self.__triangle(zeros)
            self.__name = "Triangle"
        elif figure == 1:
            self.__shape = self.__square(zeros)
            self.__name = "Square"
        elif figure == 2:
            self.__shape = self.__rectangle(zeros)
            self.__name = "Rectangle"
        else:
            self.__shape = self.__circle(zeros)
            self.__name = "Circle"

    # Los metodo privados se utilizan para generar una respectiva figura
    # todos reciben como parametro una imagen en negro, y retorna una ima-
    # gen del mismo tamano con la respectiva figura dibujada

    #Metodo privado para generar cuadrado a 45°
    def __square(self, img):
        lado = int(min(self.width, self.height)/2)
        angle = 45
        x0 = int((self.height/2) - (lado/2))
        y0 = int((self.width/2) - (lado/2))
        xf = int((self.height/2) + (lado/2))
        yf = int((self.width/2) + (lado/2))
        square_img = cv2.rectangle(img, (x0, y0), (xf, yf), self.__color, 2)
        rot_mat = cv2.getRotationMatrix2D((self.height/2, self.width/2),angle,1.0)
        new_image = cv2.warpAffine(img, rot_mat, (self.height, self.width))
        return new_image

    # Metodo privado para generar circulo
    def __circle(self, img):
        radio = int(min(self.width, self.height) / 4)
        x0 = int(self.height/2)
        y0 = int(self.width/2)
        circle_image = cv2.circle(img, (x0, y0), radio, self.__color, 2)
        return circle_image

    # Metodo privado para generar rectangulo
    def __rectangle(self, img):
        lado_horizontal = int(self.width / 2)
        lado_vertical = int(self.height / 2)
        x0 = int((self.height / 2) - (lado_vertical / 2))
        y0 = int((self.width / 2) - (lado_horizontal / 2))
        xf = int((self.height / 2) + (lado_vertical / 2))
        yf = int((self.width / 2) + (lado_horizontal / 2))
        rect_img = cv2.rectangle(img, (x0, y0), (xf, yf), self.__color, 2)
        return rect_img

    # Metodo privado para generar triangulo equilatero
    def __triangle(self, img):
        lado = int(min(self.width, self.height) / 2)
        angle = 45
        h = int((math.sqrt(3)*lado)/2)
        x0 = int((self.height/2) - (lado/2))
        y0 = int((self.width/2) + (h/2))
        x1 = int((self.height/2) + (lado/2))
        y1 = int((self.width/2) + (h/2))
        x2 = int((self.height/2))
        y2 = int((self.width/2) - (h/2))
        square_img = cv2.line(img, (x0, y0), (x1, y1), self.__color, 2)
        square_img = cv2.line(img, (x1, y1), (x2, y2), self.__color, 2)
        square_img = cv2.line(img, (x2, y2), (x0, y0), self.__color, 2)
        return square_img

    def showShape(self):
        if not len(self.__shape):
            zeros = np.zeros((self.width, self.height, 3), np.uint8)
            cv2.namedWindow("Shape")
            cv2.imshow("Shape", zeros)
        else:
            cv2.namedWindow("Shape")
            cv2.imshow("Shape", self.__shape)

        cv2.waitKey(5000)


    def getShape(self):
        return [self.__shape, self.__name]

    def whatShape(self, img):
        my_img = img.copy()
        img_gray = cv2.cvtColor(my_img, cv2.COLOR_BGR2GRAY)

        # Umbralizar y binarizar componente B y G, pues Cyan = B + G
        ret, bw_B_mask = cv2.threshold(my_img[:, :, 0], 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        ret, bw_G_mask = cv2.threshold(my_img[:, :, 1], 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Combinacion de mascara binaria de B y G
        bw_mask = bw_G_mask & bw_B_mask

        # Cambio de espacio de color a HSV
        hsv_img = cv2.cvtColor(my_img, cv2.COLOR_BGR2HSV)

        # Histograma a la componente S con la mascara binaria "bw_mask"
        hist_hsv = cv2.calcHist([hsv_img[:,:,1]], [0], bw_mask, [180], [0, 180])
        max_pos = int(hist_hsv.argmax())

        # Binarizacion
        Shape_mask = cv2.inRange(my_img, (max_pos - 10, 0, 0), (max_pos + 10, 255, 255))
        Shape_mask = cv2.bitwise_not(Shape_mask)

        # Encontrar contornos
        contours, hierarchy = cv2.findContours(Shape_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        image_draw = my_img.copy()

        # Aproximacion de contornos a poli-lineas y evaluacion de las mismas
        for cnt in contours:
            font = cv2.FONT_HERSHEY_COMPLEX
            color = (0, 255, 255)
            white = (255, 255, 255)
            cv2.drawContours(image_draw, [cnt], 0, color, 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            if len(approx) == 3:
                cv2.putText(image_draw, "Triangle", (x,y), font, 1, white)
                cv2.imshow('Shape', image_draw)
                cv2.waitKey(2000)
                return "Triangle"

            elif len(approx) == 4:

                # compute the bounding box of the contour and use the
                # bounding box to compute the aspect ratio
                (x, y, w, h) = cv2.boundingRect(approx)
                ar = w / float(h)
                # a square will have an aspect ratio that is approximately
                # equal to one, otherwise, the shape is a rectangle
                shape = "Square" if ar >= 0.95 and ar <= 1.05 else "Rectangle"

                if shape == "Square":
                    cv2.putText(image_draw, "Square", (x, y), font, 1, white)
                    cv2.imshow('Shape', image_draw)
                    cv2.waitKey(2000)
                else:
                    cv2.putText(image_draw, "Rectangle", (x, y), font, 1, white)
                    cv2.imshow('Shape', image_draw)
                    cv2.waitKey(2000)
                return shape

            else:
                cv2.putText(image_draw, "Circle", (x, y), font, 1, white)
                cv2.imshow('Shape', image_draw)
                cv2.waitKey(2000)
                return "Circle"