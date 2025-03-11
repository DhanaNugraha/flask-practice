from flask import Flask, render_template

from router.user import user_router

app = Flask(__name__)
# to inject path from router
app.register_blueprint(user_router)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

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
