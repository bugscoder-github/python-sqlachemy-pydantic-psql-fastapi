from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.crud import *
from db.models.skill_assess import Skill_assess, SkillType

router = APIRouter()

@router.post("/")
def get_skill_assess(query: SkillType, db: Session = Depends(get_db)):
    result = get_data(db, Skill_assess, query.dict())
    if not result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result