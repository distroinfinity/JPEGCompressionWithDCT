import numpy
from PIL import Image
from scipy.fftpack import dct,idct

def quantisation(k):
    #Quantisation table for Y component
    Q10 = numpy.array([[80,60,50,80,120,200,255,255],
                [55,60,70,95,130,255,255,255],
                [70,65,80,120,200,255,255,255],
                [70,85,110,145,255,255,255,255],
                [90,110,185,255,255,255,255,255],
                [120,175,255,255,255,255,255,255],
                [245,255,255,255,255,255,255,255],
                [255,255,255,255,255,255,255,255]])

    Q50 = numpy.array([[16,11,10,16,24,40,51,61],
                [12,12,14,19,26,58,60,55],
                [14,13,16,24,40,57,69,56],
                [14,17,22,29,51,87,80,62],
                [18,22,37,56,68,109,103,77],
                [24,35,55,64,81,104,113,92],
                [49,64,78,87,103,121,120,101],
                [72,92,95,98,112,100,130,99]])

    Q90 = numpy.array([[3,2,2,3,5,8,10,12],
                    [2,2,3,4,5,12,12,11],
                    [3,3,3,5,8,11,14,11],
                    [3,3,4,6,10,17,16,12],
                    [4,4,7,11,14,22,21,15],
                    [5,7,11,13,16,12,23,18],
                    [10,13,16,17,21,24,24,21],
                    [14,18,19,20,22,20,20,20]])
    if k == "Q10":
        return Q10
    elif k == "Q50":
        return Q50
    elif k == "Q90":
        return Q90
    

if __name__ == "__main__":
    #load image & convert to YCbCr colourspcae
    imgArray = numpy.array(Image.open("grcropped.jpg",'r').convert('YCbCr'))
    imgArray = imgArray.astype("float64")

    #centre pixel values around 0
    imgArray=imgArray[:,:,0]-128
    #Cb=imgArray[:,:,1]-128
    #Cr=imgArray[:,:,2]-128

    blockSize=8
    imgSize = imgArray.shape
    #make height and width a multiple of 8
    height = imgSize[0]+(8-(imgSize[0]%8))
    width = imgSize[1]+(8-(imgSize[1]%8))
    
    #outplace matrix to adjust the boundary cases
    dctOutput = numpy.zeros([height,width],float)
    for i in range(0,imgSize[0]):
        for j in range(0,imgSize[1]):
            dctOutput[i][j]=imgArray[i][j]
    qt=quantisation("Q50")
    
    #Iterate on 8x8 pixel group
    for i in range(0,height,8):
        for j in range(0,width,8):
            #performing out-place, for more clearity 
            temp = dctOutput[i:i+8,j:j+8]
            
            #Apply dct on 8x8 matrix
            temp = dct(dct(temp,axis=0,norm='ortho'),axis=1,norm='ortho')
            #Quantize the DCT output
            for k in range(0,8):
                for m in range(0,8):
                    temp[k][m]=numpy.round(temp[k][m]/qt[k][m])
            
            dctOutput[i:i+8,j:j+8] = idct(idct(temp,axis=0,norm='ortho'),axis=1,norm='ortho')

    dctOutput = dctOutput+128
    outputImage = Image.fromarray(dctOutput).convert("RGB")
    outputImage.save('groutput.jpg')


#Downsample the colour components by a factor of 2 in both direction
#Cb=Cb[0::2,0::2]
#Cr=Cr[0::2,0::2]