import asyncio
import logging
from aiogram import Bot, Dispatcher, types, Router
from config_reader import config
from datetime import datetime
from aiogram.types import (
    CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message, BotCommandScopeAllPrivateChats,
)

from handlers.registration import user_new_router
from handlers.old import user_old_router
from common.bot_commands_list import privat

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())

# Диспетчер
router = Router()
dp = Dispatcher()
dp.include_router(user_new_router)
dp.include_router(user_old_router)
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=privat,scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=["message", "inline_query", "chat_member"])


asyncio.run(main())