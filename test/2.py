import numpy as np
from PIL import Image

array = np.zeros([8,8, 3], dtype=np.uint8)
array[:,:] = [255, 128, 0] #Orange left side
#array[:,3:] = [0, 0, 255]   #Blue right side

img = Image.fromarray(array)
img.save('testrgb.jpg')