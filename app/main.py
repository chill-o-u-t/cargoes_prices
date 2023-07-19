from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api import main_router
from app.core import settings, DATABASE_CONFIG

app = FastAPI(title=settings.app_title)

app.include_router(main_router)

register_tortoise(
    app=app,
    config=DATABASE_CONFIG
)
