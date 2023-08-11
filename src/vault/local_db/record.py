from src.models.obf import Obf


class Record:
    __pattern: str = '[]* []*'
    __obfuscated_data: [Obf]

    def __init__(self, obfuscated_data: [Obf]):
        self.__obfuscated_data = obfuscated_data


