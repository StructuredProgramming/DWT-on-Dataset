from PIL import Image
import os
import numpy as np
import pywt
import matplotlib.pyplot as plt



from PIL import Image as PImage

def loadImages(path):
    counter=1

    dirpath = os.listdir(path)
    
    loadedImages = []
    for subdir in dirpath:
        full_subdir= path + subdir + '/'
        imageList = os.listdir(full_subdir)
        for image in imageList:
            fullpath = full_subdir + image
            img = PImage.open(fullpath)
            loadedImages.append(img)
            titles = ['Approximation', ' Horizontal detail',
          'Vertical detail', 'Diagonal detail']
            coefficients = pywt.dwt2(img, 'bior1.3')
            LL, (LH, HL, HH) = coefficients
            fig = plt.figure(figsize=(12, 3))
            for i, a in enumerate([LL, LH, HL, HH]):
                ax = fig.add_subplot(1, 4, i + 1)
                ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
                ax.set_title(titles[i], fontsize=10)
                ax.set_xticks([])
                ax.set_yticks([])

            fig.tight_layout()
            plt.show()
            fig.savefig(str(counter)+".png")
            print(counter)
            counter=counter+1
    

    return loadedImages

#Edit to path on your computer to the images
path = "D:/abhay/wavelets/dataset/"

imgs = loadImages(path)

for img in imgs:
    img.show()
