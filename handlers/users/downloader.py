from aiogram import types
from loader import dp
from pytube import YouTube
from io import BytesIO
from aiogram.dispatcher.dispatcher import Text
from keyboards.inline.audiovideo import button


@dp.message_handler(Text(startswith='!'))
async def my_btn(message: types.Message):
    await message.answer(text='btn', reply_markup=button)


@dp.message_handler(Text(startswith="http"))
async def test(message: types.Message):
    link = message.text
    url = YouTube(link)
    buffer = BytesIO()
    if url.check_availability() is None:
        # audio = url.streams.get_audio_only()  # mp3
        video = url.streams.get_by_itag(18)  # video
        print(url.streams.filter(progressive=True))  # mp3 kachestva 760 360 144
        # audio.stream_to_buffer(buffer)
        video.stream_to_buffer(buffer)
        buffer.seek(0)
        # await message.answer_audio(audio=buffer, caption=url.title)
        await message.answer_video(video=buffer, caption=url.title)
    else:
        await message.answer("Xatolik")