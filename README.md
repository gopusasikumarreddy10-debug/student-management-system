# 🎓 Student Management System

## 📌 Project Overview

The **Student Management System** is a web-based application developed using Python FastAPI and SQLite database. It helps users manage student information efficiently.

This application allows users to add new students, view student details, update existing student information, and delete student records.

The project follows CRUD (Create, Read, Update, Delete) operations and uses HTML templates with Jinja2 for displaying web pages.

## 🚀 Features

- **Add Student:** Add new student details.
- **View Students:** Display all registered students.
- **View Single Student:** View individual student information using student ID.
- **Update Student:** Edit existing student details.
- **Delete Student:** Remove student records from the database.
- **Form Validation:** Validate student details using Pydantic.
- **Database Management:** Store student information using SQLite.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | Web framework |
| SQLite | Database |
| HTML | Web page structure |
| CSS | Web page styling |
| Jinja2 | HTML templating |
| Pydantic | Data validation |
| Uvicorn | Application server |

## 📂 Project Structure

```text
Student-Management-System/
│
├── main.py
├── student.db
│
├── templates/
│   ├── home.html
│   ├── add-std.html
│   ├── single-std.html
│   └── edit.html
│
└── README.md
```

## 🗄️ Database Structure

**Database Name:** student.db

**Table Name:** students

| Column Name | Data Type | Description |
|---|---|---|
| id | INTEGER | Primary key |
| name | TEXT | Student name |
| age | INTEGER | Student age |
| gender | TEXT | Student gender |
| marks | INTEGER | Student marks |
| course | TEXT | Student course |
| image | TEXT | Student image path or URL |
| status | INTEGER | Student status |

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### Step 2: Open Project Folder

```bash
cd Student-Management-System
```

### Step 3: Install Required Packages

```bash
pip install fastapi uvicorn jinja2 python-multipart
```

### Step 4: Run the Application

```bash
uvicorn main:app --reload
```

### Step 5: Open in Browser

```text
http://127.0.0.1:8000
```

## 🔗 Application Routes

| HTTP Method | Route | Description |
|---|---|---|
| GET | `/` | Display all students |
| GET | `/add-student` | Open add student page |
| POST | `/add-student` | Add student details |
| GET | `/students/{std_id}` | View single student |
| POST | `/student/delete/{std_id}` | Delete student |
| GET | `/student/edit/{std_id}` | Open edit student page |
| POST | `/student/edit/{std_id}` | Update student details |

## 🔄 CRUD Operations

1. **Create:** Add new student information into the database.
2. **Read:** Retrieve and display student information.
3. **Update:** Modify existing student details.
4. **Delete:** Remove student information from the database.

## 🎯 Project Objectives

- To develop a simple student management web application.
- To understand FastAPI framework and its functionality.
- To implement CRUD operations using SQLite.
- To understand database connectivity with Python.
- To implement form handling and data validation.
- To understand Jinja2 template rendering.

## ▶️ Future Enhancements

- Student login and authentication.
- Search students by name or ID.
- Upload student profile pictures.
- Generate student performance reports.
- Add pagination and filtering.
- Improve the user interface and dashboard.

## 👨‍💻 Author

**Sasi Kumar Reddy Gopu**

## 📌 Conclusion

The Student Management System provides a simple and effective way to manage student records. Through this project, I gained practical knowledge of Python, FastAPI, SQLite database connectivity, HTML templates, and CRUD operations.
