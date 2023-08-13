import json

from src.models.cla import Cla
from src.models.obf import Obf
from src.vault.local_db.entry import Entry


class Record:
    __key: str
    __entries_list: [Entry]

    def __init__(self, obfuscated_data: Obf):
        data = json.loads(bytes(Cla(False, bytes(obfuscated_data))))

        self.__key = data.get('key')
        self.__entries_list = [Entry(e.get('value'), e.get('creation_timestamp')) for e in data.get('entries')]

    def get_key(self) -> str:
        return self.__key

    def get_entries_list(self) -> [Entry]:
        return self.__entries_list

    def get_newest_entry(self) -> Entry | None:
        self.__entries_list.sort(key=lambda e: e.timestamp, reverse=True)

        return self.__entries_list[0] if len(self.__entries_list) > 0 else None
