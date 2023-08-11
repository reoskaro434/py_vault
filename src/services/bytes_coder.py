import base64


class BytesCoder:
    __mask = 0xFF

    @staticmethod
    def invert_bits(bytes_data: bytes) -> bytes:
        return bytes(BytesCoder.__mask ^ byte for byte in bytes_data)

    @staticmethod
    def b64_encode(bytes_data: bytes) -> bytes:
        return base64.b64encode(bytes_data)

    @staticmethod
    def b64_decode(bytes_data: bytes) -> bytes:
        return base64.b64decode(bytes_data)

    @staticmethod
    def text_to_bytes(text: str) -> bytes:
        return text.encode('utf-8')

    @staticmethod
    def bytes_to_text(bytes_data: bytes) -> str:
        return bytes_data.decode('utf-8')
