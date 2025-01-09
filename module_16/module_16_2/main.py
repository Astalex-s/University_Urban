from fastapi import FastAPI, Path
from typing import Annotated


# Создаем экземпляр приложения FastAPI
app = FastAPI()


# Определение базового маршрута
@app.get("/")
async def get_main_page() -> str:
    return "Главная страница"


@app.get("/user/{username}/{age}")
async def get_user_info(username: Annotated[str, Path(min_length=5,
                                                      max_length=20,
                                                      description="Enter username",
                                                      example="Your name")],
                        age: Annotated[int, Path(ge=18,
                                                 le=120,
                                                 description="Enter age",
                                                 example=24)]):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}."


@app.get("/user/admin")
async def get_admin_page() -> str:
    return "Вы вошли как администартор"


@app.get("/user/{user_id}")
async def get_user_number(user_id: Annotated[int, Path(gt=1, le=100, description="Enter User ID", example=12)]):
    return f"Вы вошли как пользователь № {user_id}"
