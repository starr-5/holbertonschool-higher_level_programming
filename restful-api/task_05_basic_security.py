from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)

app = Flask(__name__)

# Secret key for JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Users database (in memory)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# -------------------------
# BASIC AUTH
# -------------------------

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# -------------------------
# JWT AUTH
# -------------------------

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create token with username
    access_token = create_access_token(identity=username)

    return jsonify({"access_token": access_token})


# JWT Protected route
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# Admin-only route
@app.route("/admin-only")
@jwt_required()
def admin_only():
    username = get_jwt_identity()
    user = users.get(username)

    if user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# -------------------------
# JWT ERROR HANDLERS (IMPORTANT)
# -------------------------

@jwt.unauthorized_loader
def missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


if __name__ == "__main__":
    app.run()