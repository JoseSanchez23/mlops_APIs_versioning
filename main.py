from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
import uuid

api = FastAPI(
    title="User API",
    description="API para manejar usuarios",
    version="1.0.0"
)

users_data = {}

@api.post("/users", tags=["Users"])
async def user_sign_up(data: dict):
    user_id = str(uuid.uuid4())
    name = data.get("name")
    email = data.get("email")
    username = data.get("username")

    if not name or not email or not username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Todos los campos (name, email, username) son obligatorios"
        )

    users_data[user_id] = {
        "name": name,
        "email": email,
        "username": username
    }

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "response": f"Se ha creado exitosamente el usuario {username} con el email {email}",
            "id": user_id,
            "name": name
        }
    )

@api.get("/users/{user_id}", tags=["Users"])
async def get_user(user_id: str):
    user = users_data.get(user_id)


    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=user
    )
