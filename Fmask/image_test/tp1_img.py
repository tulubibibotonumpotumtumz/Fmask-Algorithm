#importations
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
#ex1 - exemples
L = 15
C = 15

im = np.zeros((L,C), dtype=np.uint8)

im[5, 2] = 10

im[0:4, 5:10] = 25

"""plt.imshow(im, cmap='gray')
plt.axis('off')
plt.show()"""

#ex1
"""taille = 5
debutL = int(L/2)
debutC = int(C/4)
im1 = np.zeros((L, C), dtype=np.uint8)
im1[debutL:debutL+taille, debutC:debutC+taille] = 25

plt.imshow(im1, cmap='gray')
plt.axis('off')
plt.show()"""

#ex2
im2 = io.imread('peppers.tiff')
#im2[125, 55] = [134  35  30]
#print(im2[125, 55])
def bin_red(image, composante=0):
    n = len(image)
    m = len(image[0])
    res = np.zeros((n,m),dtype=np.uint8)
    for i in range(n):
        for j in range(m):
            
            if image[i, j, composante] > image[i, j, 1] or image[i, j, composante] > image[i, j, 2]:
                res[i, j, composante] = 1
    return res


#io.imsave('red_peppers.tiff', bin_red(im2))
im_gray = [[for j in range()] for i in range(len(im)]
im_gray = np.array(im_gray, dtype=np.uint8)





























