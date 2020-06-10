from fastai.vision import load_learner
from fastai.vision.image import open_image
import os
import cv2
import numpy as np




def predict(filename):    
    app_root = os.path.dirname(os.path.abspath(__file__))
    app_root=os.path.join(app_root,'Skincancermodel')
    p=['Actinic keratoses',
    'Basal cell carcinoma',
    'Benign keratosis ',
    'Dermatofibroma',
    'Melanocytic nevi',
    'Melanoma',
    'Vascular lesions']
    img = open_image(os.path.join(app_root,filename))
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
    if ii/jj>0.5:
        return {
            "answer":"no skin"
        }
    #os.remove(os.path.join(app_root,filename))
    learn  = load_learner(os.path.join( os.path.dirname(os.path.abspath(__file__)),'Skincancermodel'),"export.pkl")
    aa=p[learn.predict(img)[1]]
    bb=learn.predict(img)
    predict_names={
        "answer":aa,
        "v1":str(bb[0]),
        "v2":str(bb[1]),
        "v3":str(bb[2])
    }
    print("predict______predict")
    print(predict_names)
    return predict_names
  
    
#predict('file.jpg','ootypicsmodel.sav')
