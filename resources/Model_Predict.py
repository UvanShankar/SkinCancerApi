from fastai.vision import load_learner
from fastai.vision.image import open_image
import os
#import cv2
import numpy as np
from resources.isskin import skin




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
    #abc=skin(filename)
    #if abc>0.5:
    #    return {
    #        "answer":"no skin"
    #    }
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
    abc=skin(filename)
    if abc>0.5:
        return {
            "answer":"no skin"
        }
    return predict_names
  
    
#predict('file.jpg','ootypicsmodel.sav')
