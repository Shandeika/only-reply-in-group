import logging
import os
from typing import Union

import aiogram
from aiogram.filters import BaseFilter
from aiogram.types import Message

bot = aiogram.Bot(token=os.getenv("BOT_TOKEN"))
dp = aiogram.Dispatcher()

logging.basicConfig(level=logging.INFO)


class ChatTypeFilter(BaseFilter):
    def __init__(self, chat_type: Union[str, list]):
        self.chat_type = chat_type

    async def __call__(self, message: Message) -> bool:
        if isinstance(self.chat_type, str):
            return message.chat.type == self.chat_type
        else:
            return message.chat.type in self.chat_type


@dp.message(ChatTypeFilter(chat_type=["group", "supergroup"]))
async def message_handler(message: Message):
    if not message.reply_to_message:
        await message.delete()


dp.run_polling(bot)
