from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.crud import *
from db.models.user import User, UserRegister, UserLogin, UserSchema

router = APIRouter()

@router.post("/")
def user(db: Session = Depends(get_db)):
    result = get_data(db, User)
    if not result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

# register new user
@router.post("/register")
def user_register(user_data: UserRegister, db: Session = Depends(get_db)):
    result = insert_data(db, User, user_data.dict())
    if not result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

# login
@router.post("/login")
def user_login(user_data: UserLogin, db: Session = Depends(get_db)):
    result = get_data(db, User, user_data.dict())
    if not result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@router.post("/{email}", summary="Get user details")
def user(email: str, db: Session = Depends(get_db)):
    result = get_data(db, User, {"email": email})
    if not result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

# update user details using their email
@router.post("/{email}/update")
def user_update(user_data: UserSchema, email: str, db: Session = Depends(get_db)):
    result = update_data(db, User, {"email": email}, user_data.dict())
    if result:
        print(f"User with email {email} updated successfully.")
    else:
        # print(f"User with email {email} not found.")
        raise HTTPException(status_code=400, detail={result["error"]})
    
    return result