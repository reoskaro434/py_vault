import json

from src.models.obf import Obf
from src.vault.local_db.record import Record

if __name__ == "__main__":
    sample = {
        'key': 'value_of_key',
        'entries': [
            {
                'creation_timestamp': 12345,
                'value': 'sample_value'
            }
        ]
    }

    obf_data = Obf(False, json.dumps(sample))

    record = Record(obf_data)

    record.get_key()



