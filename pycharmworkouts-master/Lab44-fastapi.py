#pip install fastapi uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def helloworld():
    print("Hello Guys..How are you")
    return {"msg": "Hello Guys..How are you"}

@app.get("/hello")
def fn_hello():
    return {"msg": "Hello, Guys!"}

@app.get("/hello/{name}")
def fn_hello_name(name: str):
    return {"msg": f"Hello, {name}!"}

@app.get("/addnum/{n1}/{n2}")
def addnumber(n1:int,n2:int):
    return {"msg": f"sum of {n1} and {n2} is {n1+n2}"}


class users(BaseModel):
    id:int
    uname:str
    pwd:str

@app.post("/saveuser")
def saveuser(obj:users):
    print(obj.id)
    print(obj.uname)
    print(obj.pwd)
    return {
        "status": "success",
        "message": "User info saved successfully"
    }
@app.post("/writedata")
def writedata():
    return {"message": "written successfully"}

#curl -X POST "http://127.0.0.1:8000/saveuser" -H "Content-Type: application/json" -d '{"id": 1, "uname": "testuser", "pwd": "secret123"}'
