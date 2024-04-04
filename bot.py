import yaml
from datetime import datetime



def read_events_from_yaml(file_path):
    """
    Читает события из YAML файла.

    :param file_path: Путь к файлу YAML.
    :return: Список событий.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
        return data.get('events', [])

# Предполагается, что файл events.yaml находится в том же каталоге, что и скрипт.
data = read_events_from_yaml('events.yaml')
print(data)


def find_today_events(events):
    """
    Ищет события на сегодняшнюю дату.

    :param events: Список событий.
    :return: Список событий на сегодня.
    """
    today = datetime.now().date()  # Сегодняшняя дата
    # Фильтруем события, дата которых совпадает с сегодняшней
    return [event for event in events if event['date'] == today]


def main():
    file_path = 'events.yaml'
    events = read_events_from_yaml(file_path)
    today_events = find_today_events(events)
    
    if today_events:
        print("События на сегодня:")
        for event in today_events:
            print(f"- {event['description']}")
    else:
        print("На сегодня событий нет.")

if __name__ == '__main__':
    main()

    
