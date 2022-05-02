from operator import truediv
from PIL import Image
from cv2 import imshow
import numpy as np
import cv2 as cv

def image_fusion(img1,img2):

    im1 = Image.open(img1)
    im2 = Image.open(img2)

    # 重新設定im2的大小
    im1 = im1.resize((640,480))
    im1 = im1.rotate(-90,expand = True)
    im2 = im2.resize((640,480))
    im2 = im2.rotate(-90,expand = True)    
    # im1.show()
    print(im1.size)

    # # 將影像2的三個色道分離，其中r、g、b都為Image物件
    r, g, b = im2.split()
    mask = Image.new("L", im1.size, 50)
    # # 遮罩混合
    img = Image.composite(im1, im2, mask)
    img.show()

    return img



if __name__ == "__main__":
    for i in range(1,13):
        img1 = './Face_Portrait/face_side_'+ str(2*i-1) + '.jpg'
        img2 = './Face_Portrait/face_side_'+ str(2*i) + '.jpg'   
        img = image_fusion(img1,img2)
        save_path = './Face_Portrait/out/fusion_' + str(i) + '.jpg'
        img.save(save_path)


