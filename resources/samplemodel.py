from flask_restful import Resource, reqparse,request
import os
from resources.Model_Predict import predict
from models.user import UserModel

class SampleModel(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This username cannot be blank."
                        )

    def post(self):
        print("fdshgf")
        print('Headers: %s', request.headers)
        data = SampleModel.parser.parse_args()
        user= UserModel.find_by_username(data['username'])
        print(user)
        if(user==None):
            return "invalid username"
        row=user
        print ("Name: ",row.username, "Request:",row.requests)
        if row.requests>50:
            return {"msg":"max limit reached convert to premium"}
        UserModel.update_requests(data['username'])
        
        #user.save_to_db()
        #print('Body: %s', request.get_data())
        #print('Body: %s', request.files())
        app_root = os.path.dirname(os.path.abspath(__file__))
        #data = SampleModel.parser.parse_args()
        target = os.path.join(app_root, 'Skincancermodel')
        # target = os.path.join(APP_ROOT, 'static/')
        print("tar"+target)
        #return {"message": "image received","apicode":"100"}, 201
        
        for upload in request.files.getlist("image"):
            print("{} is the file name".format(upload.filename))
            filename = upload.filename
            destination =  "/".join([target, filename])
            print ("Accept incoming file:", filename)
            print ("Save it to:", destination)
            upload.save(destination)
        print("predict calling")
        ans=predict(filename)
        print("predict called")
        print(ans)

        return {"message": ans}, 201
    
    
    def get(self):
        return {"UserModel.find_all()":"hfv"}
