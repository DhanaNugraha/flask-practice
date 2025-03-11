from flask import jsonify
from repo.universal import all_users_repository, get_user_by_email
from auth.login import get_token


def user_login(login_request):
    email = login_request.get("email")
    password = login_request.get("password")
    user_data = get_user_by_email(email)
    
    assert user_data["password"] == password, "Incorrect password"

    token = get_token(email, user_data["id"])

    return jsonify({"data": {"token": token}, "success": True}), 200

