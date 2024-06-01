from db import Session, User, Task
from sqlalchemy import select
from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()


    
class User_Data(BaseModel):
    login: str
    password: str
    
    
class Task_Data(BaseModel):
    creator:str
    title: str
    content: str 



@app.get("/users", response_model=list[User_Data])
def get_users():
    with Session.begin() as session:
        users = session.scalars(select(User)).all()
        return users
        


@app.post("/create_user")
def create_user(user: User_Data):
    with Session.begin() as session:
        user = User(**user.model_dump())
        session.add(user)
        return user
    

@app.put("/user/{user_id}")
def update_user(user_id: int, user:User_Data):
    with Session.begin() as session:
        current_user = session.scalar(select(User).where(User.id == user_id))
        if user:
            current_user.login = user.login
            current_user.password = user.password
            
            return current_user
        
            
        
        

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    with Session.begin() as session:
        current_user = session.scalar(select(User).where(User.id == user_id))
        session.delete(current_user)
        return "User deleted successfully"


@app.get("/tasks")
def get_tasks():
    with Session.begin() as session:
        task = session.scalars(select(Task)).all()
        return task
    
@app.post("/create_task")
def create_task(task: Task_Data):
    with Session.begin() as session:
        task = Task(**task.model_dump())
        session.add(task)
        return task


@app.put("/update_task/{task_id}")
def update_task(task: Task_Data, task_id: int):
    with Session.begin() as session:
        updated_task = session.scalar(select(Task).where(Task.id == task_id))
        if task:
            updated_task.creator = task.creator
            updated_task.title = task.title
            updated_task.content = task.content
            return updated_task
        

@app.delete("/task/{task_id}")
def delete_task(task_id: int):
    with Session.begin() as session:
        task = session.scalar(select(Task).where(Task.id == task_id))
        session.delete(task)
        return "task deleted successfully"