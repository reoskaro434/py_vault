from src.services.bin_file_reader import BinFileReader
from src.services.bin_file_writer import BinFileWriter
from src.vault.decorators.inject_logger import inject_global_logger


class LocalDatabase:
    _logger: any

    @inject_global_logger
    def __init__(self, file_location: str):
        self.__file_location = file_location

        binary_data = BinFileReader().read_binary_file(self.__file_location)

    def __del__(self):
        BinFileWriter.write_binary_file(self.__file_location)

        pass
