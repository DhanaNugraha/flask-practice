import copy
from models.user import dummy_db

def all_users_repository():
    return copy.deepcopy(dummy_db["users"])


def get_user_by_email(email):
    all_users = all_users_repository()

    for _id, user_data in all_users.items():
        if user_data["email"] == email:
            user_data.update({"id": _id})
            return user_data
        
    return None
