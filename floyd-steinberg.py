import numpy as np
from PIL import Image

def dither(image):
    img = Image.open(image).convert('L')
    imgArray = np.array(img)
    threshold = 128
    rows, cols = imgArray.shape

    for y in range(rows):
        for x in range(cols):
            oldPixel = imgArray[y, x]
            newPixel = 255 if oldPixel > threshold else 0
            imgArray[y, x] = newPixel

            error = oldPixel - newPixel  #hata değerini hesapla

            #hatayı komşu pixellere dağıt
            if x + 1 < cols:
                imgArray[y, x + 1] += error * 7 / 16
            if x - 1 >= 0 and y + 1 < rows:
                imgArray[y + 1, x - 1] += error * 3 / 16    
            if y + 1 < rows:
                imgArray[y + 1, x] += error * 5 / 16
            if x + 1 < cols and y + 1 < rows:
                imgArray[y + 1, x + 1] += error * 1 / 16

    imgArray = np.clip(imgArray, 0, 255)  #hata eklenince 0-255 aralığından çıkmamak için

    binaryImg = Image.fromarray(imgArray).convert('1') 
    binaryImg.save("output-floyd-steinberg.png")
    return binaryImg

binaryImg = dither("input.png")
binaryImg.show()
