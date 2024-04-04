from event_finder import EventFinder

def main():
    file_path = 'events.yaml'  # Укажите актуальный путь к файлу
    event_finder = EventFinder(file_path)
    events = event_finder.read_events_from_yaml()
    today_events = event_finder.find_events_by_today_day(events)
    
    if today_events:
        print("События на сегодня:")
        for event in today_events:
            print(f"- {event['description']}")
    else:
        print("На сегодня событий нет.")

if __name__ == '__main__':
    main()

    
