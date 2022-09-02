from random import random
from typing import Union, Optional
from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import random

app = FastAPI()
templates = Jinja2Templates(directory="templates/")


def add_random_number(num: int) -> int:
    print(f"{num = }")
    return num +  random.randint(0, 100)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/login/")
def login(username: str = Form(), email: str = Form(), password: str = Form()):
    return {"username": username, "email": email}


@app.get("/form", response_class=HTMLResponse)
def get_form(request: Request):
    result = "Input details"
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})


@app.post("/form")
def post_form(request: Request, task_name: Optional[str] = Form(None), show_plot: Optional[bool] = Form(None), 
              algo: str = Form(...), columns: str = Form(...), file: UploadFile = File(...)):
    file_name = file.filename
    columns = columns.split(",")
    
    result = dict(task_name = task_name, show_plot = show_plot, algo = algo, columns=columns, file_name = file_name)
    print(result)
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})