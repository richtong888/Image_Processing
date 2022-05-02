import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from pip import main

if __name__ == "__main__":
    name = 'trainABP.txt'
    path = './'
    f = open(path+name, 'r')

    text = f.read()
    # print(text)
    f.close()

    newtext = text.split(",")
    print(newtext)
