from flask import jsonify
from repo.user import register_user_repository
from repo.universal import all_users_repository

def serialize_user(user_data):
    return {
        "email": user_data["email"],
        "full_name": user_data["full_name"],
    }

def get_users(user_email=False):
    users = all_users_repository()
    filtered_db = []

    # for specific user
    if user_email:
        for id, user_data in users.items():
            if user_data["email"] == user_email:
                filtered_db.append(serialize_user(user_data))

        # when user not found
        if filtered_db == []:
            return jsonify(
                {
                    "message": "This user does not exist",
                    "success": False,
                }
            ), 400

    # for all user
    else:
        for id, user_data in users.items():
            filtered_db.append(serialize_user(user_data))

    return jsonify({"data": filtered_db, "success": True}), 200


def register_user(user_data):
    # important to get so we can check data exist
    first_name = user_data.get("first_name")
    last_name = user_data.get("last_name")
    email = user_data.get("email")
    password = user_data.get("password")

    # data checker
    if not first_name or not last_name or not email or not password:
        return jsonify(
            {
                "message": {
                    "first_name": "first name is required"
                    if not first_name
                    else "filled",
                    "last_name": "last name is required" if not last_name else "filled",
                    "email": "email is required" if not email else "filled",
                    "password": "password is required" if not password else "filled",
                },
                "success": False,
            }
        ), 400

    # full name maker and updater
    full_name = f"{first_name} {last_name}"

    # check for duplicate in db
    # dont loop db directly, create a copy
    users = all_users_repository()
    for id, registered_user in users.items():
        if registered_user["full_name"] == full_name or registered_user["email"] == email :
            return jsonify(
                {
                    "message": "This user already exists",
                    "success": False,
                }
            ), 400

    # put in full name in user_data
    user_data.update({"full_name": full_name})

    # create user id
    user_id = max(users.keys()) + 1

    # register user
    register_user_repository(user_id, user_data)

    # print(all_users_repository())
    return jsonify(
        {"data": {"message": f"{full_name} registered successfully!"}, "success": True}
    ), 201
