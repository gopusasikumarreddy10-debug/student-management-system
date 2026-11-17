from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
import sqlite3
from pydantic import BaseModel,Field
from fastapi.responses import RedirectResponse

app=FastAPI()

templates = Jinja2Templates(
    directory="templates"
)

class Student(BaseModel):
    name:str=Field(min_length=4,max_length=20)
    age:int=Field(ge=18,le=60)
    gender:str
    marks:int=Field(ge=1,le=100)
    course:str
    image:str
    status:int
    

def get_connection():
    connection=sqlite3.connect(
        "student.db"
    )
    return connection

get_connection()

def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    
    q="""
    create table if not exists students(
        id integer primary key autoincrement,
        name text,
        age integer,
        gender text,
        marks integer,
        course text,
        image text,
        status integer
    )
    """
    
    cursor.execute(q)
    connection.commit()
    connection.close()

create_table()

@app.get("/")
def home_page(req:Request):
    
    connection = get_connection()
    cursor = connection.cursor()
    
    q="""
    select * from students
    """
    cursor.execute(q)
    students = cursor.fetchall()
    connection.close()
    
    return templates.TemplateResponse(
        request=req,
        name="home.html",
        context={
            "stds":students
        }
    )


@app.get("/add-student")
def add_student(req:Request):
    return templates.TemplateResponse(
        request=req,
        name="add-std.html",
        context={}
    )
 
   
@app.post("/add-student")

def student_details(
    name=Form(),
    age=Form(),
    gender=Form(),
    marks=Form(),
    course=Form(),
    image=Form(),
    status=Form()
    
):
    
    std_obj=Student(
    name=name,
    age=age,
    gender=gender,
    marks=marks,
    course=course,
    image=image,
    status=status
    )
    
    values=(std_obj.name,std_obj.age,std_obj.gender,std_obj.marks,std_obj.course,std_obj.image,std_obj.status)
    
    connection = get_connection()
    cursor = connection.cursor()
    
    q="""
    insert into students
    (name,age,gender,marks,course,image,status)
    values
    (?,?,?,?,?,?,?)
    """
    cursor.execute(q,(values))
    connection.commit()
    connection.close()
    
    return RedirectResponse(url="/",status_code=303)

@app.get("/students/{std_id}")
def get_single_student(req:Request , std_id:int):
    
    connection = get_connection()
    cursor = connection.cursor()
    
    q="""
    select * from students where id=?
    """
    
    cursor.execute(q,(std_id,))
    student = cursor.fetchone()
    connection.close()
    
    return templates.TemplateResponse(
        request=req,
        name="single-std.html",
        context={
            "std":student
        }
    )
    
@app.post("/student/delete/{std_id}")
def delete_student(std_id:int):
    
    connection = get_connection()
    cursor = connection.cursor()
    
    q="""
    delete from students where id = ?
    """
    cursor.execute(q,(std_id,))
    
    connection.commit()
    connection.close()
    
    return RedirectResponse(url="/",status_code=303)
    

    
@app.get("/student/edit/{std_id}")
def edit_page(req:Request,std_id:int):
    
    connection  = get_connection()
    cursor = connection.cursor()
    
    q ="select * from students where id = ?"
    cursor.execute(q,(std_id,))
    student=cursor.fetchone()
   
    connection.close()

    return templates.TemplateResponse(
        request=req,
        
        name ="edit.html",
        context= {
            "std":student
        }
    )
    

@app.post("/student/edit/{std_id}")
def update_student(
    std_id:int,
    name=Form(),
    age=Form(),
    gender=Form(),
    marks=Form(),
    course=Form(),
    image=Form(),
    status=Form()
    
):
    
    std_obj=Student(
    name=name,
    age=age,
    gender=gender,
    marks=marks,
    course=course,
    image=image,
    status=status
    )
    
    values=(std_obj.name,std_obj.age,std_obj.gender,std_obj.marks,std_obj.course,std_obj.image,std_obj.status,std_id)
    
    connection = get_connection()
    cursor = connection.cursor()
    
    q="""
    update students set
    name=?,
    age=?,
    gender=?,
    marks=?,
    course=?,
    image=?,
    status=?
    where id =?
    """
    cursor.execute(q,(values))
    connection.commit()
    connection.close()
    
    return RedirectResponse(url="/",status_code=303)

