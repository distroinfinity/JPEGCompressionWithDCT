import numpy
from PIL import Image
from scipy.fftpack import dct,idct 

def dct2(a):
    return dct(dct( a.T,norm='ortho' ).T, norm='ortho' )

def idct2(a):
    return idct(idct( a, norm='ortho'),norm='ortho')

a = numpy.array([202,202,202,202,202,202,202,202],
                [202,202,202,202,202,202,202,202],
                [202,202,202,202,202,202,202,202],
                [202,202,202,202,202,202,202,202],
                [202,202,202,202,202,202,202,202],
                [202,202,202,202,202,202,202,202],
                [202,202,202,202,202,202,202,202],
                [202,202,202,202,202,202,202,202])
b=dct2(a)
print(b)
c=idct2(b)
print(c)