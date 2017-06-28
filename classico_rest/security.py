from werkzeug.security import safe_str_cmp
from models.user import UserModel
from flask_bcrypt import Bcrypt

# security
bcrypt = Bcrypt()


def authenticate(nickname, password):
    user = UserModel.find_by_nickname(nickname)
    # if user and safe_str_cmp(user.password, password):
    if user and bcrypt.check_password_hash(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    print(user_id)
    user = UserModel.find_by_nickname(user_id)
    return user
