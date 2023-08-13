class Entry:
    __value: str
    __create_time: int

    def __init__(self, value: str, create_time: int):
        self.__value = value
        self.__create_time = create_time

    def get_value(self):
        return self.__value

    def get_timestamp(self):
        return self.__create_time

    def __get__(self):
        return {'value': self.__value, 'create_time': self.__create_time}
