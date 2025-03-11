from flask import Blueprint, request
from views.user import get_users, register_user


user_router = Blueprint("user_router", __name__, url_prefix="/api/v1/users")

# path from url prefix
@user_router.route("", methods=["GET", "POST"])
def user_api():
    match request.method.lower():
        case "get":
            return get_users()

        case "post":
            return register_user(request.json)
        
@user_router.route("/email/<user_email>", methods=["GET"])
def get_user_by_email(user_email):
    return get_users(user_email)

# @user_router.route("/id/<user_id>", methods=["GET"])
# def get_user_by_id(user_id):
#     print("herewwadwd")
#     print(user_id)
#     print(type(user_id))
#     return get_users(user_id)