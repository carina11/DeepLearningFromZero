#画像の表示

import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('lena.png')
plt.imshow(img)
plt.savefig("1-6-3.png")