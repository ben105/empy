HEADER_NAME = 0
DATA_VALUE = 1

TS_TIMESTAMP_KEY = 'timestamp'
TS_VALUES_KEY = 'values'

def convert_to_time_series(pairs):
    timestamp_pair = pairs.pop(0)
    timestamp = timestamp_pair[DATA_VALUE]
    return {
        TS_TIMESTAMP_KEY: timestamp,
        TS_VALUES_KEY: convert_pairs_to_map(pairs),
    }

def convert_pairs_to_map(pairs):
    hash_map = {}
    for pair in pairs:
        hash_map.update({
            pair[HEADER_NAME]: pair[DATA_VALUE]
        })
    return hash_map
