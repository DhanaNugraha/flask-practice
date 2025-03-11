from flask import Flask, render_template, jsonify, request
from router.user import user_router
from router.auth import auth_router
import uuid
from auth.login import claim_user, login_required

app = Flask(__name__)
# to inject path from router
app.register_blueprint(user_router)
app.register_blueprint(auth_router)

@app.before_request
def before_request():
    print("Before request")
    token = request.headers.get("Authorization")
    print("token", token)
    if token:
        request.user = claim_user(token)
        


@app.after_request
def after_request(response):
    request_id = str(uuid.uuid4())
    print("request id is", request_id)
    response.headers["X-Request-ID"] = request_id
    return response

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.route("/account", methods=["GET"])
@login_required
def account():
    print("Route /account")
    return jsonify(
        {"data": {"message": {"you" : request.user} }, "success": True}
    ), 200


@app.route("/")
def index():
    return render_template("index.html")


# good routing practice = CRUD create, read, update, delete. this means that one function of path should alraedy comprise of all the operations


# case "put":

# case "delete":


# @app.route('/send-message', methods=['GET'])
# def home():
#     return jsonify({"message": "Hello World!"}), 200

# @app.route('/create-letter', methods=['POST'])
# def create_letter():
#     data = request.json
#     print(data)
#     return jsonify({"message": "Letter created successfully!"}), 201

# if __name__ == '__main__':
#     app.run(debug=True)
