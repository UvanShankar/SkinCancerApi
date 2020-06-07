from flask_restful import Resource, reqparse,request
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('emailId',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('premium',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('requests',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        print("fdshgf")
        print('Headers: %s', request.headers)
        print('Body: %s', request.get_data())
        
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message":{"answer" :"A user with that username already exists","apicode":"111"}}, 201
        if UserModel.find_by_emailId(data['emailId']):
            return {"message": {"answer":"A user with that emailId already exists","apicode":"121"}}, 201
        print(data['username'], data['password'], data['emailId'])
        user = UserModel(data['username'], data['password'], data['emailId'],data['premium'],0)
        user.save_to_db()

        return {"message":{"answer" :"User created successfully.","apicode":"100"}}, 201
