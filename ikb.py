import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InputFile
from aiogram.utils.markdown import hbold
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Дізнатись цыну та час виготовлення ключів', callback_data='price'),
    ],
    [
        InlineKeyboardButton(text='Подивитись розташування майстерні на карті', callback_data='map'),
    ],
    [
        InlineKeyboardButton(text='zsdfhxjh2', callback_data='zhfdh2'),
    ]
])

