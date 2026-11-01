# Student Management System

## Introduction
The Student Management System is a database-driven application developed using Python. It allows users to manage student records through a web interface.

## Technologies Used
- Python
- Flask
- SQLite
- Streamlit
- Requests

## Features
- Add new student records
- View all students
- View an individual student
- Update student information
- Delete student records

## Project Structure
- `app.py` – Flask API and database operations.
- `streamlit_app.py` – Streamlit user interface.
- `students.db` – SQLite database, created automatically when the Flask application runs.

## How to Run

1. Install the required libraries:
   `py -m pip install flask streamlit requests`

2. Start the Flask API:
   `py app.py`

3. Open a second terminal and start Streamlit:
   `py -m streamlit run streamlit_app.py`

4. Open the local Streamlit URL shown in the terminal.

## Developed For
Compiler/Programming Assignment – Task 1
