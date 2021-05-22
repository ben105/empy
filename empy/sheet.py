from empy.config import Config
from empy.headers import create_header_keys
from pandas import DataFrame


def get_seconds_sheet(excel_data_frames):
    return excel_data_frames.get(Config.seconds_sheet, DataFrame())

def get_minutes_sheet(excel_data_frames):
    return excel_data_frames.get(Config.minutes_sheet, DataFrame())

def get_hours_sheet(excel_data_frames):
    return excel_data_frames.get(Config.hours_sheet, DataFrame())

def get_days_sheet(excel_data_frames):
    return excel_data_frames.get(Config.days_sheet, DataFrame())

def parse_all_rows(sheet_data_frame):
    header_keys = create_header_keys(sheet_data_frame)
    all_row_pairs = []
    for i in range(len(sheet_data_frame)):
        row_pairs = parse_single_row(sheet_data_frame.loc[i, :], header_keys)
        all_row_pairs.append(row_pairs)
    return all_row_pairs

def parse_single_row(row, header_keys):
    pairs = []
    for header_key in header_keys:
        pairs.append((header_key, row.loc[header_key]))
    return pairs
