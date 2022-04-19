import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
from IPython.display import clear_output
from pip import main

def show_img(img, bigger=False):
    if bigger:
        plt.figure(figsize=(15,15))
    image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.show()

def mouse_handler(event, x, y, flags, data):
    if event == cv2.EVENT_LBUTTONDOWN:
        # 標記點位置
        cv2.circle(data['img'], (x,y), 3, (0,0,255), 5, 16) 

        # 改變顯示 window 的內容
        cv2.imshow("Image", data['img'])
        
        # 顯示 (x,y) 並儲存到 list中
        print("get points: (x, y) = ({}, {})".format(x, y))
        data['points'].append((x,y))

def get_points(im):
    # 建立 data dict, img:存放圖片, points:存放點
    data = {}
    data['img'] = im.copy()
    data['points'] = []
    
    # 建立一個 window
    cv2.namedWindow("Image", 0)
    
    # 改變 window 成為適當圖片大小
    h, w, dim = im.shape
    print("Img height, width: ({}, {})".format(h, w))
    cv2.resizeWindow("Image", w, h)
        
    # 顯示圖片在 window 中
    cv2.imshow('Image',im)
    
    # 利用滑鼠回傳值，資料皆保存於 data dict中
    cv2.setMouseCallback("Image", mouse_handler, data)
    
    # 等待按下任意鍵，藉由 OpenCV 內建函數釋放資源
    cv2.waitKey()
    cv2.destroyAllWindows()
    
    # 回傳點 list
    return data['points']

if __name__ == "__main__":

#Read the destination image
    img_dst = cv2.imread("./geo.jpg")

    print("Click on the screen and press any key for end process")
    points  = get_points(img_dst)

    print("\npoints list:")
    print(points)