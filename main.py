import numpy as np
import cv2
from modules import asNumpyArray, invertImage, toGray
from matplotlib import pyplot
path = "./assets/image.jpeg"
# n_path = "./newimage.jpg"
n_imagem_name = "GrayLion.png"

image = cv2.imread(path)


new_image = toGray(image)
i_image = invertImage(new_image)
# cv2.imwrite(n_imagem_name, asNumpyArray(new_image))

# Mapeia para o mapa de cores que deve usar.
pyplot.imshow(i_image, cmap='gray')
pyplot.show()
# with open(n_path,'w') as file:
#     file.write(new_image.__str__())
