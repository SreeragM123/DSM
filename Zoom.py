import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt
from PIL import Image
a=Image.open('tree.jpg')
b=np.array(a)
x=ndimage.zoom(b,1)
d=Image.fromarray(x)
plt.imshow(d)