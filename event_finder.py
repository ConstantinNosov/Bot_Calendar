import yaml
from datetime import datetime

class EventFinder:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_events_from_yaml(self):
        """
        Читает события из YAML файла.

        :return: Список событий.
        """
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
            return data.get('events', [])

    def find_today_events(self, events):
        """
        Ищет события на сегодняшнюю дату.

        :param events: Список событий.
        :return: Список событий на сегодня.
        """
        today = datetime.now().date()  # Сегодняшняя дата
        # Фильтруем события, дата которых совпадает с сегодняшней
        return [event for event in events if event['date'] == today]