from src.vault.decorators.inject_logger import inject_global_logger


class BinFileReader:
    _logger: any

    @inject_global_logger
    def __init__(self):
        pass

    def read_binary_file(self, location: str) -> [bytes]:
        try:
            with open(location, 'rb') as f:
                return bytes.splitlines(f.read())

        except Exception as ex:
            self._logger.error(ex)
            raise ex
