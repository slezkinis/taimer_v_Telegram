import os
import ptbot
from pytimeparse import parse


TG_TOKEN = os.environ['TOKEN']
def wait(chat_id, message):
  if message == '/start':
    bot.send_message(chat_id, 'Бот запущен!')
    bot.send_message(chat_id, 'На сколько запустить таймер?')
    return
  time = parse(message)
  message_id = bot.send_message(chat_id, 'Запускаю таймер...')
  bot.create_countdown(time, notify_progress, author_id=chat_id, message_id=message_id, time=time)
  bot.create_timer(time, end, author_id=chat_id, message=message)

def notify_progress(secs_left, author_id, message_id, time):
  secs_past = int(time - secs_left)
  bot.update_message(author_id, message_id, f'Осталось {secs_left} секунд\n{render_progressbar(time, secs_past)}')
def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix) 
def end(author_id, message):
    bot.send_message(author_id, 'Время вышло!')

bot = ptbot.Bot(TG_TOKEN)
bot.reply_on_message(wait)
bot.run_bot()