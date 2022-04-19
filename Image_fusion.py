from PIL import Image
import numpy as np
import cv2 as cv

if __name__ = "__main__":
    # 開啟影像1
    im1 = Image.open('/content/drive/MyDrive/Colab_Notebooks/swim/img1.jpg')
    # 開啟影像2
    im2 = Image.open('/content/drive/MyDrive/Colab_Notebooks/swim/img2.jpg')
    # 重新設定im2的大小
    im2.resize(im1.size)
    # 將影像2的三個色道分離，其中r、g、b都為Image物件
    r, g, b = im2.split()
    # 遮罩混合
    img = Image.composite(im1, im2, b)