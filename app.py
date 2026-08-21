# app.py
# This is the main Flask application file.
# It contains all the routes (URLs) and the logic that connects
# our frontend (HTML pages) to our backend (Python) and database (SQLite).

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# Create the Flask application object.
# __name__ tells Flask where to look for templates/static files.
app = Flask(__name__)

# Name of our SQLite database file.
DATABASE = "database.db"


def get_db_connection():
    """
    Creates and returns a connection to the SQLite database.
    We use this function everywhere we need to talk to the database,
    so we don't repeat the same connection code again and again.
    """
    conn = sqlite3.connect(DATABASE)
    # This makes rows behave like dictionaries (access columns by name).
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Creates the 'students' table if it does not already exist.
    This runs automatically every time the app starts, so you
    never have to manually create the database.
    """
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            course TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()


# --------------------------------------------------------------------
# ROUTE: Home Page
# --------------------------------------------------------------------
@app.route("/")
def home():
    """Shows the home/welcome page."""
    return render_template("index.html")


# --------------------------------------------------------------------
# ROUTE: View All Students
# --------------------------------------------------------------------
@app.route("/students")
def students():
    """
    Fetches all students from the database and displays them
    in a table using the students.html template.
    """
    conn = get_db_connection()
    all_students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("students.html", students=all_students)


# --------------------------------------------------------------------
# ROUTE: Add a New Student
# --------------------------------------------------------------------
@app.route("/add", methods=["GET", "POST"])
def add_student():
    """
    GET  -> shows the 'Add Student' form.
    POST -> receives the form data and inserts a new student
            into the database.
    """
    if request.method == "POST":
        # Get form values sent from add_student.html
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        course = request.form.get("course", "").strip()
        age = request.form.get("age", "").strip()

        # --- Simple error handling / validation ---
        if not name or not email or not course or not age:
            return render_template(
                "add_student.html",
                error="All fields are required. Please fill in every field."
            )

        try:
            age = int(age)
        except ValueError:
            return render_template(
                "add_student.html",
                error="Age must be a number."
            )

        # Insert the new student into the database.
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO students (name, email, course, age) VALUES (?, ?, ?, ?)",
            (name, email, course, age)
        )
        conn.commit()
        conn.close()

        # Redirect to the students list page after adding.
        return redirect(url_for("students"))

    # If it's a GET request, just show the empty form.
    return render_template("add_student.html", error=None)


# --------------------------------------------------------------------
# ROUTE: Edit an Existing Student
# --------------------------------------------------------------------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_student(id):
    """
    GET  -> shows the edit form pre-filled with the student's current data.
    POST -> updates the student's data in the database.
    The <int:id> in the route captures the student's ID from the URL.
    """
    conn = get_db_connection()
    student = conn.execute(
        "SELECT * FROM students WHERE id = ?", (id,)
    ).fetchone()

    # If no student with this ID exists, show a simple error message.
    if student is None:
        conn.close()
        return "Student not found.", 404

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        course = request.form.get("course", "").strip()
        age = request.form.get("age", "").strip()

        if not name or not email or not course or not age:
            conn.close()
            return render_template(
                "edit_student.html",
                student=student,
                error="All fields are required."
            )

        try:
            age = int(age)
        except ValueError:
            conn.close()
            return render_template(
                "edit_student.html",
                student=student,
                error="Age must be a number."
            )

        conn.execute(
            "UPDATE students SET name = ?, email = ?, course = ?, age = ? WHERE id = ?",
            (name, email, course, age, id)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("students"))

    conn.close()
    return render_template("edit_student.html", student=student, error=None)


# --------------------------------------------------------------------
# ROUTE: Delete a Student
# --------------------------------------------------------------------
@app.route("/delete/<int:id>")
def delete_student(id):
    """
    Deletes the student with the given ID from the database,
    then redirects back to the students list.
    """
    conn = get_db_connection()
    conn.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("students"))


# --------------------------------------------------------------------
# Run the application
# --------------------------------------------------------------------
if __name__ == "__main__":
    # Create the database/table (if it doesn't already exist) before starting.
    init_db()
    # debug=True gives helpful error pages while you're learning.
    app.run(debug=True)
