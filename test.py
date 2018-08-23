'''test stacky'''
import numpy as np
import tifffile
from skimage.data import astronaut
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

I = rgb2gray(astronaut())
print(I.shape)

s = np.zeros((3, I.shape[0]-50, I.shape[1]-50))

s[0, :, :] = I[25:-25, 25:-25]
s[1, :, :] = I[:-50, :-50]
s[2, :, :] = I[40:-10, 40:-10]
print(s.shape)

fig, ax = plt.subplots(1,3,figsize=(15,5))
for i in range(s.shape[0]):
    ax[i].imshow(s[i,:,:], cmap='gray')
plt.show()

from stack_registration import stack_registration

stack_registration(s, align_to_this_slice=0)

fig, ax = plt.subplots(1,3,figsize=(15,5))
for i in range(s.shape[0]):
    ax[i].imshow(s[i,:,:], cmap='gray')
plt.show()
