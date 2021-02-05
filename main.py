import numpy
from PIL import Image

#imgArray = numpy.array(Image.open("girlcropped3h.jpg",'r').convert('YCbCr'))
imgArray = numpy.array(Image.open("girlcropped3h.jpg",'r'))
print(imgArray)

outputImage = Image.fromarray(imgArray)
outputImage.save('outputImage.jpeg')
