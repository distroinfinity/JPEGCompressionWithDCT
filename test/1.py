import numpy
from PIL import Image
from scipy.fftpack import dct,idct

def rgb2ycbcr(im):
    xform = numpy.array([[.299, .587, .114], [-.1687, -.3313, .5], [.5, -.4187, -.0813]])
    ycbcr = im.dot(xform.T)
    ycbcr[:,:,[1,2]] += 128
    
    ycbcr.astype(dtype=numpy.uint8)
    return ycbcr
    #return numpy.uint8(ycbcr)

def ycbcr2rgb(im):
    xform = numpy.array([[1, 0, 1.402], [1, -0.34414, -.71414], [1, 1.772, 0]])
    rgb = im.astype(float)
    rgb[:,:,[1,2]] -= 128
    return rgb.dot(xform.T)
    #return numpy.uint8(rgb.dot(xform.T))

image = Image.open("mybike.jpg",'r')
imgarray = numpy.array(image)
print(imgarray)
imgarray-=128
img1 = rgb2ycbcr(imgarray)

#Image.fromarray(numpy.uint8((img1))).show()
#print(img1)
img2 = ycbcr2rgb(img1)
img2+=128
Image.fromarray(numpy.uint8((img2))).show()
print(img2)