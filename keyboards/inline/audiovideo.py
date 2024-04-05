from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button = InlineKeyboardMarkup()
btn_audio = InlineKeyboardButton(text="Audio", callback_data="audio")
btn_video = InlineKeyboardButton(text="Video", callback_data="video")

button.row(btn_audio, btn_video)