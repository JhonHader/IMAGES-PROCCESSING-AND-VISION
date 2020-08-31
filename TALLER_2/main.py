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

import Shape


#------------------------------------------------------------------------------#
#                                      main                                    #
#------------------------------------------------------------------------------#

if __name__ == '__main__':

    #Ingresar dimensiones de la imagen
    x = int(input("Ingrese width: "))
    y = int(input("Ingrese height: "))
    print("Dimensiones ingresadas:", (x, y))

    #Uso de la clase imageShape
    img = Shape.imageShape(x,y)

    #Generar figura y visualizar por 5 segundos
    img.generateShape()
    img.showShape()

    #Obtencion y clasificacion
    img_genarated, name = img.getShape()
    shape = img.whatShape(img_genarated)
    print("Su figura es: ", shape)

    #Validacion de la clasificacion
    validation = "Correct" if name == shape else "Incorrect"
    print("Classfied was: " + validation)