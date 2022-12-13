#needed packages 
import numpy as np 
import pandas as pd
import scipy as sp
import itertools as it
import matplotlib.pyplot as plt
from scipy import signal 
from matplotlib.animation import FuncAnimation

#import your image 
#pathname to your image 
image = "/Users/alauth/Documents/AQL.JPG"

#need to read an image into an array 
im_image = plt.imread(image)
# print(im_image)
# print(im_image.shape)
# print(im_image.size)

#this gives me pixes with numberical values [0 - 255] max number that can represent with an 8-bit binary number
#shape 3024 x 3024, 3 = each pixel has three values associated with it. RBG
#size or the total number of pixels. 

#I want to rescale my pixles from 0-255 (0: no color; 255: saturated) to 0-1
#think of it as a percentage all over 255. 
image_final = plt.imread(image).astype(float)/255
#now we have decminal values that are relative to 255(max binary value)
print(image_final)