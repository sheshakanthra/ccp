from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login():
    return {"token": "dummy-jwt-token"}

@router.post("/register")
def register():
    return {"msg": "User registered"}
