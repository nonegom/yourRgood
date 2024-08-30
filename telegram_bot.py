import asyncio
import telegram
from datetime import datetime
import os 

BOT_TOKEN = os.getenv('BOT_TOKEN')
current_time = datetime.today().strftime("%Y-%m-%d %H:%M:%S")


class telegramBot():
    def __init__(self):
        self.bot = telegram.Bot(token=BOT_TOKEN)
        self.chat_id = asyncio.run(self.load_chat_id())

    async def checkbot(self):
        print(await self.bot.get_me())

    async def load_chat_id(self):
        updates = (await self.bot.get_updates())
        chat_id = updates[0]['message']['chat']['id']
        return chat_id


    async def main(self, message):
        await self.bot.send_message(text=f'너는 아주 잘하고 있어! 최고야!!', chat_id=self.chat_id)
        print('message send!')

if __name__ == '__main__':
    telegram_bot_1 = telegramBot()
    asyncio.run(telegram_bot_1.main('test'))