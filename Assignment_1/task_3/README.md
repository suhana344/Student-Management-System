# Task 3: Authentication and Authorization in Flask API

## Introduction
This project demonstrates authentication and authorization using a Flask REST API. It has two types of users: Employee and Admin. Each user has different access permissions.

## Features
- Employee and Admin login.
- Token-based authentication.
- Employees can view employee records.
- Admins can view, add, and delete employee records.
- Employees cannot perform admin-only actions.
- Invalid login details and tokens are rejected.

## Technologies Used
- Python
- Flask
- REST API
- JSON
- PowerShell for testing

## Demo Login Credentials
| Role | Username | Password |
|---|---|---|
| Employee | employee | emp123 |
| Admin | admin | admin123 |

*These are demonstration credentials for this educational project only.*

## API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| POST | `/login` | Login and receive an authentication token |
| GET | `/employees` | View employee records (authenticated users) |
| POST | `/employees` | Add an employee (Admin only) |
| DELETE | `/employees/<id>` | Delete an employee (Admin only) |

## How to Run the Project
1. Install Flask:
   `py -m pip install flask`
2. Open the Task_3 folder in the terminal.
3. Run the application:
   `py app.py`
4. The API will run at:
   `http://127.0.0.1:5002`

## Testing
The following operations were tested successfully:
- Employee login.
- Admin login.
- Employee viewing employee records.
- Admin adding an employee.
- Admin deleting an employee.
- Employee being denied permission to add an employee.

## Note
This is an educational demonstration. Employee data and authentication tokens are stored in memory and reset when the server restarts. Demo credentials are hardcoded and should not be used for real accounts.

## Conclusion
This project demonstrates how authentication verifies a user's identity and authorization controls what that user is allowed to do.