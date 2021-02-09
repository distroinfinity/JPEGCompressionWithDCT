import numpy
from PIL import Image
from scipy.fftpack import dct

#Load an image,change colour space from RGB to YCbCr
#and store data in an array

imgArray = numpy.array(Image.open("gr.jpg",'r').convert('YCbCr'))
imgArray = imgArray.astype("float64")

#YCbCr ranges from -127 to 128 unlike RGB which is 0-256
Y=imgArray[:,:,0]-128
#Cb=imgArray[:,:,1]-128
#Cr=imgArray[:,:,2]-128

blockSize=8
imgSize = imgArray.shape
height = imgSize[0]+(8-(imgSize[0]%8))
width = imgSize[1]+(8-(imgSize[1]%8))
dctOutput = numpy.zeros([height,width],float)
for i in range(0,imgSize[0]):
    for j in range(0,imgSize[1]):
        dctOutput[i][j]=Y[i][j]
#print(dctOutput)

#Quantisation matrix for medium compression
"""
qt = numpy.array([[16,11,10,16,24,40,51,61],
                [12,12,14,19,26,58,60,55],
                [14,13,16,24,40,57,69,56],
                [14,17,22,29,51,87,80,62],
                [18,22,37,56,68,109,103,77],
                [24,35,55,64,81,104,113,92],
                [49,64,78,87,103,121,120,101],
                [72,92,95,98,112,100,130,99]])
"""
qt = numpy.array([[3,2,2,3,5,8,10,12],
                    [2,2,3,4,5,12,12,11],
                    [3,3,3,5,8,11,14,11],
                    [3,3,4,6,10,17,16,12],
                    [4,4,7,11,14,22,21,15],
                    [5,7,11,13,16,12,23,18],
                    [10,13,16,17,21,24,24,21],
                    [14,18,19,20,22,20,20,20]])
count=0
print(height," ",width)

for i in range(0,height,8):
    for j in range(0,width,8):
        #performing out-place, for more clearity 
        temp = dctOutput[i:i+8,j:j+8]
        
        #Apply dct on 8x8 matrix
        temp = dct(dct(temp,axis=0,norm='ortho'),axis=1,norm='ortho')
        for k in range(0,8):
            for m in range(0,8):
                temp[k][m]=numpy.round(temp[k][m]/qt[k][m])
        dctOutput[i:i+8,j:j+8] = temp

        count+=1
        print(count)
        #print(temp)

#print(dctOutput)
dctOutput = dctOutput+128
outputImage = Image.fromarray(dctOutput).convert("RGB")
outputImage.save('groutput2.jpg')

"""
print(dctOutput[0:2,0:2])
print(dctOutput[0:2,2:4])
print(dctOutput[2:4,0:2])
"""
#Downsample the colour components by a factor of 2 in both direction
#Cb=Cb[0::2,0::2]
#Cr=Cr[0::2,0::2]




#outputImage = Image.fromarray(imgArray)
#outputImage.save('outputImage.jpeg')
