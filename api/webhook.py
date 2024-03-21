from api import app
from app import config
from app.misc import bot


@app.get('/api/webhook')
async def set_webhook():
    await bot.set_webhook(config.WEBHOOK_URL)
    return {"status": "ok"}
