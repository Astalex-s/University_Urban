from fastapi import FastAPI


# Создаем экземпляр приложения FastAPI
app = FastAPI()


# Определение базового маршрута
@app.get("/")
async def get_main_page() -> str:
    return "Главная страница"


@app.get("/user")
async def get_user_info(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}."


@app.get("/user/admin")
async def get_admin_page() -> str:
    return "Вы вошли как администартор"


@app.get("/user/{user_id}")
async def get_user_number(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"
