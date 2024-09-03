import asyncio
import telegram
from datetime import datetime
import os 
import json
from dotenv import load_dotenv
import random
load_dotenv(verbose=True)

BOT_TOKEN = os.getenv('BOT_TOKEN')
current_time = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

class telegramBot():
    def __init__(self):
        self.bot = telegram.Bot(token=BOT_TOKEN)
        self.checkbot()
        self.chat_id = asyncio.run(self.load_chat_id())
        self.good_word_list = self.load_good_word_list()             

    def load_good_word_list(self):
        with open('good_word_list.json', 'r', encoding='utf-8') as file:
            word_list = json.load(file)
        return word_list['yourRgood']

    async def checkbot(self):
        print(await self.bot.get_me())

    async def load_chat_id(self):
        updates = (await self.bot.get_updates())
        chat_id = updates[0]['message']['chat']['id']
        return chat_id

    async def main(self, text):
        good_word4you = random.choice(self.good_word_list)
        await self.bot.send_message(text=f'{current_time} / {good_word4you}', chat_id=self.chat_id)
        print('message send!')

if __name__ == '__main__':
    telegram_bot_1 = telegramBot()
    asyncio.run(telegram_bot_1.main('test'))