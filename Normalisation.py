from skimage import io
from skimage import transform
from math import ceil
import numpy as np

def Resize(filename,x_length,y_length):
    image = io.imread(filename)
    return (transform.resize(image,(y_length,x_length))*255).astype(np.uint8)

def CropFromMiddle(filename,x_length,y_length):
    image = io.imread(filename)
    image_width = image.shape[1]
    image_height = image.shape[0]
    x1 = ceil((image_width - x_length)/2)
    x2 = x1 + x_length

    y1 = ceil((image_height - y_length)/2)
    y2 = y1 + y_length
    
    cropped = image[y1:y2,x1:x2]
    return cropped


def Normalize(image):
    
    return (image.astype(np.float64)/255)