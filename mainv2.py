import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ChatJoinRequest
from aiogram import Router

API_TOKEN = 'YOUR_API_HERE'
WELCOME_MESSAGE = "Welcome to the Group. Glad to see you here! <3"

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()
dp.include_router(router)

@router.chat_join_request()
async def handle_chat_join_request(chat_join_request: ChatJoinRequest):
    logger.debug(f"Chat Join Request Received: {chat_join_request}")  # Логирование в начале

    try:
        await bot.approve_chat_join_request(chat_join_request.chat.id, chat_join_request.from_user.id)
        await bot.send_message(chat_join_request.chat.id, WELCOME_MESSAGE)
        logger.info(f"Approved join request from {chat_join_request.from_user.id}")
    except Exception as e:
        logger.error(f"Error approving join request: {e}")

    logger.debug(f"Chat Join Request Processed: {chat_join_request}")  # Логирование в конце

async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())
