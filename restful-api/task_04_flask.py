from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage
users = {}


# Root endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# Return list of usernames
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))


# Status endpoint
@app.route("/status")
def status():
    return "OK"


# Get user by username (dynamic route)
@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


# Add new user (POST)
@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        data = request.get_json()
    except:
        return jsonify({"error": "Invalid JSON"}), 400

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Store user
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
