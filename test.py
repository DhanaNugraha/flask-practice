dummy_db = {
    "users": {
        "email@gmail.com": {
            "full_name": "Hello world",
            "first_name": "Hello",
            "last_name": "world",
            "password": "pass231",
            "email": "email@gmail.com",
        },
        "ail@gmail.com": {
            "full_name": "llo rld",
            "first_name": "llo",
            "last_name": "rld",
            "password": "ss231",
            "email": "ail@gmail.com",
        },
        "mail@gmail.com": {
            "full_name": "llo rld",
            "first_name": "llo",
            "last_name": "rld",
            "password": "ss231",
            "email": "mail@gmail.com",
        },
    }
}

full_name = "llo rld"
email = "ail@gmail.com"

for id, registered_user in dummy_db["users"].items():
    if registered_user["full_name"] == full_name or registered_user["email"] == email:
        print("duplicate")
        break

# print(full_name in dummy_db["users"].values().get("full_name"))