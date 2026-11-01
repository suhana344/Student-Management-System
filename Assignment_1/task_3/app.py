
from flask import Flask, request, jsonify
from functools import wraps
import secrets

app = Flask(__name__)

# Demo users
users = {
    "employee": {
        "password": "emp123",
        "role": "employee"
    },
    "admin": {
        "password": "admin123",
        "role": "admin"
    }
}

# Store login tokens
tokens = {}

# Sample employee records
employees = [
    {"id": 1, "name": "Ali", "department": "IT"},
    {"id": 2, "name": "Sara", "department": "HR"}
]


# Login API
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}

    username = data.get("username")
    password = data.get("password")

    if username not in users or users[username]["password"] != password:
        return jsonify({"error": "Invalid username or password"}), 401

    token = secrets.token_hex(16)
    tokens[token] = username

    return jsonify({
        "message": "Login successful",
        "token": token,
        "role": users[username]["role"]
    })


# Authentication decorator
def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token or not token.startswith("Bearer "):
            return jsonify({"error": "Token is missing"}), 401

        token = token.split(" ", 1)[1]

        if token not in tokens:
            return jsonify({"error": "Invalid token"}), 401

        request.current_user = tokens[token]
        return func(*args, **kwargs)

    return wrapper


# Admin authorization decorator
def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = getattr(request, "current_user", None)

        if not username:
            return jsonify({"error": "Authentication required"}), 401

        if users[username]["role"] != "admin":
            return jsonify({"error": "Admin access required"}), 403

        return func(*args, **kwargs)

    return wrapper


# View employees (Employee and Admin)
@app.route("/employees", methods=["GET"])
@token_required
def get_employees():
    return jsonify(employees)


# Add employee (Admin only)
@app.route("/employees", methods=["POST"])
@token_required
@admin_required
def add_employee():
    data = request.get_json(silent=True) or {}

    if not isinstance(data.get("name"), str) or not data["name"].strip():
        return jsonify({"error": "Employee name is required"}), 400

    if not isinstance(data.get("department"), str) or not data["department"].strip():
        return jsonify({"error": "Department is required"}), 400

    new_employee = {
        "id": max([e["id"] for e in employees], default=0) + 1,
        "name": data["name"].strip(),
        "department": data["department"].strip()
    }

    employees.append(new_employee)

    return jsonify({
        "message": "Employee added successfully",
        "employee": new_employee
    }), 201


# Delete employee (Admin only)
@app.route("/employees/<int:employee_id>", methods=["DELETE"])
@token_required
@admin_required
def delete_employee(employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            employees.remove(employee)
            return jsonify({"message": "Employee deleted successfully"})

    return jsonify({"error": "Employee not found"}), 404


if __name__ == "__main__":
    app.run(port=5002, debug=True)
