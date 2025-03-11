from models.user import dummy_db


def register_user_repository(user_id, user_data):
    dummy_db["users"].update({user_id: user_data})
