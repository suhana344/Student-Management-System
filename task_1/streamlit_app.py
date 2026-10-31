
import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/students"

# Website title
st.title("Student Management System")
st.write("Manage student records easily.")

# Display all students
st.subheader("All Students")

response = requests.get(API_URL)

if response.status_code == 200:
    students = response.json()

    if students:
        st.dataframe(students, use_container_width=True)
    else:
        st.info("No students found.")
else:
    st.error("Unable to connect to Flask API.")


# Add a new student
st.subheader("Add New Student")

with st.form("add_student_form"):

    name = st.text_input("Student Name")
    department = st.text_input("Department")
    email = st.text_input("Email")

    add = st.form_submit_button("Add Student")

    if add:
        data = {
            "name": name,
            "department": department,
            "email": email
        }

        response = requests.post(API_URL, json=data)

        if response.status_code == 201:
            st.success("Student added successfully!")
            st.rerun()
        else:
            st.error(response.json()["error"])


# Update student information
st.subheader("Update Student")

with st.form("update_student_form"):

    student_id = st.number_input(
        "Student ID",
        min_value=1,
        step=1
    )

    new_name = st.text_input("New Name")
    new_department = st.text_input("New Department")
    new_email = st.text_input("New Email")

    update = st.form_submit_button("Update Student")

    if update:
        data = {
            "name": new_name,
            "department": new_department,
            "email": new_email
        }

        response = requests.put(
            f"{API_URL}/{student_id}",
            json=data
        )

        if response.status_code == 200:
            st.success("Student updated successfully!")
            st.rerun()
        else:
            st.error(response.json()["error"])


# Delete student
st.subheader("Delete Student")

delete_id = st.number_input(
    "Student ID to Delete",
    min_value=1,
    step=1,
    key="delete_id"
)

if st.button("Delete Student"):

    response = requests.delete(
        f"{API_URL}/{delete_id}"
    )

    if response.status_code == 200:
        st.success("Student deleted successfully!")
        st.rerun()
    else:
        st.error(response.json()["error"])
