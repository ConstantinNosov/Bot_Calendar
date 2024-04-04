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
        Ищет события на сегодняшнюю дату полностью учитывая год месяц и число.
        :param events: Список событий.
        :return: Список событий на сегодня.
        """
        today = datetime.now().date()  # Сегодняшняя дата
        # Фильтруем события, дата которых совпадает с сегодняшней
        return [event for event in events if event['date'] == today]
    

    def find_events_by_today_day(self, events):
        """
        Ищет события, которые происходят в текущий день месяца, не учитывая месяц и год.
        :param events: Список событий.
        :return: Список событий, день которых совпадает с текущим днем месяца.
        """
        today_day = datetime.now().day  # Текущий день месяца
        return [event for event in events if event['date'].day == today_day]
    

    