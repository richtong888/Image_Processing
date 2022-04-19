from traceback import print_tb
import cv2 as cv
import numpy as np

class ShapeAnalysis:
    def __init__(self):
        self.shapes = {'triangle': 0, 'rectangle': 0, 'polygons': 0, 'circles': 0}

    def analysis(self, frame):
        h, w, ch = frame.shape
        result = np.zeros((h, w, ch), dtype=np.uint8)
        # 二值化圖像
        print("start to detect lines...\n")
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        ret, binary = cv.threshold(gray, 10, 255, cv.THRESH_BINARY_INV) # if threshould number too high, all pass except white
    
        cv.imshow("input image", frame)
        cv.imshow("binary image", binary)

        contours , hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        for cnt in range(len(contours)):
            # 提取與繪制輪廓
            cv.drawContours(result, contours, cnt, (0, 255, 0), 2)

            # 輪廓逼近
            epsilon = 0.01 * cv.arcLength(contours[cnt], True)

            approx = cv.approxPolyDP(contours[cnt], epsilon, True)

            # 分析幾何形狀
            corners = len(approx)
            shape_type = ""
            if corners == 3:
                count = self.shapes['triangle']
                count = count+1
                self.shapes['triangle'] = count
                shape_type = "三角形"
            if corners == 4:
                count = self.shapes['rectangle']
                count = count + 1
                self.shapes['rectangle'] = count
                shape_type = "矩形"
            if corners >= 10:
                count = self.shapes['circles']
                count = count + 1
                self.shapes['circles'] = count
                shape_type = "圓形"
            if 4 < corners < 10:
                count = self.shapes['polygons']
                count = count + 1
                self.shapes['polygons'] = count
                shape_type = "多邊形"

            # 求解中心位置
            mm = cv.moments(contours[cnt])
            cx = int(mm['m10'] / mm['m00'])
            cy = int(mm['m01'] / mm['m00'])
            cv.circle(result, (cx, cy), 3, (0, 0, 255), -1)

            # 顏色分析
            color = frame[cy][cx]
            color_str = "(" + str(color[0]) + ", " + str(color[1]) + ", " + str(color[2]) + ")"

            # 計算面積與周長
            p = cv.arcLength(contours[cnt], True)
            area = cv.contourArea(contours[cnt])
            print("周長: %.3f, 面積: %.3f 顏色: %s 形狀: %s "% (p, area, color_str, shape_type))

        cv.imshow("Analysis Result", self.draw_text_info(result))
        cv.imwrite("D:/test-result.png", self.draw_text_info(result))
        print("周長: %.3f, 面積: %.3f 顏色: %s 形狀: %s "% (p, area, color_str, shape_type))

        cv.imshow("Only Result", result)

        return self.shapes

    def draw_text_info(self, image):
        c1 = self.shapes['triangle']
        c2 = self.shapes['rectangle']
        c3 = self.shapes['polygons']
        c4 = self.shapes['circles']
        cv.putText(image, "triangle: "+str(c1), (10, 20), cv.FONT_HERSHEY_PLAIN, 1.2, (255, 0, 0), 1)
        cv.putText(image, "rectangle: " + str(c2), (10, 40), cv.FONT_HERSHEY_PLAIN, 1.2, (255, 0, 0), 1)
        cv.putText(image, "polygons: " + str(c3), (10, 60), cv.FONT_HERSHEY_PLAIN, 1.2, (255, 0, 0), 1)
        cv.putText(image, "circles: " + str(c4), (10, 80), cv.FONT_HERSHEY_PLAIN, 1.2, (255, 0, 0), 1)
        return image

def find_nose(img):
    
    # data cropping
    x = 260
    y = 400

    w = 100
    h = 50
  
    crop_img = img[y:y+h, x:x+w]


    gray2 = cv.cvtColor(img ,cv.COLOR_BGR2GRAY)
    ret2,binary2 = cv.threshold(gray2 , 50 ,255 ,cv.THRESH_BINARY_INV)  
    gray = cv.cvtColor(crop_img ,cv.COLOR_BGR2GRAY) 
    ret,binary = cv.threshold(gray , 50 ,255 ,cv.THRESH_BINARY_INV)
    contour , hierarcy = cv.findContours(binary, cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE)
    cx = { }
    cy = { }
    for i in range(len(contour)):
        cnt = contour[i]
        m = cv.moments(cnt)
        cv.drawContours(crop_img , contour , -1 , (0,0,200),5)

        cx[i] = int(m['m10'] / m['m00'])
        cy[i] = int(m['m01'] / m['m00'])

        cv.circle(crop_img, (cx[i], cy[i]), 3, (0, 255, 0), -1)

    cv.imshow("img" , img)
    cv.imshow("binary" , binary)
    cv.imshow("crop img" , crop_img) 
    cv.imshow('gray2',binary2)  
    print(len(contour))
    print(m)
    print(len(cx))
    print('Center of two nostrils are(', cx[0]+x, ' , ', cy[0]+y,'),(' , cx[1]+x, ' , ' , cy[1]+y, ')')
    cv.waitKey(0)





def find_portrait(img):
    # data cropping
    # x = 260
    # y = 400

    # w = 100
    # h = 50
  
    # crop_img = img[y:y+h, x:x+w]


    # gray2 = cv.cvtColor(img ,cv.COLOR_BGR2GRAY)
    # ret2,binary2 = cv.threshold(gray2 , 50 ,255 ,cv.THRESH_BINARY_INV) 
    img = cv.resize(img, (640,480), interpolation=cv.INTER_AREA)

    gray = cv.cvtColor(img ,cv.COLOR_BGR2GRAY) 
    ret,binary = cv.threshold(gray , 130 ,255 ,cv.THRESH_BINARY_INV)
    contour , hierarcy = cv.findContours(binary, cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE)
    cx = { }
    cy = { }
    # for i in range(len(contour)):
    #     cnt = contour[i]
    #     m = cv.moments(cnt)
    #     cv.drawContours(img , contour , -1 , (0,0,200),5)

    #     cx[i] = int(m['m10'] / m['m00'])
    #     cy[i] = int(m['m01'] / m['m00'])

    #     cv.circle(img, (cx[i], cy[i]), 3, (0, 255, 0), -1)

    cv.imshow("img" , img)
    cv.imshow("binary" , binary)
    print(len(contour))
    # print(m)
    # print(len(cx))
    # print('Center of two nostrils are(', cx[0]+x, ' , ', cy[0]+y,'),(' , cx[1]+x, ' , ' , cy[1]+y, ')')
    cv.waitKey(0)


def draw_line(img):   
     
    img = cv.resize(img, (640,480), interpolation=cv.INTER_AREA)
    cv.line(img, (200, 220), (370, 220), (0, 0, 255), 5)
    cv.imshow('lineimg',img)
    cv.waitKey(0)

if __name__ == "__main__":
    # img = cv.imread("geo.jpg")
    # img = cv.imread("img1.jpg")
    img = cv.imread("por2.jpg")    
    # find_portrait(img)
    draw_line(img)
    # ld = ShapeAnalysis()
    # ld.analysis(img)
    key = cv.waitKey(0) & 0xFF
    if key == ord('q'):
        cv.destroyAllWindows()