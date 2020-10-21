from aiogram import executor
from tortoise import Tortoise, run_async
from loguru import logger
from config import *
from fastapi import FastAPI
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
import core.handlers
import core.helpers
import asyncio
import uvicorn


app = FastAPI(
    title="FondLeaderBot"
)


register_tortoise(
    app,
    db_url="sqlite://tokens.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    uvicorn.run("main:app",
                debug=True)


