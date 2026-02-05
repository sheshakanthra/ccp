from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["Auth"])

class LoginRequest(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    email: str
    password: str
    full_name: str
    role: str = "citizen"

@router.post("/login")
def login(creds: LoginRequest):
    # Mock Login Logic for Demo
    role = "citizen"
    if "admin" in creds.email.lower():
        role = "admin"
        
    return {
        "token": "dummy-jwt-token",
        "user": {
            "email": creds.email,
            "full_name": "Demo User",
            "role": role,
            "id": 1
        }
    }

@router.post("/register")
def register(user: RegisterRequest):
    # In a real app, save to DB.
    # Here we just acknowledge.
    return {"msg": "User registered", "user": user.dict()}
