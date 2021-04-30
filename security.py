from werkzeug.security import safe_str_cmp
from models.user import UserModel 


def authenticate(username, password):
    """
    function that gets called when a user call the /auth endpoint
    with their username and password.
    :param username: User's username in string format
    :param password:  User's un-encrypted password in string format.
    :return: A user if authentication was successful, none otherwise.
    """
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user 


def identity(payload):
    """
    function that gets called when user has already authenticated, and Flask-JWT
    verified their authorization header is correct.
    :param payload: A dictionary with 'identity' key, which is the user id.
    :return: A UserModel
    """
    user_id = payload('identity')
    return UserModel.find_by_id(user_id)
    


