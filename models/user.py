from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    emailId = db.Column(db.String(80))
    premium = db.Column(db.String(80))
    requests = db.Column(db.Numeric)

    def __init__(self, username,password, emailId,premium,requests):
        self.username = username
        self.password = password
        self.emailId = emailId
        self.premium =premium
        self.requests =requests

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    
    @classmethod
    def find_by_emailId(cls, emailId):
        return cls.query.filter_by(emailId=emailId).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def update_requests(cls, username):
        user=cls.query.filter_by(username=username).first()
        user.requests=user.requests+1
        
        db.session.commit()
        return user.requests

