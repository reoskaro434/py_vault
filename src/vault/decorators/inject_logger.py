from src.vault.globals import LOGGER


def inject_global_logger(fnc):
    def enhanced_func(self, *args, **kwargs):
        self._logger = LOGGER

        fnc(self, *args, **kwargs)

    return enhanced_func
