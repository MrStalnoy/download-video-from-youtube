
import telebot
from pytube import YouTube

bot = telebot.TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Это бот для скачивания видео с YouTube. Отправь мне ссылку на видео, чтобы начать загрузку.')

@bot.message_handler(func=lambda message: True)
def download_video(message):
    try:
        video_url = message.text
        yt = YouTube(video_url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video.download()
        bot.reply_to(message, 'Видео успешно загружено.')
    except Exception as e:
        bot.reply_to(message, f'Ошибка: {str(e)}')

bot.polling()