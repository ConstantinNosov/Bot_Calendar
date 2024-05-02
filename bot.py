from event_finder import EventFinder
from config import bot_token, chat_id
import time
from bot_lib import TelegramBot


bot = TelegramBot(chat_id, bot_token)


def main():
    file_path = 'events.yaml'  # Укажите актуальный путь к файлу
    event_finder = EventFinder(file_path)
    events = event_finder.read_events_from_yaml()
    today_events = event_finder.find_events_by_today_day(events)
    
    if today_events:
        for event in today_events:
            bot.send_message(f"- {event['description']}")
    else:
        bot.send_message("На сегодня задач нет.")

while True:
    main()
    time.sleep(10)