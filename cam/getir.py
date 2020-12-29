import time
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#import cv2

def contrast_stretch(im):
    """
    Performs a simple contrast stretch of the given image, from 5-95%.
    """
    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 95)

    out_min = 0.0
    out_max = 255.0

    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min

    return out


imdia = np.array(Image.open("ims/imgDIA.jpg"))
imIR = np.array(Image.open("ims/imgIR.jpg"))

IR=imIR-imdia

red=imdia[:,:,0].astype(float)
nir=IR[...,2].astype(float)

den=red+nir
den[den==0]=0.01
ndvi=(nir-red)/den
ndvi=contrast_stretch(ndvi)
ndvi=ndvi.astype(np.uint8)

plt.imshow(ndvi, cmap='jet')
plt.savefig('ims/NDVI.png')
plt.show()


Image.fromarray(IR).save('ims/IR.jpg')
#im=Image.fromarray(ndvi)
#im.show()
