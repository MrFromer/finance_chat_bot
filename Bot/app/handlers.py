from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.methods import send_sticker
from aiogram import html
import app.keyboards as kb
import sys
sys.path.append('E://Studying_project/')
from Parser_news.news_parser_1 import currency
from Parser_for_ML.parser_for_ml import candle_data
from chatgpt import result_gpt


router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(text=f"""
Привет, {html.bold(message.from_user.full_name)}👋
Наш бот выдаёт информацию по валютным парам, так же он может проводить анализ и давать тебе советы, братишка!

🤖Для этого нажми кнопку ниже и выбери валютную пару, так же ты можешь добавить интересующие тебя валютные пары в избранное!
Чтобы узнать все доступные комманды напиши 👉🏼 /help
""", reply_markup=kb.main_menu)
    await message.delete()


@router.message(Command('help'))
async def help(message: Message):
    #await bot.send_sticker(chat_id= message.chat.id, sticker='CAACAgIAAxkBAAEKoOVlPeSr9mMp7nttYSLV4Q1Z3OeeVwAChwEAAiteUwt4J9ZNhn9pYDAE')
    await message.answer(text= """
    🤩Давай поможем тебе, братишка, сейчас наш бот реагирует на следующие комманды:
/pares - все доступные валютные пары
/favorite - избранные валютные пары
/news - новости по фондовому рынку
                         
🗿Остальной функционал в разработке """)
    await message.delete()

@router.message(F.text == "💸Валютные пары")
async def Pares(message: Message):
    await message.answer(text='🔥Выбери интересующую валютную пару:', reply_markup=kb.ikb_currency)
    await message.delete()

@router.message(Command('pares'))
async def Pares_cmd(message: Message):
    await message.answer(text='🔥Выбери интересующую валютную пару:', reply_markup=kb.ikb_currency)
    await message.delete()

TEXT_NEWS = ''' '''
currency_list = currency()
for i in currency_list:
    TEXT_NEWS+=str(i)
    TEXT_NEWS+=str('\n МНЕНИЕ GPT: {result_gpt}')

@router.message(F.text == "🧾Новости")
async def Pares(message: Message):
    await message.answer(text = TEXT_NEWS)
    await message.delete()

@router.message(Command('news'))
async def Pares_cmd(message: Message):
    await message.answer(text = TEXT_NEWS)
    await message.delete()

@router.message(F.text == "⭐️Избранное")
async def Pares(message: Message):
    await message.answer(text='Пока что функция находится в разработке')
    await message.delete()

@router.message(Command('favorite'))
async def Pares_cmd(message: Message):
    await message.answer(text='Пока что функция находится в разработке')
    await message.delete()



TEXT_EUR_USD = f'''
На данный момент следующая ситуация по валютной паре EUR/USD:
{candle_data}
'''
@router.callback_query(F.data == 'eur/usd')
async def eur_usd(callback: CallbackQuery):
    await callback.answer('Вы выбрали валютную пару EUR/USD')
    await callback.message.edit_text(text= TEXT_EUR_USD, reply_markup = kb.ikb_return)

@router.callback_query(F.data == 'return')
async def return_ikb(callback: CallbackQuery):
    await callback.answer('Вы вернулись в меню выбора валютных пар')
    await callback.message.edit_text(text='🔥Выбери интересующую валютную пару:', reply_markup=kb.ikb_currency)

@router.message()
async def check_message(message: Message) -> None:
    try:
        await message.answer(chat_id=message.chat.id, text='Если вы хотите узнать информацию по валютным парам, напишите /pares')
    except TypeError:
        await message.answer(text='Это не известная мне команда, напишите /help')
