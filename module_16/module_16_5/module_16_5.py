from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from typing import Annotated
from typing import List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates


# Создаем экземпляр приложения FastAPI
app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    username: str
    age: int


users: List[User] = []


# Возвращаем список users

@app.get("/")
async def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}")
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        for user in users:
            if user.id == user_id:
                return templates.TemplateResponse("users.html", {"request": request, "user": user})
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


# Добавляем в словарь пользователя
@app.post("/user/{username}/{age}")
async def post_user(username: Annotated[str, Path(min_length=5,
                                                  max_length=20,
                                                  description="Enter username",
                                                  example="Your name")],
                    age: Annotated[int, Path(ge=18,
                                             le=80,
                                             description="Enter age",
                                             example=24)]) -> User:
    new_id = max((t.id for t in users), default=0) + 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


# Обновляем значения из списка users
@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def put_user(user_id: Annotated[int, Path(ge=1,
                                                le=100,
                                                description="Enter user_id",
                                                example=2)],
                   username: Annotated[str, Path(min_length=5,
                                                 max_length=20,
                                                 description="Enter username",
                                                 example="Your name")],
                   age: Annotated[int, Path(ge=18,
                                            le=80,
                                            description="Enter age",
                                            example=22)]) -> User:

    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


# Удаляем значения из словоря users
@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: Annotated[int, Path(description="Enter user_id",
                                                   example=2)]) -> User:
    for i, user in enumerate(users):
        if user.id == user_id:
            users.pop(i)
            return user

    raise HTTPException(status_code=404, detail="User was not found")
