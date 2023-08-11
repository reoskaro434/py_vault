from src.services.bytes_coder import BytesCoder


class Cla:
    __clarified_data: bytes

    def __init__(self, is_clarified: bool, data: str | bytes):
        if isinstance(data, str):
            bytes_data = BytesCoder.text_to_bytes(data)
        else:
            bytes_data = data

        if is_clarified:
            self.__clarified_data = bytes_data
            return

        inverted_data = BytesCoder.invert_bits(bytes_data)
        self.__clarified_data = BytesCoder.b64_decode(inverted_data)

    def __str__(self):
        return BytesCoder.bytes_to_text(self.__clarified_data)

    def __bytes__(self):
        return self.__clarified_data

    def __len__(self):
        return len(self.__clarified_data)

