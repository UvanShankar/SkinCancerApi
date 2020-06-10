import cv2
import numpy as np
import os

def skin(filename):
    app_root = os.path.dirname(os.path.abspath(__file__))
    app_root=os.path.join(app_root,'Skincancermodel')
    img=cv2.imread(os.path.join(app_root,filename))
    #converting from gbr to hsv color space
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #skin color range for hsv color space 
    HSV_mask = cv2.inRange(img_HSV, (0, 15, 0), (17,170,255)) 
    HSV_mask = cv2.morphologyEx(HSV_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))

    #converting from gbr to YCbCr color space
    img_YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    #skin color range for hsv color space 
    YCrCb_mask = cv2.inRange(img_YCrCb, (0, 135, 85), (255,180,135)) 
    YCrCb_mask = cv2.morphologyEx(YCrCb_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))

    #merge skin detection (YCbCr and hsv)
    global_mask=cv2.bitwise_and(YCrCb_mask,HSV_mask)
    global_mask=cv2.medianBlur(global_mask,3)
    global_mask = cv2.morphologyEx(global_mask, cv2.MORPH_OPEN, np.ones((4,4), np.uint8))


    HSV_result = cv2.bitwise_not(HSV_mask)
    YCrCb_result = cv2.bitwise_not(YCrCb_mask)
    global_result=cv2.bitwise_not(global_mask)

    #print(global_result.size)
    #show results
    # cv2.imshow("1_HSV.jpg",HSV_result)
    # cv2.imshow("2_YCbCr.jpg",YCrCb_result)
    # cv2.imshow("3_global_result.jpg",global_result)
    # cv2.imshow("Image.jpg",img)
    #cv2.imwrite("1_HSV.jpg",HSV_result)
    #cv2.imwrite("2_YCbCr.jpg",YCrCb_result)
    #cv2.imwrite("3_global_result.jpg",global_result)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()  
    ii=0
    jj=0
    for i in range(0,global_result.shape[0]):
      for j in range(0,global_result.shape[1]):
        ii+=global_result[i][j]
        jj+=255
    print(ii)
    print(jj)
    print(ii/jj)
    return ii/jj
    
