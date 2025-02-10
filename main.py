from fastapi import FastAPI
from db.db_connection import init_table
from routers.user import router as user_router
from routers.skill_assess import router as skill_assess_router

# init_table()

app = FastAPI()

#router
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(skill_assess_router, prefix="/skill-assess", tags=["skill-assess"])