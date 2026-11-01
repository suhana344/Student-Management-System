
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to SQLite database
def get_db():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    return conn


# Create students table
def create_table():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# GET: Retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    conn = get_db()

    students = conn.execute(
        "SELECT * FROM students"
    ).fetchall()

    conn.close()

    return jsonify([dict(s) for s in students])


# GET: Retrieve a specific student
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    conn = get_db()

    student = conn.execute(
        "SELECT * FROM students WHERE id = ?", (id,)
    ).fetchone()

    conn.close()

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(dict(student))


# POST: Add a new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json(silent=True) or {}

    if not all(data.get(field) for field in
               ['name', 'department', 'email']):
        return jsonify({"error": "All fields are required"}), 400

    conn = get_db()

    cursor = conn.execute(
        """INSERT INTO students (name, department, email)
           VALUES (?, ?, ?)""",
        (data['name'], data['department'], data['email'])
    )

    conn.commit()
    student_id = cursor.lastrowid
    conn.close()

    return jsonify({
        "message": "Student added successfully",
        "id": student_id
    }), 201


# PUT: Update student information
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json(silent=True) or {}

    if not all(data.get(field) for field in
               ['name', 'department', 'email']):
        return jsonify({"error": "All fields are required"}), 400

    conn = get_db()

    student = conn.execute(
        "SELECT * FROM students WHERE id = ?", (id,)
    ).fetchone()

    if student is None:
        conn.close()
        return jsonify({"error": "Student not found"}), 404

    conn.execute(
        """UPDATE students
           SET name = ?, department = ?, email = ?
           WHERE id = ?""",
        (data['name'], data['department'], data['email'], id)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Student updated successfully"})


# DELETE: Delete a student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    conn = get_db()

    cursor = conn.execute(
        "DELETE FROM students WHERE id = ?", (id,)
    )

    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({"message": "Student deleted successfully"})


# Run Flask application
if __name__ == '__main__':
    create_table()
    app.run(debug=True)
