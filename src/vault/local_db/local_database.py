import json
from typing import List, Set

from src.models.cla import Cla
from src.models.obf import Obf
from src.services.bin_file_reader import BinFileReader
from src.services.bin_file_writer import BinFileWriter
from src.vault.decorators.inject_logger import inject_global_logger
from src.vault.local_db.record import Record


class LocalDatabase:
    _logger: any
    __records: [Record]

    @inject_global_logger
    def __init__(self, file_location: str):
        self.__file_location = file_location

        bytes_data_list = BinFileReader().read_binary_file(self.__file_location)

        self.__add_from_bytes_data_list(bytes_data_list)

    def __del__(self):
        BinFileWriter.write_binary_file(self.__file_location)

        pass

    @staticmethod
    def __decode_record(raw_record: bytes) -> {}:
        return json.dumps(str(Cla(False, raw_record)))

    def __add_from_bytes_data_list(self, bytes_data_list: [bytes]):
        for bytes_data in bytes_data_list:
            self.__records.append(self.__decode_record(bytes_data))

    def __save_records_to_file(self):
        bytes_data_list = []

        for record in self.__records:
            str_record = json.dumps({'key': record.get_key(), 'entries': record.get_entries_list()})
            bytes_data_list.append(Obf(False, str_record))

