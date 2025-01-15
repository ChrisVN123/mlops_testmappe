from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


from enum import Enum
class ItemEnum(Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/restric_items/{item_id}")
def read_item(item_id: ItemEnum):
    return {"item_id": item_id}


database = {'username': ["cvn"], 'password': ["passwordet"]}

@app.post("/login/")
def login(username: str, password: str):
    username_db = database['username']
    password_db = database['password']
    if username not in username_db and password not in password_db:
        with open('database.csv', "a") as file:
            file.write(f"{username}, {password} \n")
        username_db.append(username)
        password_db.append(password)
    return "login saved"