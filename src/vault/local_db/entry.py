class Entry:
    __value: str
    __timestamp: int

    def __init__(self, value: str, timestamp: int):
        self.__value = value
        self.__timestamp = timestamp

    def get_value(self):
        return self.__value

    def get_timestamp(self):
        return self.__timestamp
