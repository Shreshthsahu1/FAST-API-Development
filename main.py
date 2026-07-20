from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to FastAPI!"

#home, contact, about
@app.get("/home")
def home():
    return "Welcome to the Home page!"

@app.get("/contact")
def contact():
    return "Contact us at contact@example.com"

@app.get("/about")
def about():
    return "Learn more about us!"

#asynchronous api
@app.get("/async")
async def async_api():
    return "This is an asynchronous endpoint!"

@app.post("/post")
def post_api():
    return "Post API!"

@app.put("/put")
def put_api():
    return "Put API!"

@app.delete("/delete")
def delete_api():
    return "Delete API!"

@app.get("/getdata")
def get_student_data():
    students = [
        {"id": 1, "name": "Shreshth", "Roll No.": 51, "dept": "Computer Science"},
        {"id": 2, "name": "Sahu", "Roll No.": 52, "dept": "Mechanical Engineering"},
        {"id": 3, "name": "Gopal", "Roll No.": 53, "dept": "Electrical Engineering"}]
    return students

@app.get("/getdata/{id:int}")
def request_param(id):
    return f"student id: {id}"

# create student list with name, if entered name is in list/data simply return it otherwise return message data not found
@app.get("/getdata/{name}")
def request_param(name):   
    return f"student name: {name}"



#query parameter : to get filtered and sorted result
# ?department=It&cgpa=5
#/student?department=CSE & cgpa=9.5
@app.get("/student")
def get_query(department: str, cgpa: float):
    students = [
        {"id": 1, "name": "Shreshth", "Roll No.": 51, "dept": "cse", "cgpa": 9.5},
        {"id": 2, "name": "Sahu", "Roll No.": 52, "dept": "Mechanical Engineering", "cgpa": 8.5},
        {"id": 3, "name": "Gopal", "Roll No.": 53, "dept": "Electrical Engineering", "cgpa": 7.5}]

#acc to query parameter print result
#cgpa => 5.5 department = CSE
    result = []
    for s in students:
        if s["dept"] == department and s["cgpa"] >= cgpa:
            result.append(s)

    return result   

#Pydantic : validation tool by which python automatically validate request and response

from pydantic import BaseModel
class Student(BaseModel):
    id: int
    name: str
    roll_no: int
    dept: str
    cgpa: float

students = []

@app.post("/student/add")
def student_model(student: Student):
    students.append(student)
    return f"Student Added : {students}"
