import numpy as np
from PIL import Image
from scipy import ndimage
from matplotlib import pyplot as plt

a = Image.open('tree.jpg')
angle_degrees = 90
rotated_image = ndimage.rotate(a, angle_degrees)

plt.imshow(rotated_image)