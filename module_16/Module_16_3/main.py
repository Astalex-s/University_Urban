from fastapi import FastAPI, Path
from typing import Annotated


# Создаем экземпляр приложения FastAPI
app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


# Возвращаем словарь users
@app.get("/users")
async def get_users() -> dict:
    return users


# Добавляем в словарь пользователя
@app.post("/user/{username}/{age}")
async def post_user(username: Annotated[str, Path(min_length=5,
                                                  max_length=20,
                                                  description="Enter username",
                                                  example="Your name")],
                    age: Annotated[int, Path(ge=18,
                                             le=80,
                                             description="Enter age",
                                             example=24)]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


# Обновляем значения из словоря users
@app.put("/user/{user_id}/{username}/{age}")
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
                                            example=22)]) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


# Удаляем значения из словоря users
@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[str, Path(description="Enter user_id",
                                                   example=2)]) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"
