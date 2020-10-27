from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

basic_auth_users = {
    "john": generate_password_hash("mrdoe"),
    "jane": generate_password_hash("mrsdoe")
}

@auth.verify_password
def verify_password(username, password):
    if username in basic_auth_users and \
            check_password_hash(basic_auth_users.get(username), password):
        return username

    return None

@app.route("/basic_auth")
@auth.login_required
def basic_auth():
    return "Hello, {}!".format(auth.current_user())



@app.route("/get_token", methods=["POST"])
def get_token():
    print(jsonify(request.json))
    print(request.get_json())
    # u = request.json.username
    # p = request.json.password
    # username = verify_password(u, p)
    # if username:
    #     return username, 200
    return "", 400

@app.route("/token_secured")
def token_secured():
    return "", 200
