''' Ruler 1         2         3         4         5         6         7        '
/*******************************************************************************
*                                                                              *
*                                       /$$                                    *
*                                      | $$                                    *
*                  /$$$$$$$   /$$$$$$  | $$   /$$$$$$    /$$$$$$               *
*                 /$$_____/  /$$__  $$ | $$  /$$__  $$  /$$__  $$              *
*                | $$       | $$  \ $$ | $$ | $$  \ $$ | $$  \__/              *
*                | $$       | $$  | $$ | $$ | $$  | $$ | $$                    *
*                |  $$$$$$$ |  $$$$$$/ | $$ |  $$$$$$/ | $$                    *
*                 \_______/  \______/  |__/  \______/  |__/                    *
*                                                                              *
*            /$$$$$$                                                           *
*           |_  $$_/                                                           *
*             | $$    /$$$$$$/$$$$    /$$$$$$    /$$$$$$    /$$$$$$            *
*             | $$   | $$_  $$_  $$  |____  $$  /$$__  $$  /$$__  $$           *
*             | $$   | $$ \ $$ \ $$   /$$$$$$$ | $$  \ $$ | $$$$$$$$           *
*             | $$   | $$ | $$ | $$  /$$__  $$ | $$  | $$ | $$_____/           *
*            /$$$$$$ | $$ | $$ | $$ |  $$$$$$$ |  $$$$$$$ |  $$$$$$$           *
*           |______/ |__/ |__/ |__/  \_______/  \____  $$  \_______/           *
*                                               /$$  \ $$                      *
*                                              |  $$$$$$/                      *
*                                               \______/                       *
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

import numpy as np
import cv2
import os

#------------------------------------------------------------------------------#
#                                colorImage CLASS                              #
#------------------------------------------------------------------------------#

class colorImage():

    path = ''
    image = ''

    def __init__(self, input_path):
        self.path = input_path
        self.image = cv2.imread(input_path)

    def displayProperties(self):
        Dimensions = np.array(self.image)
        print('The size of image is: ' + str(Dimensions.shape[0:2]))

    def makeGray(self):
        Gray_Image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        return Gray_Image

    def colorsizeRGB(self, channel):
        if (channel == 'Red') or (channel == 'Green') or (channel =='Blue'):
            img = self.image
            if channel == 'Blue':
                b = img.copy()
                b[:, :, 1] = 0
                b[:, :, 2] = 0
                return b
            elif channel == 'Green':
                g = img.copy()
                g[:, :, 0] = 0
                g[:, :, 2] = 0
                return g
            else:
                r = img.copy()
                r[:, :, 0] = 0
                r[:, :, 1] = 0
                return r
        else:
            return print('Invalid channel!')

    def makeHue(self):
        HSV_Image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        HSV_Image[:, :, 1] = 255
        HSV_Image[:, :, 2] = 255
        Tones_Image = cv2.cvtColor(self.image, cv2.COLOR_HSV2BGR)
        return Tones_Image
