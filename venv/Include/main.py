from aiogram import executor
from tortoise import Tortoise, run_async
from loguru import logger
from config import *
import core.handlers
import core.helpers
import asyncio

async def main():
    logger.info("Tortoise inited!")
    await Tortoise.init(
        db_url="sqlite://tokens.sqlite3",
        modules={"models": ["models"]}
    )
    await Tortoise.generate_schemas()

if __name__ == "__main__":
    run_async(main())
    executor.start_polling(dp, skip_updates=True)


