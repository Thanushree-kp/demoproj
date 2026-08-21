# Student Management System

A simple full-stack web application to manage student records — built as a beginner-friendly learning project.

## Description

This project lets you **Add**, **View**, **Edit**, and **Delete** student records through a clean web interface. It was built to learn how a frontend, backend, and database connect together in a real project, and how to publish that project to GitHub.

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask)
- **Database:** SQLite
- **Version Control:** Git & GitHub

## Features

- Add a new student (Name, Email, Course, Age)
- View all students in a table
- Edit existing student details
- Delete a student record
- Simple, responsive design
- Basic input validation and error handling

## Project Structure

```
student-management-system/
│
├── app.py
├── init_db.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_student.html
│   ├── students.html
│   └── edit_student.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## How to Install and Run

1. Clone or download this repository.
2. Open the folder in VS Code (or any editor).
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the app:
   ```bash
   python app.py
   ```
6. Open your browser at:
   ```
   http://127.0.0.1:5000
   ```

The SQLite database (`database.db`) is created automatically the first time you run the app.

## Screenshots

_Add screenshots of your app here once it's running, e.g._

`![Home Page](screenshots/home.png)`

`![Student List](screenshots/students.png)`
