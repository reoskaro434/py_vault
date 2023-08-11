from logging import Logger

from src.vault.decorators.inject_logger import inject_global_logger


class BinFileWriter:
    _logger: any

    @inject_global_logger
    def __init__(self):
        pass

    def write_binary_file(self, location: str, data_list: [bytes]):
        try:
            with open(location, 'wb') as f:
                f.writelines([data + b'\n' for data in data_list])
            return True

        except Exception as ex:
            self._logger.error(ex)

        return False

