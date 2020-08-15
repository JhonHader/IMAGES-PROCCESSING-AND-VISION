''' Ruler 1         2         3         4         5         6         7        '
/*******************************************************************************
*                                                                              *
*                  /$$      /$$   /$$$$$$   /$$$$$$  /$$   /$$                 *
*                 | $$$    /$$$  /$$__  $$ |_  $$_/ | $$$ | $$                 *
*                 | $$$$  /$$$$ | $$  \ $$   | $$   | $$$$| $$                 *
*                 | $$ $$/$$ $$ | $$$$$$$$   | $$   | $$ $$ $$                 *
*                 | $$  $$$| $$ | $$__  $$   | $$   | $$  $$$$                 *
*                 | $$\  $ | $$ | $$  | $$   | $$   | $$\  $$$                 *
*                 | $$ \/  | $$ | $$  | $$  /$$$$$$ | $$ \  $$                 *
*                 |__/     |__/ |__/  |__/ |______/ |__/  \__/                 *
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

import colorImage as ci
import cv2

#------------------------------------------------------------------------------#
#                                      main                                    #
#------------------------------------------------------------------------------#

if __name__ == '__main__':

    print('Example of how yo have to insert path: C:/Users/Desktop/image.png')
    image = ci.colorImage(input('Insert complete path of image (with filename and format):'))

    # -- Display Properties
    gray_image = image.displayProperties()

    # -- Gray Image
    gray_image = image.makeGray()
    cv2.namedWindow("Gray Scale Image")
    cv2.imshow('Gray Scale Image', gray_image)

    # -- Red Image
    r_image = image.colorsizeRGB('Red')
    cv2.namedWindow("Red Image")
    cv2.imshow('Red Image', r_image)

    # -- Hue Image
    hue_image = image.makeHue()
    cv2.namedWindow("Hue Image")
    cv2.imshow('Hue Image', hue_image)

    cv2.waitKey(0)