OUTPUT_HEADERS = ["Total Kw/Hrs", "Off Peak $'s", "Part Peak $'s", "Peak $'s", "Total $'s"]

def create_header_keys(data_frame):
    return list(filter(is_valid, data_frame.columns))

def is_valid(column_name):
    if not column_name or column_name.startswith('Unnamed'):
        return False
    return True
