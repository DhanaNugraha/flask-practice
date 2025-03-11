from flask import Blueprint, request, jsonify
from views.auth import user_login


auth_router = Blueprint("auth_router", __name__, url_prefix="/login")

@auth_router.route("", methods=["POST"])
def login():
    try:
        response = user_login(request.json)

    except Exception as e:
        return jsonify({"message": str(e), "success": False}), 401
    
    return response