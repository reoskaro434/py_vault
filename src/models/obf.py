from src.services.bytes_coder import BytesCoder


class Obf:
    __obfuscated_data: bytes

    def __init__(self, is_obfuscated: bool, data: str | bytes):
        if isinstance(data, str):
            bytes_data = BytesCoder.text_to_bytes(data)
        else:
            bytes_data = data

        if is_obfuscated:
            self.__obfuscated_data = bytes_data
            return

        b64_data = BytesCoder.b64_encode(bytes_data)
        self.__obfuscated_data = BytesCoder.invert_bits(b64_data)

    def __str__(self):
        return BytesCoder.bytes_to_text(self.__obfuscated_data)

    def __bytes__(self):
        return self.__obfuscated_data
