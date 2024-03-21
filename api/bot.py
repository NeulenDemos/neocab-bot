from aiogram import types, Dispatcher, Bot
from api import app
from app import config
from app.bot import dp, bot


@app.post(config.WEBHOOK_PATH)
async def bot_webhooks_endpoint(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)
