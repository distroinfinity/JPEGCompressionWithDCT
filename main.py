import numpy
from PIL import Image

#Load an image,change colour space from RGB to YCbCr
#and store data in an array
imgArray = numpy.array(Image.open("girlcropped6.jpg",'r').convert('YCbCr'))
imgArray = imgArray.astype("float64")
#imgArray = numpy.array(Image.open("girlcropped3h.jpg",'r'))
print(imgArray)

#YCbCr ranges from -127 to 128 unlike RGB which is 0-256
Y=imgArray[:,:,0]-128
Cb=imgArray[:,:,1]-128
Cr=imgArray[:,:,2]-128

#Downsample the colour components by a factor of 2 in both direction
Cb=Cb[0::2,0::2]
Cr=Cr[0::2,0::2]

print("Y",Y)
print("Cb",Cb)
print("Cr",Cr)

#outputImage = Image.fromarray(imgArray)
#outputImage.save('outputImage.jpeg')
